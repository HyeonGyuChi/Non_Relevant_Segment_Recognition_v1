import os
import cv2
from PIL import Image
import torch
import numpy as np
import pandas as pd
import glob
import matplotlib
import argparse

from pandas import DataFrame as df
from tqdm import tqdm

matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint

import torch

from Model import CAMIO
from torchvision import transforms

import datetime

from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

import pickle

import time
import json

def test_video() :
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--model_path', type=str, help='trained model_path')
    # robot_3 | /logs/robot/OOB/robot_oob_train_3/epoch=2-val_loss=0.0541.ckpt
    # robot_4 | /logs/robot/OOB/robot_oob_train_4/epoch=9-val_loss=0.0597.ckpt
    

    # os.getcwd() + '/logs/robot/OOB/robot_oob_train_1/epoch=12-val_loss=0.0303.ckpt' // OOB = 1
    # os.getcwd() + '/logs/OOB_robot_test7/epoch=6-val_loss=0.0323.ckpt' // OOB = 0
    parser.add_argument('--data_dir', type=str,
                        default='/data/ROBOT/Video', help='video_path :) ')

    parser.add_argument('--anno_dir', type=str,
                        default='/data/OOB', help='annotation_path :) ')

    parser.add_argument('--results_save_dir', type=str, help='inference results save path')

    parser.add_argument('--mode', type=str,
                        default='robot', choices=['ROBOT', 'LAPA'], help='inference results save path')
    
    ## trained model (you should put same model as trained model)
    parser.add_argument('--model', type=str,
                        choices=['resnet18', 'resnet34', 'resnet50', 'wide_resnet50_2', 'resnext50_32x4d', 'mobilenet_v2', 'mobilenet_v3_small', 'squeezenet1_0'], help='trained backborn model')
    
    # inference frame step
    parser.add_argument('--inference_step', type=int, default=5, help='inference frame step')

    # inference video
    '''
    trainset = ['R_1', 'R_2', 'R_3', 'R_4', 'R_5', 'R_6', 'R_7', 'R_10', 'R_13', 'R_14', 'R_15', 'R_18', 
                'R_19', 'R_48', 'R_56', 'R_74', 'R_76', 'R_84', 'R_94', 'R_100', 'R_117', 'R_201', 'R_202', 'R_203', 
                'R_204', 'R_205', 'R_206', 'R_207', 'R_209', 'R_210', 'R_301', 'R_302', 'R_304', 'R_305', 'R_313']

    valset = ['R_17', 'R_22', 'R_116', 'R_208', 'R_303']
    '''
    parser.add_argument('--test_videos', type=str, nargs='+',
                        choices=['R_1', 'R_2', 'R_3', 'R_4', 'R_5', 'R_6', 'R_7', 'R_10', 'R_13', 'R_14', 'R_15', 'R_17', 'R_18', 
                'R_19', 'R_22', 'R_48', 'R_56', 'R_74', 'R_76', 'R_84', 'R_94', 'R_100', 'R_116', 'R_117', 'R_201', 'R_202', 'R_203', 
                'R_204', 'R_205', 'R_206', 'R_207', 'R_208', 'R_209', 'R_210', 'R_301', 'R_302', 'R_303', 'R_304', 'R_305', 'R_313'],
                         help='inference video')
    
    # infernece assets root path
    parser.add_argument('--inference_assets_dir', type=str, help='inference assets root path')

    args, _ = parser.parse_known_args()

    ### ### create results folder for save args and log.txt ### ###
    try :
        if not os.path.exists(args.results_save_dir) :
            os.makedirs(args.results_save_dir)
    except OSError :
        print('ERROR : Creating Directory, ' + args.results_save_dir)

    # save args log
    with open(os.path.join(args.results_save_dir, 'commandline_args.txt'), 'w') as f:
        json.dump(args.__dict__, f, indent=2)

    log_txt='\n\n=============== \t\t COMMAND ARGUMENT \t\t ============= \n\n'
    log_txt+=json.dumps(args.__dict__, indent=2)

    # start time stamp
    startTime = time.time()
    s_tm = time.localtime(startTime)
    
    log_txt+='\n\n=============== \t\t INFERNECE TIME \t\t ============= \n\n'
    log_txt+='STARTED AT : \t' + time.strftime('%Y-%m-%d %I:%M:%S %p \n', s_tm)
    
    save_log(log_txt, os.path.join(args.results_save_dir, 'log.txt')) # save log

    ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
    

    '''
    # load args log
    parser = ArgumentParser()
    args = parser.parse_args()
    with open('commandline_args.txt', 'r') as f:
        args.__dict__ = json.load(f)
    '''

    '''    
    data_transforms = {
        'val': transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
    }
    '''
    

    # dirscirbe exception, inference setting for each mode
    if args.mode == 'LAPA' :        
        # test_video_for_lapa()
        exit(0) # not yet support
        pass

    else : # robot
        test_hparams = {
            'optimizer_lr' : 0, # dummy (this option use only for training)
            'backborn_model' : args.model # (for train, test)
        }

        print('')
        print('')
        print(test_hparams)

        model = CAMIO.load_from_checkpoint(args.model_path, config=test_hparams)

        model.cuda()
        model.eval()

        print('\n\t=== model_loded for ROBOT ===\n')

        # starting inference
        test_video_for_robot(args.data_dir, args.anno_dir, args.inference_assets_dir, args.results_save_dir, model, args.test_videos, args.inference_step)
        

    # finish time stamp
    finishTime = time.time()
    f_tm = time.localtime(finishTime)

    log_txt = 'FINISHED AT : \t' + time.strftime('%Y-%m-%d %I:%M:%S %p \n', f_tm)
    save_log(log_txt, os.path.join(args.results_save_dir, 'log.txt')) # save log





### @@@ union def @@@ ###
# cal vedio frame
def time_to_idx(time, fps):
    t_segment = time.split(':')
    # idx = int(t_segment[0]) * 3600 * fps + int(t_segment[1]) * 60 * fps + int(t_segment[2]) 
    idx = (int(t_segment[0]) * 3600 * fps) + (int(t_segment[1]) * 60 * fps) + (int(t_segment[2]) * fps) + int(t_segment[3]) # [h, m, s, frame] 


    return idx

def idx_to_time(idx, fps) :
    time_s = idx // fps
    frame = idx % fps

    converted_time = str(datetime.timedelta(seconds=time_s))
    converted_time = converted_time + ':' + str(frame)

    return converted_time


# input|DataFrame = 'frame' 'time' truth' 'predict'
# calc FN, FP, TP, TN
# out|{} = FN, FP, TP, TN frame
def return_metric_frame(result_df) :
    IB_CLASS, OOB_CLASS = 0,1

    print(result_df)
    
    # FN    
    FN_df = result_df[(result_df['truth']==OOB_CLASS) & (result_df['predict']==IB_CLASS)]
    
    # FP
    FP_df = result_df[(result_df['truth']==IB_CLASS) & (result_df['predict']==OOB_CLASS)]

    # TN
    TN_df = result_df[(result_df['truth']==IB_CLASS) & (result_df['predict']==IB_CLASS)]
    
    # TP
    TP_df = result_df[(result_df['truth']==OOB_CLASS) & (result_df['predict']==OOB_CLASS)]

    return {
        'FN_df' : FN_df,
        'FP_df' : FP_df,
        'TN_df' : TN_df,
        'TP_df' : TP_df,
    }


# save video frame from frame_list | it will be saved in {save_path}/{video_name}-{frame_idx}.jpg
def save_video_frame(video_path, frame_list, save_path, video_name) :
    video = cv2.VideoCapture(video_path)
    
    print('TARGET VIDEO_PATH : ', video_path)
    print('TARGET FRAME : ', frame_list)

    for frame_idx in tqdm(frame_list, desc='Saving Frame From {} ... '.format(video_path)) :
        video.set(1, frame_idx) # frame setting
        _, img = video.read() # read frame

        cv2.imwrite(os.path.join(save_path, '{}-{:010d}.jpg'.format(video_name, frame_idx)), img)
    
    video.release()
    print('======> DONE.')

# calc OOB_false Metric
def calc_OOB_metric(FN_cnt, FP_cnt, TN_cnt, TP_cnt, TOTAL_cnt) :
    OOB_metric = -1

    try : # zero devision except
        OOB_metric = (TP_cnt - FP_cnt) / (FP_cnt + TP_cnt + FN_cnt) # positie = OOB
    except :
        OOB_metric = -1

    return OOB_metric


# check results for binary metric
def calc_confusion_matrix(gts, preds):
    IB_CLASS, OOB_CLASS = [0, 1]
    
    classification_report_result = classification_report(gts, preds, labels=[IB_CLASS, OOB_CLASS], target_names=['IB', 'OOB'], zero_division=0)
    
    prec = precision_score(gts, preds, average='binary',pos_label=1, zero_division=0) # pos = [1]
    recall = recall_score(gts, preds, average='binary',pos_label=1, zero_division=0) # pos = [1]

    metric = pd.crosstab(pd.Series(gts), pd.Series(preds), rownames=['True'], colnames=['Predicted'], margins=True)
    
    saved_text = '{} \nprecision \t : \t {} \nrecall \t\t : \t {} \n\n{}'.format(classification_report_result, prec, recall, metric)

    return saved_text

# save log 
def save_log(log_txt, save_dir) :
    print('=========> SAVING LOG ... | {}'.format(save_dir))
    with open(save_dir, 'a') as f :
        f.write(log_txt)


# Annotation Sanity Check
def check_anno_sequence(anno_info:list): # annotation sequence에 이상없을 경우 = True, 이상 있을경우 = False

    if len(anno_info) == 1 :
        p_start, p_end = anno_info[0][0], anno_info[0][1]
        is_block_seq_ok = False

        if p_start < p_end : 
            is_block_seq_ok = True

        if not(is_block_seq_ok) :
            return False


    elif len(anno_info) >  1 :
        p_start, p_end = anno_info[0][0], anno_info[0][1]
        for start, end in anno_info[1:] :
            is_block_seq_ok = False
            is_total_seq_ok = False

            if start < end : 
                is_block_seq_ok = True

            if p_end < start : 
                is_total_seq_ok = True 

            if not(is_block_seq_ok) or not(is_total_seq_ok) :
                return False

            p_start, p_end = start, end

    return True

# check over frame and modify last annotation info
def check_anno_over_frame(anno_info:list, video_len): # over frame 존재하지 않을경우 = True, over frame 존재할 경우 = False  
    has_not_over_frame = False
    
    last_start, last_end = anno_info[-1]
    
    if last_end < video_len : 
        has_not_over_frame = True

    # modify
    if not(has_not_over_frame) :
        anno_info[-1] = [last_start, video_len-1]
        print('\t\t\t *** ANNO LAST FRAME END : {} | VIDEO_LEN : {}'.format(last_end, video_len))

    return has_not_over_frame, anno_info

def check_anno_int(anno_info:list): # anno int = True, anno Float = False
    is_int = True
    
    for start, end in anno_info : 
        if (not isinstance(start, int)) and (not isinstance(end, int)) :
            is_int = False
            break
    
    # modify
    if not(is_int) :
        for i, (start, end) in enumerate(anno_info) :
            anno_info[i] = [int(math.floor(start)), int(math.floor(end))]
            print('\t\t\t *** ANNO FLOAT FRAME : [{}, {}] | REFINED FRAME : {}'.format(start, end, anno_info[i]))

    return is_int, anno_info


# 불러온 annotation file 정보가 정확한지 체크 및 수정
def sanity_check_info_dict(info_dict) :
    # loop from total_videoset_cnt
    for i, (video_path_list, anno_info_list) in enumerate(zip(info_dict['video'], info_dict['anno']), 0): 
        hospital, surgery_type, surgeon, op_method, patient_idx, video_channel, video_slice = os.path.splitext(video_path_list[0])[0].split('_')
        videoset_name = '{}_{}'.format(op_method, patient_idx)

        for j, (video_path, anno_info) in enumerate(zip(video_path_list, anno_info_list), 0) :
            
            video_name = os.path.splitext(os.path.basename(video_path))[0] # only video name
            print('----- ANNOTATION CHECK => \t VIDEO\t {} \t-----'.format(video_name))
            print(info_dict['anno'][i][j])
            
            
            ##### video info and ####
            # open video cap for parse frame
            video = cv2.VideoCapture(video_path)
            video_fps = video.get(cv2.CAP_PROP_FPS)
            video_len = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            video.release()
            del video
        
            # open VideoReader
            '''
            with open(video_path, 'rb') as f :
                # open VideoReader
                video = VideoReader(f, ctx=cpu(0))
            
            # total frame
            video_len = len(video) 

            del video
            '''

            print('\tTarget video : {} | Total Frame : {} | Video FPS : {} '.format(video_name, video_len, video_fps))
            print('\tAnnotation Info : {}'.format(anno_info))


            ##### annotation sanity check #####
            ### check idx -> time
            if anno_info : # not empty list
                # init 
                over_ret = None
                int_ret = None
                val = None
                
                print('\t BEFORE ANNOTATION => {}\n'.format(anno_info))

                # seq check
                if not(check_anno_sequence(anno_info)) : 
                    print('ANNTATION SEQ ERROR | video : {} | anno {}'.format(video_path, anno_info))
                    exit(1)
                
                # last frmae annotation check
                over_ret, val = check_anno_over_frame(anno_info, video_len) # over frame이 아닐경우 True, over frame 일 경우 False
                anno_info = anno_info if over_ret else val # update anno_info | over frame일 경우 refined 된 val 값으로 update
                val = None # clean
                
                # check anntation frame is int
                int_ret, val = check_anno_int(anno_info) # int 일 경우 True, int가 아닐경우 False
                anno_info = anno_info if int_ret else val # update anno_info | frame이 int가 아닐경우 모두 int 로 refined 된 값으로 update

                print('\n\t AFTER ANNOTATION => {}'.format(anno_info))

                ##### update redefined annotation info #### 
                info_dict['anno'][i][j] = anno_info
                print(info_dict['anno'][i][j])

            else : # empty
                print(anno_info)
                print('=====> NO EVENT')
            
            print('')

    return info_dict # redefined info_dict





### union def ### 




### @@@ for robot def @@@ ###
# sanitiy check of test_assets per 1 video
def sanity_of_inference_assets(video_path, infernece_assets_path_list) :
    video = cv2.VideoCapture(video_path)
    video_len = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video.release()

    infernece_assets_len = 0

    for i, infernece_assets in tqdm(enumerate(infernece_assets_path_list), desc='Sanity Checking of Inferecnce assets... VIDEO_PATH : {} | INFERENCE ASSETS : {} '.format(video_path, infernece_assets_path_list)) :
        print(infernece_assets)
        with open(infernece_assets, 'rb') as file :
            infernece_assets_len += pickle.load(file).size()[0]
    
    assert video_len == infernece_assets_len, 'Original Video and Inference Assets is not matching in frame length\n VIDEO LEN : {} | INFERECE ASSETS LEN : {} | video_path : {} | assets_path : {}'.format(video_len, infernece_assets_len, video_path, infernece_assets_path_list)

    print('\n\n=============== \tSANITY RESULTS\t ============= \n\n')
    print('VIDEO FRAME COUNT {} | INFERENCE ASSETS TENSOR LEN : {}'.format(video_len ,infernece_assets_len))
    print('\n\n=============== \t\t ============= \n\n')


    return True


def test_video_for_robot(data_dir, anno_dir, infernece_assets_dir, results_save_dir, model, patient_list, inference_step) :
    
    ### base setting ###
    # val_videos = ['R_17', 'R_22', 'R_116', 'R_208', 'R_303']
    # val_videos = ['R_17']
    valset = patient_list

    video_ext = '.mp4'
    fps = 30

    tar_surgery = 'robot'

    ### ### ###

    # gettering information step
    info_dict = gettering_information_for_oob(data_dir, anno_dir, infernece_assets_dir, valset, mode='ROBOT')

    print('\n\n\t ==== RESULTS OF GETTERING INFORMATION==== ')
    print('\tSUCESS GETTERING VIDEO SET: ', len(info_dict['video']))
    print('\tSUCESS GETTERING ANNOTATION SET: ', len(info_dict['anno']))
    print('\tSUCESS GETTERING INFERENCE SET: ', len(info_dict['inference_assets']))
    print('\t=== === === ===\n\n')

    print('\n\n\t ==== RESULTS OF GETTERING INFORMATION==== ')
    print(info_dict['video'])
    print(info_dict['anno'])
    print(info_dict['inference_assets'])
    print('\t=== === === ===\n\n')

    #### sanity check and modify info_dict ###
    info_dict = sanity_check_info_dict(info_dict)

    print('\n\n\t ==== RESULTS OF GETTERING INFORMATION==== ')
    print('\tSUCESS GETTERING VIDEO SET: ', len(info_dict['video']))
    print('\tSUCESS GETTERING ANNOTATION SET: ', len(info_dict['anno']))
    print('\tSUCESS GETTERING INFERENCE SET: ', len(info_dict['inference_assets']))
    print('\t=== === === ===\n\n')

    print('\n\n\t ==== RESULTS OF GETTERING INFORMATION==== ')
    print(info_dict['video'])
    print(info_dict['anno'])
    print(info_dict['inference_assets'])
    print('\t=== === === ===\n\n')

    # inference step
    inference_for_robot(info_dict, model, results_save_dir, inference_step, fps=fps)


def gettering_information_for_oob(video_root_path, anno_root_path, inference_assets_root_path, video_set, mode) : # paring video from annotation info

    
    print('\n\n\n\t\t\t ### STARTING DEF [gettering_information_for_robot] ### \n\n')

    info_dict = {
        'video': [],
        'anno': [],
        'inference_assets' : []
    }

    all_video_path = []
    all_anno_path = []

    if mode == 'ROBOT' : 
        fps = 30
        
        video_ext_list = ['mp4']
        for ext in video_ext_list :
            all_video_path.extend(glob.glob(video_root_path +'/*.{}'.format(ext)))
        
        all_anno_path = glob.glob(anno_root_path + '/*.csv') # all annotation file list
    
    elif mode == 'LAPA' :
        fps = 60
        video_ext_list = ['mp4', 'MP4', 'mpg']
        
        for ext in video_ext_list :
            all_video_path.extend(glob.glob(video_root_path +'/*.{}'.format(ext)))
        
        all_anno_path = glob.glob(anno_root_path + '/*.json') # all annotation file list

        ##### except video file ######
        all_video_path.remove(os.path.join(video_root_path, '01_G_01_L_423_xx0_01.MP4'))
        all_anno_path.remove(os.path.join(anno_root_path, '01_G_01_L_423_xx0_01_OOB_16.json'))

    else :
        assert False, 'ONLY SUPPORT MODE [ROBOT, LAPA] | Input mode : {}'.format(mode)

    # dpath = os.path.join(video_root_path) # video_root path

    print('NUMBER OF TOTAL VIDEO FILE : ', len(all_video_path))
    print('NUMBER OF TOTAL ANNOTATION FILE : ', len(all_anno_path))
    print('')

    all_video_path_df = df(all_video_path, columns=['video_path'])
    all_anno_path_df = df(all_anno_path, columns=['anno_path'])

    print(all_video_path_df)
    print(all_anno_path_df)

    for video_no in video_set : # get target video
        # video_path_list = sorted([vfile for vfile in all_video_path if os.path.basename(vfile).startswith(video_no)])
        # anno_path_list = sorted([anno_file for anno_file in all_anno_path if os.path.basename(anno_file).startswith(video_no)])

        # find video_no in video_file
        video_path_df = all_video_path_df[all_video_path_df['video_path'].str.contains(video_no + '_')]

        # sort video_path_df for sync for video slice
        video_path_df = video_path_df.sort_values(by=['video_path'], axis=0, ascending=True)

        # init video and annotation paring path info
        pair_info = df(range(0,0), columns=['video_path', 'anno_path'])

        # video & annotation pairing
        for i in range(len(video_path_df)) : 
            video_file_name = os.path.splitext(os.path.basename(video_path_df['video_path'].iloc[i]))[0] # video_name with out extension
            anno_path_series = all_anno_path_df[all_anno_path_df['anno_path'].str.contains(video_file_name+'_OOB')]['anno_path'] # find annotation file based in video_file_name
            video_path_series = video_path_df.iloc[i]

            info = {
                'video_path':list(video_path_series)[0],
                'anno_path':np.nan if len(list(anno_path_series))==0 else list(anno_path_series)[0]
            }

            pair_info=pair_info.append(info, ignore_index=True)
        
        pair_info = pair_info.fillna('') # fill na -> ""
        
        print(pair_info)

        # df -> list 
        video_path_list = list(pair_info['video_path'])
        anno_path_list = list(pair_info['anno_path'])


        # inference assets base dir
        inference_assets_base_dir = os.path.join(inference_assets_root_path, video_no)
        
        
        print('\t ==== GETTERING INFO ====')
        print('\t VIDEO NO | ', video_no) 
        print('\t video_path', video_path_list) # target videos path
        print('\t anno_path', anno_path_list) # target annotaion path
        print('\t inference assets base path | ', inference_assets_base_dir)
        print('\t ', glob.glob(inference_assets_base_dir + '/*'))
        print('\t ==== ==== ==== ====\n')

        # it will be append to info_dict
        target_video_list = []
        target_anno_list = []
        target_inference_assets_list = []
        
        for target_video_path, target_anno_path in (zip(video_path_list, anno_path_list)) :
            # init
            temp_inference_assets_list = []
            # it will be append to temp_anno_list
            target_idx_list = []


            # consist infernce assets
            temp_inference_assets_list = glob.glob(os.path.join(inference_assets_base_dir, os.path.splitext(os.path.basename(target_video_path))[0], '*')) # [video1_1_0, video1_1_1, ...]

            # video and inference assets frame sanity check
            '''
            if not sanity_of_inference_assets(target_video_path, temp_inference_assets_list, slide_frame=30000) : 
                eixt(1)
            '''


            # only target_video_path 
            if target_anno_path != '' :
                anno_df = pd.read_csv(target_anno_path)
                anno_df = anno_df.dropna(axis=0) # 결측행 제거

                # time -> frame idx
                for i in range(len(anno_df)) :
                    t_start = anno_df.iloc[i]['start']
                    t_end = anno_df.iloc[i]['end']
                    
                    target_idx_list.append([time_to_idx(t_start, fps), time_to_idx(t_end, fps)]) # temp_idx_list = [[start, end], [start, end]..]
                
                print('-----'*3)
                print('target_video_path \t | ', target_video_path)
                print('inf_assets \t\t |', temp_inference_assets_list)
                print('anno_path \t\t | ', target_anno_path)
                print(anno_df)

            else : # no event
                print('-----'*3)
                print('target_video_path \t | ', target_video_path)
                print('inf_assets \t\t |', temp_inference_assets_list)
                print('anno_path \t\t | ', target_anno_path)
            
            # save gettering info
            target_video_list.append(target_video_path) # [video1_1, video_1_2, ...]
            target_anno_list.append(target_idx_list) # [temp_idx_list_1_1, temp_idx_list_1_2, ... ]
            target_inference_assets_list.append(temp_inference_assets_list) # [video1_1_0, video_1_1_1, video_1_1_2, ..]

        # info_dict['video'], info_dict['anno'] length is same as valset
        info_dict['video'].append(target_video_list) # [[video1_1, video1_2], [video2_1, video_2_2], ...]
        info_dict['anno'].append(target_anno_list) # [[temp_idx_list_1_1, temp_idx_list_1_2], [temp_idx_list_2_1, temp_idx_list_2_2,], ...]
        info_dict['inference_assets'].append(target_inference_assets_list) # [[[video1_1_0, video1_1_1, video1_1_2,..], [video1_2_0, ...]], ... ]
        
        print('\n\n')
        
    return info_dict
    


def inference_for_robot(info_dict, model, results_save_dir, inference_step, fps=30) : # project_name is only for use for title in total_metric_df.csv
    print('\n\n\n\t\t\t ### STARTING DEF [inference_for_robot] ### \n\n')

    # create results folder
    try :
        if not os.path.exists(results_save_dir) :
            os.makedirs(results_save_dir)
    except OSError :
        print('ERROR : Creating Directory, ' + results_save_dir)

    total_videoset_cnt = len(info_dict['video']) # total number of video set

    # init total metric df
    total_metric_df = pd.DataFrame(index=range(0, 0), columns=['Video_set', 'Video_name', 'FP', 'TP', 'FN', 'TN', 'TOTAL', 'GT_OOB', 'GT_IB', 'PREDICT_OOB', 'PREDICT_IB', 'GT_OOB_1FPS', 'GT_IB_1FPS', 'OOB_Metric']) # row cnt is same as checking vidoes length
    patient_total_metric_df = pd.DataFrame(index=range(0, 0), columns=['Patient', 'FP', 'TP', 'FN', 'TN', 'TOTAL', 'GT_OOB', 'GT_IB', 'PREDICT_OOB', 'PREDICT_IB', 'GT_OOB_1FPS', 'GT_IB_1FPS', 'OOB_Metric']) # row cnt is same as total_videoset_cnt

    # loop from total_videoset_cnt
    for i, (video_path_list, anno_info_list, infernece_assets_path_list) in enumerate(zip(info_dict['video'], info_dict['anno'], info_dict['inference_assets']), 1):
        
        hospital, surgery_type, surgeon, op_method, patient_idx, video_channel, video_slice = os.path.splitext(os.path.basename(video_path_list[0]))[0].split('_') # parsing videoset name
        videoset_name = '{}_{}'.format(op_method, patient_idx)

        # init for patient results_dict
        patient_video_list = []
        patient_frame_idx_list = []
        patient_time_list = []
        patient_gt_list = []
        patient_predict_list = []
        patient_truth_oob_count = 0
        patient_truth_ib_count = 0

        # create base folder for save results each video set
        each_videoset_result_dir = os.path.join(results_save_dir, videoset_name) # '~~~/results/R022' , '~~~/results/R011' ..
        try :
            if not os.path.exists(os.path.join(each_videoset_result_dir)) :
                os.makedirs(each_videoset_result_dir)
        except OSError :
            print('ERROR : Creating Directory, ' + each_videoset_result_dir)


        print('COUNT OF VIDEO SET | {} / {} \t\t ======>  VIDEO SET | {}'.format(i, total_videoset_cnt, videoset_name))
        print('NUMBER OF VIDEO : {} | NUMBER OF ANNOTATION INFO : {}'.format(len(video_path_list), len(anno_info_list)))
        print('NUMBER OF INFERNECE ASSETS {} \n==> ASSETS LIST : {}'.format(len(infernece_assets_path_list), infernece_assets_path_list))
        print('RESULTS SAVED AT \t\t\t ======>  {}'.format(each_videoset_result_dir))
        print('\n')
        
        # extract info for each video_path
        for video_path, anno_info, each_video_infernece_assets_path_list in zip(video_path_list, anno_info_list, infernece_assets_path_list) :
            
            video_name = os.path.splitext(os.path.basename(video_path))[0] # only video name

            # inference results saved folder for each video
            each_video_result_dir = os.path.join(each_videoset_result_dir, video_name) # '~~~/results/R022/R022_ch1_video_01' , '~~~/results/R022/R022_ch1_video_04' ..
            try :
                if not os.path.exists(os.path.join(each_video_result_dir)) :
                    os.makedirs(each_video_result_dir)
            except OSError :
                print('ERROR : Creating Directory, ' + each_video_result_dir)

            # FP Frame saved folder for each video
            fp_frame_saved_dir = os.path.join(each_video_result_dir, 'fp_frame') # '~~~/results/R022/R022_ch1_video_01/fp_frame'
            try :
                if not os.path.exists(os.path.join(fp_frame_saved_dir)) :
                    os.makedirs(fp_frame_saved_dir)
            except OSError :
                print('ERROR : Creating Directory, ' + fp_frame_saved_dir)
            
            # FN Frame saved folder for each video
            fn_frame_saved_dir = os.path.join(each_video_result_dir, 'fn_frame') # '~~~/results/R022/R022_ch1_video_01/fn_frame'
            try :
                if not os.path.exists(os.path.join(fn_frame_saved_dir)) :
                    os.makedirs(fn_frame_saved_dir)
            except OSError :
                print('ERROR : Creating Directory, ' + fn_frame_saved_dir)

            # open video cap, only check for frame count
            video = cv2.VideoCapture(video_path)
            video_len = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            video_fps = video.get(cv2.CAP_PROP_FPS)
            video.release()

            print('\tTarget video : {} | Total Frame : {} | Video FPS : {} '.format(video_name, video_len, video_fps))
            print('\tAnnotation Info : {}'.format(anno_info))

            ### check idx -> time
            if anno_info : # event 
                for start, end in anno_info :
                    print([idx_to_time(start, fps), idx_to_time(end, fps)])
            else : # no evnet
                print(anno_info)
                print('=====> NO EVENT')
                pass
                
            ###
            print('')

            ####  make truth list ####
            IB_CLASS, OOB_CLASS = [0, 1]
            truth_list = np.zeros(video_len, dtype='uint8') if IB_CLASS == 0 else np.ones(video_len, dtype='uint8')

            if anno_info : # only has event
                for start, end in anno_info :
                    truth_list[start:end+1] = OOB_CLASS # OOB Section

            truth_list = list(truth_list) # change to list

            truth_oob_count = truth_list.count(OOB_CLASS)
            truth_ib_count = truth_list.count(IB_CLASS)

            print('IB_CLASS = {} | OOB_CLASS = {}'.format(IB_CLASS, OOB_CLASS))
            print('TRUTH IB FRAME COUNT : ', video_len - truth_oob_count)
            print('TRUTH OOB FRAME COUNT : ', truth_oob_count)
            ### ### ###

            # init_variable
            gt_list = [] # ground truth
            predict_list = [] # predict
            frame_idx_list = [] # frmae info
            time_list = [] # frame to time

            FP_frame_cnt = 0
            FN_frame_cnt = 0
            TP_frame_cnt = 0
            TN_frame_cnt = 0
            TOTAL_frame_cnt = 0
            # frame_check_cnt = 0 # loop cnt
            OOB_metric = -1 # false metric

            print('----')
            print('EACH INFERENCE ASEETS PATH LENGTH')
            inference_assets_cnt = len(each_video_infernece_assets_path_list)
            print(inference_assets_cnt)

            # split gt_list per inference assets
            # init_variable
            SLIDE_FRAME = 30000
            inference_assets_start_end_frame_idx= [[start_idx*SLIDE_FRAME, (start_idx+1)*SLIDE_FRAME-1] for start_idx in range(inference_assets_cnt)]
            inference_assets_start_end_frame_idx[-1][1] = video_len - 1 # last frame of last pickle
            print(inference_assets_start_end_frame_idx)

            inference_frame_idx_list = [] # inference target frame [[pickle_0], [pickle_1], [pickle_2],...]

            for start, end in inference_assets_start_end_frame_idx :
                inference_frame_idx_list.append([idx for idx in range(start, end+1) if idx % inference_step == 0])
                

            BATCH_SIZE = 512

            temp_cnt = 0 ### dummy for test

            # getting infernce aseets 
            for infernece_assests_path, inference_frame_idx, (start_idx, end_idx) in zip(each_video_infernece_assets_path_list, inference_frame_idx_list, inference_assets_start_end_frame_idx) :
                print('\n\n=============== \tTARGET INFRENCE \t ============= \n\n')
                print('======> VIDEO PATH')
                print(video_path)

                print('======> ANNO INFO')
                print(anno_info)

                print('======> TRUTH_LIST LENGTH')
                print(len(truth_list))


                print('======> NUMBER OF INFERENCE ASSETS')
                print(len(each_video_infernece_assets_path_list))

                print('======> INFERENCE ASSETS PATH')
                print(infernece_assests_path)

                print('======> INFERENCE FRAME IDX [START, END]')
                print([start_idx, end_idx])

                print('======> INFERENCE FRAME IDX ')
                print(inference_frame_idx)

                print('')
                

                print('\n\n=============== \t\t ============= \n\n')

                # load inference assets from pickle
                print('===> LOADING... | \t {} '.format(infernece_assests_path))
                if True :
                    with open(infernece_assests_path, 'rb') as file :    
                        infernce_asset = pickle.load(file)
                        print('\t ===> DONE')
                else : # for test
                    infernce_asset = torch.Tensor(inference_assets_start_end_frame_idx[temp_cnt][-1], 3, 224, 224) # zero, float32
                    temp_cnt += 1
                print('\n\n=============== \t\t ============= \n\n')
                
                
                
                # infernceing 
                with torch.no_grad() :
                    # batch slice from infernece_frame_idx
                    start_pos = 0
                    end_pos = len(inference_frame_idx)
                    
                    FRAME_INDICES = []

                    # inferencing per batch
                    for idx in tqdm(range(start_pos, end_pos + BATCH_SIZE, BATCH_SIZE),  desc='Inferencing... \t ==> {} | {}'.format(video_name, infernece_assests_path)):
                        FRAME_INDICES = inference_frame_idx[start_pos:start_pos + BATCH_SIZE] # video frame idx
                        if FRAME_INDICES != []:
                            TORCH_INDIES = [f_idx-start_idx for f_idx in FRAME_INDICES] # convert to torch idx

                            # print(FRAME_INDICES)
                            # print(TORCH_INDIES)

                            # make batch input tensor
                            BATCH_INPUT_TENSOR = torch.index_select(infernce_asset, 0, torch.tensor(TORCH_INDIES, dtype=torch.int32))
                            
                            # print('= = = = = = = = = = = = = =')
                            # print(BATCH_INPUT_TENSOR.size())
                            # print(BATCH_INPUT_TENSOR)
                            
                            # upload on cuda
                            BATCH_INPUT_TENSOR = BATCH_INPUT_TENSOR.cuda()

                            # inferencing model
                            outputs = model(BATCH_INPUT_TENSOR)

                            # results of predict
                            # print('------- ==== output | predict ==== -------')
                            # print(outputs.cpu())
                            # print(outputs.cpu().size())

                            predict = torch.argmax(outputs.cpu(), 1) # predict 
                            predict = predict.tolist() # tensot -> list
                            # print(predict)

                            # save results
                            frame_idx_list+=FRAME_INDICES
                            predict_list+= list(predict)
                            
                            gt_list+=(lambda in_list, indices_list : [in_list[i] for i in indices_list])(truth_list, FRAME_INDICES) # get in_list elements from indices index 
                            time_list+=[idx_to_time(frame_idx, fps) for frame_idx in FRAME_INDICES] # FRAME INDICES -> time


                        start_pos = start_pos + BATCH_SIZE
                

                del infernce_asset # free memory

            print('\n\n=============== \t\t ============= \n\n')
            print('\t ===> INFERNECE DONE')
            print('\n\n=============== \t\t ============= \n\n')
            
            print(frame_idx_list)
            print(predict_list)
            print(gt_list)
            print(time_list)

            # saving inferece result
            result_dict = {
                'frame' : frame_idx_list,
                'time' : time_list,
                'truth' : gt_list,
                'predict' : predict_list
            }

            # append inference results for patient
            patient_video_list.append(video_name)
            patient_frame_idx_list.append(frame_idx_list)
            patient_time_list.append(time_list)
            patient_gt_list.append(gt_list)
            patient_predict_list.append(predict_list)
            patient_truth_oob_count+=truth_oob_count
            patient_truth_ib_count+=truth_ib_count

            # save for df
            inference_results_df = pd.DataFrame(result_dict)
        
            print('Result Saved at \t ====> ', each_video_result_dir)
            inference_results_df.to_csv(os.path.join(each_video_result_dir, 'Inference-{}.csv'.format(video_name)), mode="w")
            
            # calc FN, FP, TP, TN frame and TOTAL
            metric_frame = return_metric_frame(inference_results_df)

            FN_frame_cnt = len(metric_frame['FN_df'])
            FP_frame_cnt = len(metric_frame['FP_df'])
            TN_frame_cnt = len(metric_frame['TN_df'])
            TP_frame_cnt = len(metric_frame['TP_df'])
            TOTAL_frame_cnt = len(inference_results_df)

            print('\n\n=============== \tFN\t ============= \n\n')
            print(metric_frame['FN_df'])

            print('\n\n=============== \tFP\t ============= \n\n')
            print(metric_frame['FP_df'])
            

            print('\n\n=============== \tTN\t ============= \n\n')
            print(metric_frame['TN_df'])
            

            print('\n\n=============== \tTP\t ============= \n\n')
            print(metric_frame['TP_df'])
            

            print('\n\n=============== \tINFO\t ============= \n\n')
            print(FN_frame_cnt)
            print(FP_frame_cnt)
            print(TN_frame_cnt)
            print(TP_frame_cnt)
            print(TOTAL_frame_cnt)
            print(truth_oob_count)
            print(video_len - truth_oob_count)
            print('\n\n=============== \t\t ============= \n\n')
            
            
            ### saving FP TN frame
            # FP frame
            print('\n\n=============== \tSAVE FP frame \t ============= \n\n')
            save_video_frame(video_path, list(metric_frame['FP_df']['frame']), fp_frame_saved_dir, video_name)

            # FN frame
            print('\n\n=============== \tSAVE FN frame \t ============= \n\n')
            save_video_frame(video_path, list(metric_frame['FN_df']['frame']), fn_frame_saved_dir, video_name)

            # OOB_Metric
            OOB_metric = calc_OOB_metric(FN_frame_cnt, FP_frame_cnt, TN_frame_cnt, TP_frame_cnt, TOTAL_frame_cnt)

            # saving FN FP TP TN Metric
            results_metric = {
                'Video_set' : [videoset_name],
                'Video_name' : [video_name],
                'FP' : [FP_frame_cnt],
                'TP' : [TP_frame_cnt],
                'FN' : [FN_frame_cnt],
                'TN' : [TN_frame_cnt],
                'TOTAL' : [TOTAL_frame_cnt],
                'GT_OOB' : [gt_list.count(OOB_CLASS)],
                'GT_IB' : [gt_list.count(IB_CLASS)],
                'PREDICT_OOB' : [predict_list.count(OOB_CLASS)],
                'PREDICT_IB' : [predict_list.count(IB_CLASS)],
                'GT_OOB_1FPS' : [truth_oob_count],
                'GT_IB_1FPS' : [video_len-truth_oob_count],
                'OOB_Metric' : [OOB_metric]
            }

            # each metric per video
            result_metric_df = pd.DataFrame(results_metric)
            
            # save
            print('Metric Saved at \t ====> ', each_video_result_dir)
            result_metric_df.to_csv(os.path.join(each_video_result_dir, 'OOB_Metric-{}.csv'.format(video_name)), mode="w")

            # append metric
            # columns=['Video_set', 'Video_name', 'FP', 'TP', 'FN', 'TN', 'TOTAL', 'GT_OOB', 'GT_IB', 'PREDICT_OOB', 'PREDICT_IB', 'GT_OOB_1FPS', 'GT_IB_1FPS', 'OOB_Metric'])           
            # total_metric_df = total_metric_df.append(result_metric_df)
            total_metric_df = pd.concat([total_metric_df, result_metric_df], ignore_index=True) # shoul shink columns

            print('')
            print(total_metric_df)
            total_metric_df.to_csv(os.path.join(results_save_dir, 'Video_Total_metric-{}.csv'.format(os.path.basename(results_save_dir))), mode="w") # save on project direc

            # saving plot
            fig = plt.figure(figsize=(16,8))

            # plt.hold()
            plt.scatter(np.array(frame_idx_list), np.array(gt_list), color='blue', marker='o', s=20, label='Truth') # ground truth
            plt.scatter(np.array(frame_idx_list), np.array(predict_list), color='red', marker='o', s=5, label='Predict') # predict

            plt.title('Inference Results By per {} Frame | Video : {} | Results : {} '.format(inference_step, video_name, os.path.basename(results_save_dir)));
            plt.suptitle('OOB_CLASS [{}] | IB_CLASS [{}] | FP : {} | TP : {} | FN : {} | TN : {} | TOTAL : {} | OOB_Metric : {} '.format(OOB_CLASS, IB_CLASS, FP_frame_cnt, TP_frame_cnt, FN_frame_cnt, TN_frame_cnt, TOTAL_frame_cnt, OOB_metric));
            plt.ylabel('class'); plt.xlabel('frame');
            plt.legend(loc='center right');

            plt.savefig(os.path.join(each_video_result_dir, 'plot_{}.png'.format(video_name)));

            # save confusion matrix
            # def calc_confusion_matrix(inference_results_df['truth'], inference_results_df['predict'])
            saved_text = calc_confusion_matrix(gt_list, predict_list)
            saved_text += '\n\nFP\t\tTP\t\tFN\t\tTN\t\tTOTAL\n'
            saved_text += '{}\t\t{}\t\t{}\t\t{}\t\t{}\n\n'.format(FP_frame_cnt, TP_frame_cnt, FN_frame_cnt, TN_frame_cnt, TOTAL_frame_cnt)
            saved_text += 'OOB_metric : {:.4f}'.format(OOB_metric)

            with open(os.path.join(each_video_result_dir, 'Metric-{}.txt'.format(video_name)), 'w') as f :
                f.write(saved_text)

            print('\n\n-------------- \t\t -------------- \n\n')

        print('\n\n=============== \t\t PATIENT PROCESSING \t\t ============= \n\n')
        
        #####  calc for patient #### 
        patient_FN_frame_cnt = 0
        patient_FP_frame_cnt = 0
        patient_TN_frame_cnt = 0
        patient_TP_frame_cnt = 0
        patient_TOTAL_frame_cnt = 0

        # video_name	frame	consensus_frame	time	consensus_time	truth	predict
        patient_inference_results_df = df(range(0,0), columns=['video_name', 'frame', 'consensus_frame', 'time', 'consensus_time', 'truth', 'predict'])

        # make results for patient
        for patient_video, patient_frame_idx, patient_time, patient_gt, patient_predict in zip(patient_video_list, patient_frame_idx_list, patient_time_list, patient_gt_list, patient_predict_list) :
            # saving inferece result per patient
            temp_patient_result_dict = {
                'video_name' : [patient_video]*len(patient_gt),
                'frame' : patient_frame_idx,
                'time' : patient_time,
                'truth' : patient_gt,
                'predict' : patient_predict
            }

            # re-index time and frame_idx
            patient_inference_results_df = pd.concat([patient_inference_results_df, df(temp_patient_result_dict)], ignore_index=True)

        # re-index consensus_frame
        patient_inference_results_df['consensus_frame'] = [frame * inference_step for frame in range(len(patient_inference_results_df))]
        # calc consensus time
        patient_inference_results_df['consensus_time'] = patient_inference_results_df.apply(lambda x : idx_to_time(x['consensus_frame'], fps), axis=1)

        # save
        print('Patient Result Saved at \t ====> ', each_videoset_result_dir)
        patient_inference_results_df.to_csv(os.path.join(each_videoset_result_dir, 'Inference-{}.csv'.format(videoset_name)), mode="w")

        # each metric per patient
        result_metric_df_per_patient = return_metric_frame(patient_inference_results_df)

        patient_FN_frame_cnt = len(result_metric_df_per_patient['FN_df'])
        patient_FP_frame_cnt = len(result_metric_df_per_patient['FP_df'])
        patient_TN_frame_cnt = len(result_metric_df_per_patient['TN_df'])
        patient_TP_frame_cnt = len(result_metric_df_per_patient['TP_df'])
        patient_TOTAL_frame_cnt = len(patient_inference_results_df)

        print('\n\n=============== \tFN\t ============= \n\n')
        print(result_metric_df_per_patient['FN_df'])

        print('\n\n=============== \tFP\t ============= \n\n')
        print(result_metric_df_per_patient['FP_df'])
        

        print('\n\n=============== \tTN\t ============= \n\n')
        print(result_metric_df_per_patient['TN_df'])
        

        print('\n\n=============== \tTP\t ============= \n\n')
        print(result_metric_df_per_patient['TP_df'])
        

        print('\n\n=============== \tINFO\t ============= \n\n')
        print(patient_FN_frame_cnt)
        print(patient_FP_frame_cnt)
        print(patient_TN_frame_cnt)
        print(patient_TP_frame_cnt)
        print(patient_TOTAL_frame_cnt)
        print('\n\n=============== \t\t ============= \n\n')

        print('Pateint Result Saved at \t ====> ', each_videoset_result_dir)

        # OOB_Metric
        patient_OOB_metric = calc_OOB_metric(patient_FN_frame_cnt, patient_FP_frame_cnt, patient_TN_frame_cnt, patient_TP_frame_cnt, patient_TOTAL_frame_cnt)

        # saving FN FP TP TN Metric
        patient_results_metric = {
        'Patient' : [videoset_name],
        'FP' : [patient_FP_frame_cnt],
        'TP' : [patient_TP_frame_cnt],
        'FN' : [patient_FN_frame_cnt],
        'TN' : [patient_TN_frame_cnt],
        'TOTAL' : [patient_TOTAL_frame_cnt],
        'GT_OOB' : [patient_TP_frame_cnt + patient_FN_frame_cnt],
        'GT_IB' : [patient_FP_frame_cnt + patient_TN_frame_cnt],
        'PREDICT_OOB' : [patient_FP_frame_cnt + patient_TP_frame_cnt],
        'PREDICT_IB' : [patient_FN_frame_cnt + patient_TN_frame_cnt],
        'GT_OOB_1FPS' : [patient_truth_oob_count],
        'GT_IB_1FPS' : [patient_truth_ib_count],
        'OOB_Metric' : [patient_OOB_metric]
        }

        # each metric per patient
        patient_result_metric_df = pd.DataFrame(patient_results_metric)

        print('Patient Metric Saved at \t ====> ', each_videoset_result_dir)
        patient_result_metric_df.to_csv(os.path.join(each_videoset_result_dir, 'OOB_Metric-{}.csv'.format(videoset_name)), mode="w")

        # append to total metric per patient
        patient_total_metric_df = pd.concat([patient_total_metric_df, patient_result_metric_df], ignore_index=True)

        # columns=['Patient', 'FP', 'TP', 'FN', 'TN', 'TOTAL', 'GT_OOB', 'GT_IB', 'PREDICT_OOB', 'PREDICT_IB', 'GT_OOB_1FPS', 'GT_IB_1FPS', 'OOB_Metric'])
        print('')
        print(patient_total_metric_df)
        patient_total_metric_df.to_csv(os.path.join(results_save_dir, 'Patient_Total_metric-{}.csv'.format(os.path.basename(results_save_dir))), mode="w") # save on project direc
    
    print('\n\n=============== \t\t ============= \t\t ============= \n\n')

    
if __name__ == "__main__":
    ###  base setting for model testing ### 
    os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'

    test_video()