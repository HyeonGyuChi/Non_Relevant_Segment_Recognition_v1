import timm
import torch
import torch.nn as nn
from core.model.mobilevit import MobileViT_Feat



def generate_timm_model(args):
    model = TIMM(args)
    
    return model


class TIMM(nn.Module):
    """
        SOTA model usage
        1. resnet18
        2. repvgg_b0
        3. mobilenetv3_large_100
        
    """
    def __init__(self, args):
        super().__init__()
        
        self.args = args
        self.use_emb = False
        self.emb_only = args.use_emb_only
        
        arch_name = self.args.model
        
        # help documents - https://fastai.github.io/timmdocs/create_model (how to use feature_extractor in timm)
        if self.args.model == 'mobile_vit':
            # https://github.com/chinhsuanwu/mobilevit-pytorch
            dims = [64, 80, 96]
            channels = [16, 16, 24, 24, 48, 48, 64, 64, 80, 80, 320]

            model = MobileViT_Feat((256, 256), dims, channels, num_classes=2, expansion=2)
            
            self.feature_module = model
            n_feat = channels[-1]
        else:
            model = timm.create_model(arch_name, pretrained=True)
            
            if self.args.model == 'swin_large_patch4_window7_224':
                self.feature_module = nn.Sequential(
                    *list(model.children())[:-2],
                )
                self.gap = nn.AdaptiveAvgPool1d(1)
            else:
                self.feature_module = nn.Sequential(
                    *list(model.children())[:-1]
                )
            n_feat = model.num_features
        
        if self.args.experiment_type == 'theator':
            for p in self.feature_module.parameters():
                p.requires_grad = False
                
        self.classifier = nn.Linear(n_feat, 2)
        
        if 'hem-emb' in self.args.hem_extract_mode or 'hem-focus' in self.args.hem_extract_mode:
            self.use_emb = True
            self.proxies = nn.Parameter(torch.randn(n_feat, 2))
        
        else : # off-line and genral
            self.classifier = nn.Sequential(
                nn.Dropout(p=self.args.dropout_prob, inplace=True),
                nn.Linear(n_feat, 2)
            )
        
        if self.args.use_online_mcd:
            self.dropout = nn.Dropout(self.args.dropout_prob)
        
    def forward(self, x):
        features = self.feature_module(x)
        
        if self.args.model == 'swin_large_patch4_window7_224':
            features = self.gap(features.permute(0, 2, 1)).squeeze()            
        
        features = torch.nn.functional.normalize(features, p=2, dim=-1)
            
        if self.args.use_online_mcd: 
            if self.training: 
                features = self.dropout(features)
            else:
                mcd_outputs = []
                for _ in range(self.args.n_dropout):
                    drop = self.dropout(features).unsqueeze(0)    
                    mcd_outputs.append(drop)
                    
                a = torch.vstack(mcd_outputs)
                
                features = torch.mean(a, 0)

        if self.emb_only:
            return features
        else:   
            output = self.classifier(features.view(x.size(0), -1))
            
            if self.use_emb and self.training:
                return features, output
            else:
                return output