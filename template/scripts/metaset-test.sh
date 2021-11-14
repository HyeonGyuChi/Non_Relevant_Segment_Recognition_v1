# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '0' \
# --IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-focus-online' --inference_fold '1' \
# --sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs/hem-online-3-1-step-test2' > /dev/null &

# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '1' \
# --IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-focus-online' --inference_fold '1' \
# --sampling_type 2 --emb_type 2 --save_path '/code/OOB_Recog/logs/hem-online-3-1-step-test2' > /dev/null &

# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '2' \
# --IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-focus-online' --inference_fold '1' \
# --sampling_type 3 --emb_type 2 --save_path '/code/OOB_Recog/logs/hem-online-3-1-step-test2' > /dev/null &

# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '3' \
# --IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-focus-online' --inference_fold '1' \
# --sampling_type 4 --emb_type 2 --save_path '/code/OOB_Recog/logs/hem-online-3-1-step-test2' > /dev/null &


# python visual_flow.py \
#     --fold '1' \
#     --trial 1 \
#     --model "mobilenetv3_large_100" \
#     --max_epoch 100 \
#     --batch_size 256 \
#     --lr_scheduler "step_lr" \
#     --lr_scheduler_step 5 \
#     --lr_scheduler_factor 0.9 \
#     --cuda_list '5' \
#     --IB_ratio 3 \
#     --random_seed 3829 \
#     --stage 'general_train' \
#     --inference_fold '1' \
#     --save_path '/OOB_RECOG/logs/WS-general-IB_ratio=3'

# python visual_flow.py \
#     --fold '1' \
#     --trial 1 \
#     --model "mobilenetv3_large_100" \
#     --max_epoch 100 \
#     --batch_size 256 \
#     --lr_scheduler "step_lr" \
#     --lr_scheduler_step 5 \
#     --lr_scheduler_factor 0.9 \
#     --cuda_list '6' \
#     --IB_ratio 4 \
#     --random_seed 3829 \
#     --stage 'general_train' \
#     --inference_fold '1' \
#     --save_path '/OOB_RECOG/logs/WS-general-IB_ratio=4'

# python visual_flow.py \
#     --fold '1' \
#     --trial 1 \
#     --model "mobilenetv3_large_100" \
#     --max_epoch 100 \
#     --batch_size 256 \
#     --lr_scheduler "step_lr" \
#     --lr_scheduler_step 5 \
#     --lr_scheduler_factor 0.9 \
#     --cuda_list '7' \
#     --IB_ratio 5 \
#     --random_seed 3829 \
#     --stage 'general_train' \
#     --inference_fold '1' \
#     --save_path '/OOB_RECOG/logs/WS-general-IB_ratio=5'


python visual_flow.py \
    --fold '1' \
    --trial 1 \
    --model "mobilenetv3_large_100" \
    --max_epoch 2 \
    --batch_size 256 \
    --lr_scheduler "step_lr" \
    --lr_scheduler_step 5 \
    --lr_scheduler_factor 0.9 \
    --cuda_list '4' \
    --IB_ratio 3 \
    --random_seed 3829 \
    --stage 'hem_train' \
    --hem_extract_mode 'hem-softmax-offline' \
    --inference_fold '1' \
    --save_path '/OOB_RECOG/logs/metaset_hem-softmax-offline_RATIO=3'



# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '2' \
# --IB_ratio 5 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
# --emb_type 3 --save_path '/code/OOB_Recog/logs/hem-online-5-1-step-new' > /dev/null &



# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '6' \
# --IB_ratio 4 --random_seed 10 --stage 'general_train' --inference_fold '1' \
# --emb_type 3 --save_path '/code/OOB_Recog/logs/general-4-1-step-org-seed' > /dev/null &

# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '7' \
# --IB_ratio 5 --random_seed 10 --stage 'general_train' --inference_fold '1' \
# --emb_type 3 --save_path '/code/OOB_Recog/logs/general-5-1-step-org-seed' > /dev/null &


# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '0' \
# --IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
# --emb_type 3 --save_path '/code/OOB_Recog/logs/hem-online-3-1-step-new' > /dev/null &

# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '1' \
# --IB_ratio 4 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
# --emb_type 3 --save_path '/code/OOB_Recog/logs/hem-online-4-1-step-new' > /dev/null &

# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '2' \
# --IB_ratio 5 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
# --emb_type 3 --save_path '/code/OOB_Recog/logs/hem-online-5-1-step-new' > /dev/null &



# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '0' \
# --IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
# --emb_type 2 --save_path '/code/OOB_Recog/logs/hem-online-3-1-step-test' > /dev/null &

# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '1' \
# --IB_ratio 4 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
# --emb_type 2 --save_path '/code/OOB_Recog/logs/hem-online-4-1-step-test' > /dev/null &

# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '2' \
# --IB_ratio 5 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
# --emb_type 2 --save_path '/code/OOB_Recog/logs/hem-online-5-1-step-test' > /dev/null &




# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '3' \
# --IB_ratio 5 --random_seed 5686 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
# --emb_type 1 --save_path '/code/OOB_Recog/logs/hem-online-5-1-step-new-seed' > /dev/null &

# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '4' \
# --IB_ratio 5 --random_seed 7789 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
# --emb_type 1 --save_path '/code/OOB_Recog/logs/hem-online-5-1-step-new-seed' > /dev/null &


# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '4' \
# --IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
# --use_wise_sample \
# --sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs/hem-online-3-1-step-ws-emb' > /dev/null &


# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '4' \
# --IB_ratio 3 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-focus-online' --inference_fold '1' \
# --use_wise_sample \
# --sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs/hem-online-3-1-step-ws-focus' > /dev/null &



# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '4' \
# --IB_ratio 4 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
# --use_wise_sample \
# --sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs/hem-online-4-1-step-ws-emb' > /dev/null &


# nohup python visual_flow.py --fold '1' --trial 1 --model "mobilenetv3_large_100" --max_epoch 100 \
# --batch_size 256 --lr_scheduler "step_lr" --lr_scheduler_step 5 --lr_scheduler_factor 0.9 --cuda_list '3' \
# --IB_ratio 5 --random_seed 3829 --stage 'hem_train' --hem_extract_mode 'hem-emb-online' --inference_fold '1' \
# --use_wise_sample \
# --sampling_type 1 --emb_type 2 --save_path '/code/OOB_Recog/logs/hem-online-5-1-step-ws-emb' > /dev/null &