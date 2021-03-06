# 21.11.19 off-line top ratio별 실험
# [고정] hem_extract_mode:hem-softmax-offline / random_seed:3829 / IB_ratio:0.10
# [변경] top_ratio

top_ratio_array=(0.10 0.20 0.30);

for top_ratio in "${top_ratio_array[@]}";
do
    nohup python visual_flow.py \
        --fold "1" \
        --trial 1 \
        --use_wise_sample \
        --model "mobilenetv3_large_100" \
        --pretrained \
        --use_lightning_style_save \
        --max_epoch 50 \
        --batch_size 256 \
        --lr_scheduler "step_lr" \
        --lr_scheduler_step 5 \
        --lr_scheduler_factor 0.9 \
        --cuda_list "5" \
        --random_seed 3829 \
        --IB_ratio 3 \
        --hem_extract_mode "hem-softmax-offline" \
        --top_ratio ${top_ratio} \
        --stage "hem_train" \
        --inference_fold "1" \
        --experiments_sheet_dir "/OOB_RECOG/results/offline-top_ratio-experiment" \
        --save_path "/OOB_RECOG/logs/offline-top_ratio-experiment" > /dev/null
done;