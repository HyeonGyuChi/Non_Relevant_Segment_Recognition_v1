import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame as df

from itertools import groupby

import argparse
import json
import os

import math
import copy

from glob import glob
from natsort import natsorted

from skimage.morphology import binary_erosion, binary_dilation, opening, closing, erosion, dilation


EXCEPTION_NUM = -100 # full TN

SUPPORT_MODEL = ['vgg11', 'vgg13', 'vgg16', 'vgg19', 'vgg11_bn', 'vgg13_bn', 'vgg16_bn', 'vgg19_bn', 'resnet18', 'resnet34', 'resnet50', 'wide_resnet50_2', 'resnext50_32x4d',
                    'mobilenet_v2', 'mobilenet_v3_small', 'mobilenet_v3_large', 'squeezenet1_0', 'squeezenet1_1',
                    'efficientnet_b0', 'efficientnet_b1', 'efficientnet_b2', 'efficientnet_b3', 'efficientnet_b4', 'efficientnet_b5', 'efficientnet_b6', 'efficientnet_b7',
					'median-1', 'median-3', 'median-5', 'median-7', 'median-9', 'median-11', 'median-15', 'median-21', 'median-29', 'median-35', 'median-45', 'median-59',
					'morphology-1', 'morphology-3', 'morphology-6',
					'morphology-1-median-5', 'morphology-1-median-9', 'morphology-1-median-15', 'morphology-1-median-21', 'morphology-1-median-29', 'morphology-1-median-35', 'morphology-1-median-45', 'morphology-1-median-59',
					'morphology-3-median-5', 'morphology-3-median-9', 'morphology-3-median-15', 'morphology-3-median-21', 'morphology-3-median-29', 'morphology-3-median-35', 'morphology-3-median-45', 'morphology-3-median-59',
					'morphology-6-median-5', 'morphology-6-median-9', 'morphology-6-median-15', 'morphology-6-median-21', 'morphology-6-median-29', 'morphology-6-median-35', 'morphology-6-median-45', 'morphology-6-median-59',
					'median-5-morphology-1', 'median-9-morphology-1', 'median-15-morphology-1', 'median-21-morphology-1', 'median-29-morphology-1', 'median-35-morphology-1', 'median-45-morphology-1', 'median-59-morphology-1',
					'median-5-morphology-3', 'median-9-morphology-3', 'median-15-morphology-3', 'median-21-morphology-3', 'median-29-morphology-3', 'median-35-morphology-3', 'median-45-morphology-3', 'median-59-morphology-3',
					'median-5-morphology-6', 'median-9-morphology-6', 'median-15-morphology-6', 'median-21-morphology-6', 'median-29-morphology-6', 'median-35-morphology-6', 'median-45-morphology-6', 'median-59-morphology-6',
					'consistency-2-2', 'consistency-2-4', 'consistency-2-6',
					'consistency-6-2', 'consistency-6-4', 'consistency-6-6',
					'consistency-12-2', 'consistency-12-4', 'consistency-12-6',
					'opening-1-closing-1', 'opening-1-closing-2', 'opening-1-closing-3',
					'opening-2-closing-1', 'opening-2-closing-2', 'opening-2-closing-3',
					'opening-3-closing-1', 'opening-3-closing-2', 'opening-3-closing-3', 'opening-3-closing-6', 'opening-3-closing-9', 'opening-3-closing-12', 'opening-3-closing-15', 'opening-3-closing-18',
					'opening-6-closing-3', 'opening-6-closing-6', 'opening-6-closing-9', 'opening-6-closing-12', 'opening-6-closing-15', 'opening-6-closing-18',
					'opening-9-closing-3', 'opening-9-closing-6', 'opening-9-closing-9', 'opening-9-closing-12', 'opening-9-closing-15', 'opening-9-closing-18',
					'opening-12-closing-3', 'opening-12-closing-6', 'opening-12-closing-9', 'opening-12-closing-12', 'opening-12-closing-15', 'opening-12-closing-18',
					'opening-15-closing-3', 'opening-15-closing-6', 'opening-15-closing-9', 'opening-15-closing-12', 'opening-15-closing-15', 'opening-15-closing-18',
					'opening-18-closing-3', 'opening-18-closing-6', 'opening-18-closing-9', 'opening-18-closing-12', 'opening-18-closing-15', 'opening-18-closing-18']


parser = argparse.ArgumentParser()

parser.add_argument('--title_name', type=str, help='plot title, and save file name')

parser.add_argument('--sub_title_name', type=str, help='sub plot title, and save file name')

parser.add_argument('--GT_path', type=str, help='GT model_inference assets path')

# 21.06.04 HG ?????? - Add supported model [VGG Family]
parser.add_argument('--model_name', type=str, nargs='+',
                    choices=SUPPORT_MODEL, help='trained backborn model, it will be yticks name')

parser.add_argument('--model_infernce_path', type=str, nargs='+', help='model_inference_assets path. this order should be pair with --model_name. if not, results is not unpair.')

parser.add_argument('--results_save_dir', type=str, help='inference results save path')

# 21.06.04 HG ?????? - Add parser Variable for set Variable [Inference Step(==it should be synk with original Experimetal Setting), Window Size, Window num(==Overlap window number)]
parser.add_argument('--INFERENCE_STEP', type=int, help='Original Experimental Setting in Infernce Step (You should be set as same as test.py --inference_step)')
parser.add_argument('--WINDOW_SIZE', type=int, help='How many frame count in One section')
parser.add_argument('--OVERLAP_SECTION_NUM', type=int, help='Overap Count for Section number inference results save path, 1 is non-overlap')

parser.add_argument('--filter', type=str, nargs='+', choices=['median', 'opening', 'closing'], help='only predict results will be apply')

parser.add_argument('--kernel_size', type=int, default=1, nargs='+', choices=[1,2,3,4,5,6,7,9,11,12,13,15,17,18,19,21,35,29,45,59], help='filter kernel size')
parser.add_argument('--ignore_kernel_size', type=int, default=0, choices=[2,4,6], help='ignore filter kernel size [consistency]')

args, _ = parser.parse_known_args()

def encode_list(s_list): # run-length encoding from list
    return [[len(list(group)), key] for key, group in groupby(s_list)] # [[length, value], [length, value]...]


# 30fps = 30's predict frame in 1 sec
# 6fps = 6's predict frame in 1 sec
# 1fps = 1's predict frame in 1 sec
# 0.5 fps = 2's predict frame in 1 sec
def time_to_filtersize(filter_sec, fps):
	'''
	filter_time = float (second)
	fps = float
	'''
	filter_size = EXCEPTION_NUM
	
	filter_size = filter_sec * fps

	return int(filter_size)
	

def medfilter (x, k):
	"""Apply a length-k median filter to a 1D array x.
	Boundaries are extended by repeating endpoints.
	"""
	assert k % 2 == 1, "Median filter length must be odd."
	assert x.ndim == 1, "Input must be one-dimensional."

	k2 = (k - 1) // 2
	y = np.zeros ((len (x), k), dtype=x.dtype)

	print('==> prepare')
	print(y)

	y[:,k2] = x
	
	print('\n==> arrange')
	print(y)
	for i in range (k2):
		j = k2 - i
		y[j:,i] = x[:-j]
		y[:j,i] = x[0]
		y[:-j,-(i+1)] = x[j:]
		y[-j:,-(i+1)] = x[-1]

	print('\n==> margin padding')
	print(y)

	return np.median (y, axis=1)


def meanfilter (x, k):
	"""Apply a length-k mean filter to a 1D array x.
	Boundaries are extended by repeating endpoints.
	"""
	assert k % 2 == 1, "Mean filter length must be odd."
	assert x.ndim == 1, "Input must be one-dimensional."

	k2 = (k - 1) // 2
	y = np.zeros ((len (x), k), dtype=x.dtype)
	y[:,k2] = x
	for i in range (k2):
		j = k2 - i
		y[j:,i] = x[:-j]
		y[:j,i] = x[0]
		y[:-j,-(i+1)] = x[j:]
		y[-j:,-(i+1)] = x[-1]
	return np.mean (y, axis=1)


def consistencyfilter(x, k, ignore_k=0):
	run_length = encode_list(x)
	print(run_length)

	total_len = 0

	IB_CLASS, OOB_CLASS  = (0,1)
	CONVERTED_FLAG = OOB_CLASS - IB_CLASS

	convert_run_length = run_length.copy()

	# 1. convert OOB chunk under count of k to IB chunk
	for idx, (length, group) in enumerate(run_length) : 
		if group == OOB_CLASS : # if OOB chunk,
			if length <= k : # is unber count of k
				convert_run_length[idx] = [length, IB_CLASS]

		total_len += length 

	# 2. check converted chunk
	converted_chunk = np.array(run_length) - np.array(convert_run_length) # if converted [0 1], not converted [0 0]
	print(converted_chunk)

	# 3. unconverted (redefine ignore block) - if converted chunk is in zig-zag, ignore filtering
	for idx, (_, flags) in enumerate(converted_chunk) : 
		if flags == CONVERTED_FLAG:
			pre_length, pre_group = (ignore_k + 10, ignore_k + 10)
			post_length, post_group = (ignore_k + 10, ignore_k + 10)

			if idx == 0 : # first chunk of sequence
				post_length, post_group = run_length[idx + 1]

			elif idx == len(converted_chunk) : # last chunk of sequence
				pre_length, pre_group = run_length[idx - 1]

			else : 
				pre_length, pre_group = run_length[idx - 1]
				post_length, post_group = run_length[idx + 1]

			# check zig-zag if ignore_k = 3, [0, 2] / [k, CONVERTED(OOB CLASS -> IB CLASS)] / [0, 9] ==> [0, 2] / [k, UN CONVERTED (IB CLASS -> OOB CLASS)] / [0, 9]
			if (pre_length <= ignore_k) or  (post_length <= ignore_k):
				target_chunk_length, target_chunk_group = run_length[idx]
				convert_run_length[idx] = [target_chunk_length, target_chunk_group]

	final_results = decode_list(convert_run_length)
	final_results = np.array(final_results)
	
	return final_results

	


def decode_list(run_length): # run_length -> [0,1,1,1,1,0 ...]
	decode_list = []

	for length, group in run_length : 
		decode_list += [group] * length
	
	# print(decode_list)

	return decode_list
	
	

def apply_filter(assets, filter_type:str, kernel_size, ignore_kernel_size) : # input = numpy, kernel should be odd

	assert filter_type in ['median', 'opening', 'closing', 'consistency'], "NOT SUPPORT FILTER"

	print('\n\n\t\t ===== APPLYING FILTER | type : {} | kernel_size = {} | ignore_kernel_size = {} =====\n\n'.format(filter_type, kernel_size, ignore_kernel_size))

	results = -1 # reutrn
	
	if filter_type == 'median' :
		results=medfilter(assets, kernel_size) # 1D numpy
		results=results.astype(assets.dtype) # convert to original dtype

		print('\t\t==> original \t')
		print(assets)
		print('\t\t==> results \t')
		print(results)

	elif filter_type == 'mean' :
		pass
	
	elif filter_type == 'opening' :
		results = openingfilter(assets, kernel_size) # 1D numpy
		results = results.astype(assets.dtype) # convert to original dtype

	elif filter_type == 'closing' :
		results = closingfilter(assets, kernel_size) # 1D numpy
		results = results.astype(assets.dtype) # convert to original dtype

	elif filter_type == 'consistency' :
		results = consistencyfilter(assets, kernel_size, ignore_kernel_size) # 1D numpy # add ignore_kernel_size
		results = results.astype(assets.dtype) # convert to original dtype

	return results # numpy




def openingfilter(x, iter_count): # x:1d-numpy, count : 1*2 = 2 frame, 2*2 = 4 frame, 2*3 = 6 frame 
	out = np.copy(x)

	# opening
	for i in range(iter_count):	
		out = erosion(out)
	
	for j in range(iter_count):
		out = dilation(out)

	return out

def closingfilter(x, iter_count): # x:1d-numpy, count : 1*2 = 2 frame, 2*2 = 4 frame, 2*3 = 6 frame 
	out = np.copy(x)

	# closing
	for i in range(iter_count):	
		out = dilation(out)
	
	for j in range(iter_count):
		out = erosion(out)

	return out



def aggregation_post_processing_results(total_eval_root_path):
	patient_eval_path_list = glob(os.path.join(total_eval_root_path, '*'))
	patient_eval_path_list = natsorted(patient_eval_path_list)

	aggregation_CR_path = os.path.join(total_eval_root_path, 'aggregation_CR.csv')
	aggregation_OR_path = os.path.join(total_eval_root_path, 'aggregation_OR.csv')

	
	aggregation_CR_df = pd.DataFrame()
	aggregation_OR_df = pd.DataFrame()
	
	# parsing only CR, OR
	for patient_eval_path in patient_eval_path_list:
		
		if not os.path.isdir(patient_eval_path):
			continue

		patient_name = os.path.basename(patient_eval_path)

		print(patient_name)
		evaluaion_df_path = os.path.join(patient_eval_path, 'mobilenet_v3_large-InferenceStep_30-{}-Evaluation.csv'.format(patient_name))

		evaluation_df = pd.read_csv(evaluaion_df_path)
		print(evaluation_df)

		model = evaluation_df['Model']
		CR = evaluation_df['CONFIDENCE_metric']
		OR = evaluation_df['OVER_estimation']
		
		# append CR,OR in aggregation df
		aggregation_CR_df['Model'] = model.values
		aggregation_CR_df[patient_name] = CR.values

		aggregation_OR_df['Model'] = model.values
		aggregation_OR_df[patient_name] = OR.values

		
	print(aggregation_CR_df)
	print(aggregation_OR_df)

	# save aggregation df
	aggregation_CR_df.to_csv(aggregation_CR_path, mode='w')
	aggregation_OR_df.to_csv(aggregation_OR_path, mode='w')



		

# for text on bar
def present_text(ax, bar, text, color='black'):
	for rect in bar:
		posx = rect.get_x()
		posy = rect.get_y() - rect.get_height()*0.1
		print(posx, posy)
		ax.text(posx, posy, text, color=color, rotation=0, ha='left', va='bottom')

def present_text_for_section(ax, bar, pos_x, text, color='black'):
	for rect in bar:
		posx = pos_x
		posy = rect.get_y() + rect.get_height()*1.2
		print(posx, posy)
		ax.text(posx, posy, text, rotation=0, color=color, ha='left', va='top', fontsize=8)

def present_text_for_sub_section(ax, bar, pos_x, text): # not used
	for rect in bar:
		posx = pos_x
		posy = rect.get_y() + rect.get_height()*1.0
		print(posx, posy)
		print('------presesnt')
		ax.text(posx, posy, text, rotation=0, ha='left', va='top', fontsize=8)

# calc OOB_Metric
# input|DataFrame = 'GT' 'model A' model B' ..
# calc FN, FP, TP, TN
# out|{} = FN, FP, TP, TN frame
def return_metric_frame(result_df, GT_col_name, predict_col_name) :
	IB_CLASS, OOB_CLASS = 0,1

	print(result_df)
    
    # FN    
	FN_df = result_df[(result_df[GT_col_name]==OOB_CLASS) & (result_df[predict_col_name]==IB_CLASS)]
    
    # FP
	FP_df = result_df[(result_df[GT_col_name]==IB_CLASS) & (result_df[predict_col_name]==OOB_CLASS)]

    # TN
	TN_df = result_df[(result_df[GT_col_name]==IB_CLASS) & (result_df[predict_col_name]==IB_CLASS)]
    
    # TP
	TP_df = result_df[(result_df[GT_col_name]==OOB_CLASS) & (result_df[predict_col_name]==OOB_CLASS)]
	
	print('RESULT DF')
	print(result_df)
	print('FN',len(FN_df), 'FP',len(FP_df), 'TN',len(TN_df), 'TP', len(TP_df))	


	print(FN_df)
	print(FP_df)
	print(TN_df)
	print(TP_df)
	
	return {
		'FN_df' : FN_df,
		'FP_df' : FP_df,
		'TN_df' : TN_df,
		'TP_df' : TP_df,
		}


# calc OOB Evaluation Metric
def calc_OOB_Evaluation_metric(FN_cnt, FP_cnt, TN_cnt, TP_cnt) :
	base_denominator = FP_cnt + TP_cnt + FN_cnt	
	# init
	EVAL_metric = {
		'CONFIDENCE_metric' : EXCEPTION_NUM,
		'correspondence' : EXCEPTION_NUM,
		'UN_correspondence' : EXCEPTION_NUM,
		'OVER_estimation' : EXCEPTION_NUM,
		'UNDER_estimtation' : EXCEPTION_NUM,
		'FN' : FN_cnt,
		'FP' : FP_cnt,
		'TN' : TN_cnt,
		'TP' : TP_cnt,
		'TOTAL' : FN_cnt + FP_cnt + TN_cnt + TP_cnt
	}


	if base_denominator > 0 : # zero devision except check, FN == full
		EVAL_metric['CONFIDENCE_metric'] = (TP_cnt - FP_cnt) / base_denominator
		EVAL_metric['correspondence'] = TP_cnt /  base_denominator
		EVAL_metric['UN_correspondence'] = (FP_cnt + FN_cnt) /  base_denominator
		EVAL_metric['OVER_estimation'] = FP_cnt / base_denominator
		EVAL_metric['UNDER_estimtation'] = FN_cnt / base_denominator
	
	return EVAL_metric


def filter_parity_check(filter_list, filter_kernel_size_list):

	parity_check = False

	if len(filter_list) == len(filter_kernel_size_list):
			parity_check = True
	else :
		print('NOT PAIR OF ARGS LENGTH | filter : {}, kernel_size : {}'.format(filter_list, filter_kernel_size_list))


	return parity_check
	

def main():

	print(json.dumps(args.__dict__, indent=2))	

	# args parity check (filter)
	# assert filter_parity_check(args.filter, args.kernel_size) , "filter's args are Out of Rule [Please check filter's args rule]"

	print(args.filter)
	print(args.kernel_size)

	# make results dir
	os.makedirs(args.results_save_dir, exist_ok=True)

	#### 1. bar plot?????? ????????? ????????? ??????
	IB, OOB = (0,1) # class index
	
	### for plt variable, it should be pair sink
	label_names = ['IB', 'OOB']
	colors = ['cadetblue', 'orange']
	height = 0.5 # bar chart thic

	## Data prepare
	print(args.GT_path)
	print('------')
	GT_df = pd.read_csv(args.GT_path)
	frame_label = list(GT_df['consensus_frame']) # sync xticks label from GT // video??? : frame , patient ??? : consensus_frame
	time_label = list(GT_df['consensus_time']) # sync xticks label from GT // video??? : time , patient ??? : consensus_time

	yticks = ['GT'] # y??? names # ????????????
	yticks += args.model_name

	predict_data = {'GT': GT_df['truth']} #### origin
	
	# pairwise read
	for y_name, inf_path in zip(args.model_name, args.model_infernce_path) :
		p_data = pd.read_csv(inf_path)['predict']
		
		
		print('BEFORE')
		print(p_data)

		# filter processing		
		if args.filter is not None :
			for filter_name, filter_size in zip(args.filter, args.kernel_size) : # filter sequence
				p_data = apply_filter(p_data.to_numpy(), filter_name, filter_size, args.ignore_kernel_size) # 1D numpy, 'filter', kernel_size, ignore_filter_size
				p_data = pd.Series(p_data)

		print('AFTER')
		print(p_data)
		predict_data[y_name] = p_data

		# save post processing df
		'''
		p_df = pd.read_csv(inf_path)
		p_df['predict'] = p_data
		p_df.to_csv(os.path.join(args.results_save_dir, '{}-{}-Inference-post.csv'.format(args.title_name, args.sub_title_name)), mode='w') # mode='w', 'a' 
		'''

	print(predict_data)
	
	'''
	predict_data = {'GT': [1, 1, 1, 0, 0, 1, 1, 1], # 0??? ~ 2??? frame , 5??? ~ 7??? frame
	        'Model A': [0, 0, 1, 1, 0, 0, 1, 1], # 2??? ~ 3??? frame
			'Model B': [1, 0, 1, 1, 1, 0, 1, 0] # 0??? ~ 0??? frame, 2??? ~ 4??? frame, 6??? ~ 6??? frame
			}
	'''

	## find High OOB False Section
	

	#### Data Processing

	# run-length encoding
	encode_data = {}
	for y_name in yticks :
		encode_data[y_name] = df(data=encode_list(predict_data[y_name]), columns=[y_name, 'class']) # [length, value]

	print(encode_data)
	
	# arrange data
	runlength_df = df(range(0,0)) # empty df
	for y_name in yticks :
		runlength_df = runlength_df.append(encode_data[y_name])

	# Nan -> 0, convert to int
	runlength_df = runlength_df.fillna(0).astype(int)
	print(runlength_df)	

	'''
	runlength_df = df([[3,0,0,1],
				[2,0,0,0],
				[3,0,0,1],
				[0,2,0,0],
				[0,2,0,1],
				[0,2,0,0],
				[0,2,0,1],
				[0,0,1,1],
				[0,0,1,0],
				[0,0,3,1],
				[0,0,1,0],
				[0,0,1,1],
				[0,0,1,0]], columns= yticks + ['class'])
	'''

	# split data, class // both should be same length
	runlength_class = runlength_df['class'] # class info
	runlength_model = runlength_df[yticks] # run length info of model prediction

	print(runlength_class)
	print(runlength_model)

	#### 2. matplotlib??? figure ??? axis ??????
	fig, ax = plt.subplots(3,1,figsize=(26,20)) # 1x1 figure matrix ??????, ??????(18??????)x??????(20??????) ????????????


	plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0, 
                    hspace=0.35)

	# print(fig)
	
	##### initalize label for legned, this code should be write before writing barchart #####
	init_bar = ax[0].barh(range(len(yticks)), np.zeros(len(yticks)), label=label_names[IB], height=height, color=colors[IB]) # dummy data
	init_bar = ax[0].barh(range(len(yticks)), np.zeros(len(yticks)), label=label_names[OOB], height=height, color=colors[OOB]) # dummy data
	##### #### #### #### ##### #### #### #### 


	# data processing for barchart
	data = np.array(runlength_model.to_numpy()) # width
	data_cum = data.cumsum(axis=0) # for calc start index

	print(data)
	print(data_cum)

	#### 3. bar ?????????
	for i, frame_class in enumerate(runlength_class) :
		print(data[i,:])
		print(frame_class)

		widths = data[i,:]
		starts= data_cum[i,:] - widths
		
		bar = ax[0].barh(range(len(yticks)), widths, left=starts, height=height, color=colors[frame_class]) # don't input label

	
	#### 3_1. Evaluation Metric calc ??? barchart oob metric ??????
	Total_Evaluation_df = df(index=range(0, 0), columns=['Model', 'kernel_size', 'CONFIDENCE_metric', 'correspondence', 'UN_correspondence', 'OVER_estimation', 'UNDER_estimtation', 'FN', 'FP', 'TN', 'TP', 'TOTAL'])

	for i, model in enumerate(yticks) :
		print(i, model)
		# calc Evaluation Metric
		metric_frame_df = return_metric_frame(df(predict_data), 'GT', model)
		
		Evaluation_metric = calc_OOB_Evaluation_metric(len(metric_frame_df['FN_df']), len(metric_frame_df['FP_df']), len(metric_frame_df['TN_df']), len(metric_frame_df['TP_df']))
		Evaluation_df = df(Evaluation_metric, index=[0])

		# Evaluation_df.insert(0, 'kernel_size', args.kernel_size)
		Evaluation_df.insert(0, 'Model', model)

		print(Evaluation_df)

		Total_Evaluation_df = pd.concat([Total_Evaluation_df, Evaluation_df], ignore_index=True)

		text_bar = ax[0].barh(i, 0, height=height) # dummy data
		# present_text(ax, text_bar, ' CONFIDENCE_METRIC : {:.3f} | OVER_ESTIMATION : {:.3f} | UNDER_ESTIMATION : {:.3f} \n FN : {} | FP : {} | TN : {} | TP : {} | TOTAL : {}'.format(Evaluation_metric['CONFIDENCE_metric'], Evaluation_metric['OVER_estimation'], Evaluation_metric['UNDER_estimtation'], Evaluation_metric['FN'], Evaluation_metric['FP'], Evaluation_metric['TN'], Evaluation_metric['TP'], Evaluation_metric['TOTAL']))
		present_text(ax[0], text_bar, 'CONFIDENCE_METRIC : {:.3f} | OVER_ESTIMATION : {:.3f}'.format(Evaluation_metric['CONFIDENCE_metric'], Evaluation_metric['OVER_estimation']))
	
	print(Total_Evaluation_df)

	# Evaluation Metric save
	Total_Evaluation_df.to_csv(os.path.join(args.results_save_dir, '{}-{}-Evaluation.csv'.format(args.title_name, args.sub_title_name)), mode='w') # mode='w', 'a'

	##### 3.2 section OOB Metric
	section_confidence_dict = {}
	section_over_dict = {}


	total_info_df = df(predict_data)
	total_len = len(total_info_df)
	
	# init_variable # 21.06.04 HG ?????? - change to parser variable
	## INFERENCE STEP = 1 | WINDOW_SIZE = 5000 | OVERLAP_OVERLAP_SECTION_NUM = 3
	## INFERENCE STEP = 5 | WINDOW_SIZE = 1000 | OVERLAP_OVERLAP_SECTION_NUM = 3
	INFERENCE_STEP = args.INFERENCE_STEP ## Frame Inference Step, it will be calc for xlabel and section of start,end idx so you should correctly set as same as test.py --inference_step
	
	WINDOW_SIZE = args.WINDOW_SIZE # count of frame in one section
	OVERLAP_OVERLAP_SECTION_NUM = args.OVERLAP_SECTION_NUM # overlap section count, if you set OVERLAP_OVERLAP_SECTION_NUM = 1, it means non overlap

	slide_window_start_end_idx= [[start_idx * WINDOW_SIZE, (start_idx+OVERLAP_OVERLAP_SECTION_NUM) * WINDOW_SIZE] for start_idx in range(int(math.ceil(total_len/WINDOW_SIZE)))]
	
	print(slide_window_start_end_idx)
	print(slide_window_start_end_idx)
	print(total_len)
	
	# affine end_idx (last)
	for z in range(1, OVERLAP_OVERLAP_SECTION_NUM+1) : 
		slide_window_start_end_idx[z*-1][1] = total_len
	
	print(slide_window_start_end_idx)
	print(total_len)
	
	
	frame_start_idx = [start_idx * INFERENCE_STEP for start_idx, end_idx in slide_window_start_end_idx]
	time_start_idx = [time_label[frame_label.index(idx)] for idx in frame_start_idx]
	
	frame_end_idx = [(end_idx-1) * INFERENCE_STEP for start_idx, end_idx in slide_window_start_end_idx]
	time_end_idx = [time_label[frame_label.index(idx)] for idx in frame_end_idx]

	section_confidence_dict = {'Frame_start_idx': frame_start_idx, 'Time_start_idx': time_start_idx, 'Frame_end_idx': frame_end_idx, 'Time_end_idx': time_end_idx}
	section_over_dict = {'Frame_start_idx': frame_start_idx, 'Time_start_idx': time_start_idx, 'Frame_end_idx': frame_end_idx, 'Time_end_idx': time_end_idx}

	print(section_confidence_dict)
	

	# calc section metric per model
	for i, model in enumerate(yticks) :
		print(i, model)
		model_section_confidence_metric_list = []
		model_section_over_metric_list = []

		for start, end in slide_window_start_end_idx : # slicing
			print('start : {}, end : {}, model : {}'.format(start,end,model))
			metric_frame_df = return_metric_frame(total_info_df.iloc[start:end, :], 'GT', model)

			
			print(metric_frame_df['FN_df'])
			print(metric_frame_df['FP_df'])
			print(metric_frame_df['TN_df'])
			print(metric_frame_df['TP_df'])
			
			Evaluation_metric = calc_OOB_Evaluation_metric(len(metric_frame_df['FN_df']), len(metric_frame_df['FP_df']), len(metric_frame_df['TN_df']), len(metric_frame_df['TP_df']))
			Evaluation_df = df(Evaluation_metric, index=[0])

			print(Evaluation_metric['CONFIDENCE_metric'])

			model_section_confidence_metric_list.append(Evaluation_metric['CONFIDENCE_metric']) # section Confidence metric
			model_section_over_metric_list.append(Evaluation_metric['OVER_estimation']) # section Over metric


		
		# model save oob_metric 
		section_confidence_dict[model] = copy.deepcopy(model_section_confidence_metric_list) # deep copy 
		section_over_dict[model] = copy.deepcopy(model_section_over_metric_list) # deep copy 

		text_bar = ax[0].barh(i, 0, height=height) # dummy data

		# oob_metric -> EXCEPTION_NUM == > 1.0 ?????? // TN ??? ????????????		
		for k in range(len(model_section_confidence_metric_list)) :
			if model_section_confidence_metric_list[k] == EXCEPTION_NUM :
				model_section_confidence_metric_list[k] = 1.0

				# ?????? ?????? ?????? (Exception)
				pos_x = frame_start_idx[k]
				present_text_for_section(ax[0], text_bar, frame_label.index(frame_start_idx[k]), '\n\n???')

			elif model_section_confidence_metric_list[k] == -1.0 : # ?????? -1.0
				# ?????? ?????? ?????? (Exception)
				pos_x = frame_start_idx[k]
				present_text_for_section(ax[0], text_bar, frame_label.index(frame_start_idx[k]), '\n\n???', color='red')
		
				
		
		# ranking // ?????? ?????? ?????? 3???(MIN_NUM) ?????? ??? ?????? (EXCEPTION_NUM ==> 1?????? ??????)
		MIN_COUNT = 3
		model_section_oob_metric_numpy = np.array(model_section_confidence_metric_list)
		model_section_oob_metric_numpy[np.where(model_section_oob_metric_numpy == -1.0)] = 100 # -1.0??? sort?????? ??????
		sort_index = np.argsort(model_section_oob_metric_numpy)

		print(section_confidence_dict[model])

		for rank, idx in enumerate(sort_index[:MIN_COUNT], 1) :
			pos_x = frame_label.index(section_confidence_dict['Frame_start_idx'][idx]) # x position
			
			# ranking ??? ????????? ?????? texting
			if rank == 1 : 
				section_text = ' R-{} | C-{:.3f} | O-{:.3f}'.format(rank, model_section_confidence_metric_list[idx], model_section_over_metric_list[idx])
			elif rank == 2 : 
				section_text = '\n R-{} | C-{:.3f} | O-{:.3f}'.format(rank, model_section_confidence_metric_list[idx], model_section_over_metric_list[idx])
			elif rank == 3 : 
				section_text = '\n\n R-{} | C-{:.3f} | O-{:.3f}'.format(rank, model_section_confidence_metric_list[idx], model_section_over_metric_list[idx])
			else : 
				section_text = ' R-{} | C-{:.3f} | O-{:.3f}'.format(rank, model_section_confidence_metric_list[idx], model_section_over_metric_list[idx])

			present_text_for_section(ax[0], text_bar, pos_x, section_text)
		


	# total section Confidence Metric Results
	Confidence_metric_per_section_df = df(section_confidence_dict) # confidence metric
	Over_metric_per_section_df = df(section_over_dict) # over metric


	print(Confidence_metric_per_section_df)
	print(Over_metric_per_section_df)

	# OOB Section Metric Save
	Confidence_metric_per_section_df.to_csv(os.path.join(args.results_save_dir, '{}-{}-Section_Confidence_metric.csv'.format(args.title_name, args.sub_title_name)), mode='w') # mode='w', 'a'
	Over_metric_per_section_df.to_csv(os.path.join(args.results_save_dir, '{}-{}-Section_Over_metric.csv'.format(args.title_name, args.sub_title_name)), mode='w') # mode='w', 'a'
		
	# OOB Section Metric Plot
	section_confidence_metric_plt(Confidence_metric_per_section_df, yticks, ax[1], title='Confidence Metric Per Section \n WINDOW SIZE : {} | WINDOW NUM : {} | INFERENCE STEP : {}'.format(WINDOW_SIZE, OVERLAP_OVERLAP_SECTION_NUM, INFERENCE_STEP))
	section_over_metric_plt(Over_metric_per_section_df, yticks, ax[2], title='Over Estimation Metric Per Section \n WINDOW SIZE : {} | WINDOW NUM : {} | INFERENCE STEP : {}'.format(WINDOW_SIZE, OVERLAP_OVERLAP_SECTION_NUM, INFERENCE_STEP))

	#### 4. title ??????
	fig.suptitle(args.title_name, fontsize=16)
	ax[0].set_title(args.sub_title_name)

	#### 6. x??? ????????????
	step_size = WINDOW_SIZE # xtick step_size
	ax[0].set_xticks(range(0, len(frame_label), step_size)) # step_size
	
	print('\n\n===== XTICKS =====\n\n')
	xtick_labels = ['{}\n{}'.format(time, frame) if i_th % 2 == 0 else '\n\n{}\n{}'.format(time, frame) for i_th, (time, frame) in enumerate(zip(frame_label[::step_size], time_label[::step_size]))]
	print(xtick_labels)

	ax[0].set_xticklabels(xtick_labels) # xtick change
	ax[0].xaxis.set_tick_params(labelsize=6)
	ax[0].set_xlabel('Frame / Time (h:m:s:fps)', fontsize=12)
	
	#### 7. y??? ????????????
	ax[0].set_yticks(range(len(yticks)))
	ax[0].set_yticklabels(yticks, fontsize=10)	
	ax[0].set_ylabel('Model', fontsize=12)
	
	#### 8. ?????? ????????????
	box = ax[0].get_position() # ????????? ??????????????? ?????? ??????????????? ??????????????? ??????
	ax[0].set_position([box.x0, box.y0, box.width * 0.9, box.height])
	ax[0].legend(label_names, loc='center left', bbox_to_anchor=(1,0.5), shadow=True, ncol=1)
	
	#### 9. ?????????(?????????) ????????????
	ax[0].set_axisbelow(True)
	ax[0].xaxis.grid(True, color='gray', linestyle='dashed', linewidth=0.5)
	
	#### 10. ????????? ???????????? ????????????
	# fig.tight_layout() # subbplot ?????? ?????????
	plt.show()
	plt.savefig(os.path.join(args.results_save_dir, '{}-{}.png'.format(args.title_name, args.sub_title_name)), format='png', dpi=500)
	

def section_confidence_metric_plt(Confidence_metric_per_section_df, model_list, ax, title) :
	x_value = Confidence_metric_per_section_df['Frame_start_idx']

	for model in model_list :
		# EXCPETION NUM (-100) ????????? 1??? ??????
		ax.plot(x_value, [1.0 if val==EXCEPTION_NUM else val for val in Confidence_metric_per_section_df[model]], marker='o', markersize=4, alpha=1.0)

		# exception mark (-1.0??? ?????? 1??? ???????????? ^ ??????)
		'''
		exception_index = Confidence_metric_per_section_df[model]== -1.0
		print(exception_index)
		print(x_value[exception_index])
		print(Confidence_metric_per_section_df[model][exception_index])
		markersize=15
		
		print([1.0]*len(x_value[exception_index]))
		ax.scatter(x_value[exception_index], [1.2]*len(x_value[exception_index]), marker='^', s=15)
		'''


	# sup title ??????
	ax.set_title(title)

	# x ??? ????????????

	#### 6. x??? ????????????
	ax.set_xticks(x_value)

	xtick_labels = ['{}\n{}'.format(time, frame) if i_th % 2 == 0 else '\n\n{}\n{}'.format(time, frame) for i_th, (time, frame) in enumerate(zip(x_value, Confidence_metric_per_section_df['Time_start_idx']))]
	ax.set_xticklabels(xtick_labels) # xtick change
	# ax.set_xticklabels(['{}\n{}'.format(time, frame) for time, frame in zip(x_value, Confidence_metric_per_section_df['Time_start_idx'])]) # xtick change
	ax.xaxis.set_tick_params(labelsize=6)
	ax.set_xlabel('Start Frame / Time (h:m:s:fps)', fontsize=12)

	# y ??? ????????????
	ax.set_ylabel('Confidence Metric', fontsize=12)

	# ?????????(?????????) ????????????
	ax.set_axisbelow(True)
	ax.xaxis.grid(True, color='gray', linestyle='dashed', linewidth=0.5)

	# ??????
	box = ax.get_position() # ????????? ??????????????? ?????? ??????????????? ??????????????? ??????
	ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
	ax.legend(model_list, loc='center left', bbox_to_anchor=(1,0.5), shadow=True, ncol=1)

def section_over_metric_plt(Over_metric_per_section_df, model_list, ax, title) :
	x_value = Over_metric_per_section_df['Frame_start_idx']

	for model in model_list :
		# EXCPETION NUM (-100) ????????? 0??? ??????
		ax.plot(x_value, [0.0 if val==EXCEPTION_NUM else val for val in Over_metric_per_section_df[model]], marker='o', markersize=4, alpha=1.0)

		# exception mark (-1.0??? ?????? 1??? ???????????? ^ ??????)
		'''
		exception_index = Over_metric_per_section_df[model]== -1.0
		print(exception_index)
		print(x_value[exception_index])
		print(Over_metric_per_section_df[model][exception_index])
		markersize=15
		
		print([1.0]*len(x_value[exception_index]))
		ax.scatter(x_value[exception_index], [1.2]*len(x_value[exception_index]), marker='^', s=15)
		'''


	# sup title ??????
	ax.set_title(title)

	# x ??? ????????????
	ax.set_xticks(x_value)
	
	xtick_labels = ['{}\n{}'.format(time, frame) if i_th % 2 == 0 else '\n\n{}\n{}'.format(time, frame) for i_th, (time, frame) in enumerate(zip(x_value, Over_metric_per_section_df['Time_start_idx']))]
	ax.set_xticklabels(xtick_labels) # xtick change
	
	# ax.set_xticklabels(['{}\n{}'.format(time, frame) for time, frame in zip(x_value, Over_metric_per_section_df['Time_start_idx'])]) # xtick change
	ax.xaxis.set_tick_params(labelsize=6)
	ax.set_xlabel('Start Frame / Time (h:m:s:fps)', fontsize=12)

	# y ??? ????????????
	ax.set_ylabel('Over estimation Metric', fontsize=12)

	# ?????????(?????????) ????????????
	ax.set_axisbelow(True)
	ax.xaxis.grid(True, color='gray', linestyle='dashed', linewidth=0.5)


	# ??????
	box = ax.get_position() # ????????? ??????????????? ?????? ??????????????? ??????????????? ??????
	ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
	ax.legend(model_list, loc='center left', bbox_to_anchor=(1,0.5), shadow=True, ncol=1)

if __name__=='__main__':
	# main()
	total_eval_root_path = '/OOB_RECOG/POST_PROCESSING/robot-oob-v2-mobilenet_v3_large-1fps/total-median'
	aggregation_post_processing_results(total_eval_root_path)
	
	




