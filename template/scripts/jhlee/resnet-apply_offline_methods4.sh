# 21.11.26 off-line mc assets 뽑기
# [고정] hem_extract_mode:all-offline / random_seed:3829 / IB_ratio:3 / WS_ratio:2 / mc:5

top_ratio=(0.20);

WS_ratio=3;
n_dropout=1;
IB_ratio=3;

for ratio in "${top_ratio[@]}";
do
    nohup python ../apply_offline_methods_flow.py \
        --fold "1" \
        --trial 1 \
        --use_wise_sample \
        --WS_ratio ${WS_ratio} \
        --model "resnet18" \
        --pretrained \
        --use_lightning_style_save \
        --max_epoch 50 \
        --batch_size 256 \
        --lr_scheduler "step_lr" \
        --lr_scheduler_step 5 \
        --lr_scheduler_factor 0.9 \
        --cuda_list "4" \
        --random_seed 3829 \
        --IB_ratio ${IB_ratio} \
        --hem_extract_mode "all-offline" \
        --top_ratio ${ratio} \
        --n_dropout ${n_dropout} \
        --stage "hem_train" \
        --inference_fold "1" \
        --hem_per_patient \
        --experiments_sheet_dir "/OOB_RECOG/results/1205-resnet18-apply_offline_methods-all-offline-IB_ratio=${IB_ratio}-ws_ratio=${WS_ratio}-MC=${n_dropout}-experiment" \
        --save_path "/OOB_RECOG/logs/1205-resnet18-apply_offline_methods-all-offline-IB_ratio=${IB_ratio}-ws_ratio=${WS_ratio}-MC=${n_dropout}-experiment" > /dev/null
done;