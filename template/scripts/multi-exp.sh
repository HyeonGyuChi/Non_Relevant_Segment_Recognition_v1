# Multi-stage MobileNet
nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '1' \
--IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
--WS_ratio 3 \
--use_wise_sample \
--multi_stage \
--n_stage 3 \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/mobilenet-multi-stage' > /dev/null &


# Multi-stage ResNet18
nohup python visual_flow.py --fold '1' --trial 1 --model "resnet18" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '2' \
--IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
--WS_ratio 3 \
--use_wise_sample \
--multi_stage \
--n_stage 3 \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/resnet18-multi-stage' > /dev/null &

# Multi-stage RepVGG
nohup python visual_flow.py --fold '1' --trial 1 --model "repvgg-a0" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '7' \
--IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
--WS_ratio 3 \
--use_wise_sample \
--multi_stage \
--n_stage 3 \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-repvgg/repvgg-a0-multi-stage' > /dev/null &



# Multi-stage MobileNet
nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '4' \
--IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
--WS_ratio 3 \
--use_wise_sample \
--multi_stage \
--n_stage 3 \
--use_neg_proxy \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-mobilenet/mobilenet-neg-multi-stage' > /dev/null &


# Multi-stage ResNet18
nohup python visual_flow.py --fold '1' --trial 1 --model "resnet18" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '5' \
--IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
--WS_ratio 3 \
--use_wise_sample \
--multi_stage \
--n_stage 3 \
--use_neg_proxy \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/resnet18-neg-multi-stage' > /dev/null &

# Multi-stage RepVGG
nohup python visual_flow.py --fold '1' --trial 1 --model "repvgg-a0" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '5' \
--IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
--WS_ratio 3 \
--use_wise_sample \
--multi_stage \
--n_stage 3 \
--use_neg_proxy \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-repvgg/repvgg-a0-neg-multi-stage' > /dev/null &





# Multi-model
nohup python visual_flow.py --fold '1' --trial 1 --model "multi-model" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '6' \
--IB_ratio 3 --random_seed 3829 --stage 'general_train' --inference_fold '1' \
--WS_ratio 3 \
--use_wise_sample \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/multi-model-ws-general' > /dev/null &

nohup python visual_flow.py --fold '2' --trial 1 --model "multi-model" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '7' \
--IB_ratio 3 --random_seed 3829 --stage 'general_train' --inference_fold '2' \
--WS_ratio 3 \
--use_wise_sample \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/multi-model-ws-general' > /dev/null &

nohup python visual_flow.py --fold '3' --trial 1 --model "multi-model" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '7' \
--IB_ratio 3 --random_seed 3829 --stage 'general_train' --inference_fold '3' \
--WS_ratio 3 \
--use_wise_sample \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/multi-model-ws-general' > /dev/null &



nohup python visual_flow.py --fold '1' --trial 1 --model "multi-model" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '3' \
--IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
--WS_ratio 3 \
--use_wise_sample \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/multi-model-proxy' > /dev/null &

nohup python visual_flow.py --fold '2' --trial 1 --model "multi-model" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '4' \
--IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '2' \
--WS_ratio 3 \
--use_wise_sample \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/multi-model-proxy' > /dev/null &

nohup python visual_flow.py --fold '3' --trial 1 --model "multi-model" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '5' \
--IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '3' \
--WS_ratio 3 \
--use_wise_sample \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/multi-model-proxy' > /dev/null &







# Multi-stage MobileNet
nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '0' \
--IB_ratio 3 --random_seed 3829 --stage 'general_train' --inference_fold '1' \
--WS_ratio 3 \
--use_oversample \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/mobilenet-general-oversample' > /dev/null &


# Multi-stage ResNet18
nohup python visual_flow.py --fold '1' --trial 1 --model "resnet18" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '3' \
--IB_ratio 3 --random_seed 3829 --stage 'general_train' --inference_fold '1' \
--WS_ratio 3 \
--use_oversample \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/resnet18-general-oversample' > /dev/null &

# Multi-stage RepVGG
nohup python visual_flow.py --fold '1' --trial 1 --model "repvgg-a0" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '4' \
--IB_ratio 3 --random_seed 3829 --stage 'general_train' --inference_fold '1' \
--WS_ratio 3 \
--use_oversample \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/repvgg-a0-general-oversample' > /dev/null &





# Multi-stage MobileNet
nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '5' \
--IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
--WS_ratio 3 \
--use_wise_sample \
--use_oversample \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/mobilenet-proxy-oversample' > /dev/null &


# Multi-stage ResNet18
nohup python visual_flow.py --fold '1' --trial 1 --model "resnet18" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '6' \
--IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
--WS_ratio 3 \
--use_wise_sample \
--use_oversample \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/resnet18-proxy-oversample' > /dev/null &

# Multi-stage RepVGG
nohup python visual_flow.py --fold '1' --trial 1 --model "repvgg-a0" --max_epoch 100 \
--batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '7' \
--IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
--WS_ratio 3 \
--use_wise_sample \
--use_oversample \
--sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs-other-fold/repvgg-a0-proxy-oversample' > /dev/null &