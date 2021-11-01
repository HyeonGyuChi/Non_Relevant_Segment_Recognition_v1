for trial in 1 2 3 4 5 6 7 8 9 10; do
    for fold in 1 2 3; do
        nohup python inference_flow.py \
        --fold ${fold} \
        --trial ${trial} \
        --model "mobilenetv3_large_100" \
        --cuda_list '5' \
        --save_path '/code/OOB_Recog/logs/hem-emb-mobilenet-ver4' \
        --max_epoch 150 \
        --batch_size 128 \
        --lr_scheduler "step_lr" \
        --lr_scheduler_step 5 \
        --lr_scheduler_factor 0.9 \
        --train_method "hem-emb4" \
        > /dev/null


    done

    for fold in 1 2 3; do
        nohup python inference_flow.py \
        --fold ${fold} \
        --trial ${trial} \
        --model "mobilenetv3_large_100" \
        --cuda_list '5' \
        --save_path '/code/OOB_Recog/logs/hem-emb-mobilenet-ver3' \
        --max_epoch 150 \
        --batch_size 128 \
        --lr_scheduler "step_lr" \
        --lr_scheduler_step 5 \
        --lr_scheduler_factor 0.9 \
        --train_method "hem-emb3" \
        > /dev/null
    done

    for fold in 1 2 3; do
        nohup python inference_flow.py \
        --fold ${fold} \
        --trial ${trial} \
        --model "mobilenetv3_large_100" \
        --cuda_list '5' \
        --save_path '/code/OOB_Recog/logs/hem-emb-mobilenet-ver1' \
        --max_epoch 150 \
        --batch_size 128 \
        --lr_scheduler "step_lr" \
        --lr_scheduler_step 5 \
        --lr_scheduler_factor 0.9 \
        --train_method "hem-emb" \
        > /dev/null
    done
done