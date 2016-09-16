from time import time
import csv
from sklearn.cluster import k_means
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from sklearn import preprocessing

from elm import ELMClassifier, ELMRegressor, GenELMClassifier, GenELMRegressor
from random_layer import RandomLayer, MLPRandomLayer, RBFRandomLayer, GRBFRandomLayer
from math import sqrt
import mysql as dbconn

if __name__ == "__main__":
	db_conn = dbconn.MySQL()
	# date_init = "2014-12-31"
	sql='SELECT * FROM PB'
	columns=db_conn.get_col_names(sql)
	# print(columns)


	file = open("1.csv")
	try:
		data = file.read()
	finally:
		file.close()
	# print(data)


	with open('pb.csv', 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
		sql='SELECT * FROM PB'
		columns=db_conn.get_col_names(sql)
		spamwriter.writerow(columns)
		rs= db_conn.select(sql)
		# print(len(rs))
		for r in rs:
			spamwriter.writerow(r)

	with open("1.csv") as file:
		data = file.read()
	# print(data)

	data = pd.read_csv('pb.csv')
	
	outputy=['after_1mon', 'after_2mon', 'after_3mon', 'after_4mon', 'after_5mon', 'after_6mon']

	''' 3 yinsu '''
	# 0.732
	# els = ['fore_PMI_1','fore_PMI_2','fore_PMI_3','fore_PMI_4','fore_PMI_5','fore_PMI_6'
			# 'fore_tksjkl_1','fore_tksjkl_2','fore_tksjkl_3','fore_tksjkl_4','fore_tksjkl_5','fore_tksjkl_6',
			# 'fore_tksykcl_1','fore_tksykcl_2','fore_tksykcl_3','fore_tksykcl_4','fore_tksykcl_5','fore_tksykcl_6']

	# 0.524
	# els = ['fore_PMI_1','fore_PMI_2','fore_PMI_3','fore_PMI_4','fore_PMI_5','fore_PMI_6']

	# 0.50
	# els = ['fore_tksjkl_1','fore_tksjkl_2','fore_tksjkl_3','fore_tksjkl_4','fore_tksjkl_5','fore_tksjkl_6']


	# 0.67
	# els = ['fore_tksykcl_1','fore_tksykcl_2','fore_tksykcl_3','fore_tksykcl_4','fore_tksykcl_5','fore_tksykcl_6']

	# 0.737
	# els = ['fore_PMI_1','fore_PMI_2','fore_PMI_3','fore_PMI_4','fore_PMI_5','fore_PMI_6',
	# 		'fore_tksykcl_1','fore_tksykcl_2','fore_tksykcl_3','fore_tksykcl_4','fore_tksykcl_5','fore_tksykcl_6']

	# 0.78
	els = ['after_1mon', 'after_2mon', 'after_3mon', 'after_4mon', 'after_5mon', 'after_6mon',
			'fore_tksjkl_1','fore_tksjkl_2','fore_tksjkl_3','fore_tksjkl_4','fore_tksjkl_5','fore_tksjkl_6',
			'fore_tksykcl_1','fore_tksykcl_2','fore_tksykcl_3','fore_tksykcl_4','fore_tksykcl_5','fore_tksykcl_6']
	''' 3 yinsu '''


	''' 5 yinsu  '''
	# 0.88
	es = [
		# 'fore_meiyuan_1','fore_meiyuan_2','fore_meiyuan_3','fore_meiyuan_4','fore_meiyuan_5','fore_meiyuan_6',
		# 'fore_psjgzs_1','fore_psjgzs_2','fore_psjgzs_3','fore_psjgzs_4','fore_psjgzs_5','fore_psjgzs_6',
		'fore_haiyunBDI_1','fore_haiyunBDI_2','fore_haiyunBDI_3','fore_haiyunBDI_4','fore_haiyunBDI_5','fore_haiyunBDI_6',
		'fore_haiyunBCI_1','fore_haiyunBCI_2','fore_haiyunBCI_3','fore_haiyunBCI_4','fore_haiyunBCI_5','fore_haiyunBCI_6',
		'fore_haiyunBDTI_1','fore_haiyunBDTI_2','fore_haiyunBDTI_3','fore_haiyunBDTI_4','fore_haiyunBDTI_5','fore_haiyunBDTI_6',
		# 'fore_WTI_1','fore_WTI_2','fore_WTI_3','fore_WTI_4','fore_WTI_5','fore_WTI_6',
		# 'before_1mon','before_2mon','before_3mon','before_4mon','before_5mon','before_6mon'
		]			


	# # 0.66
	# es = ['fore_meiyuan_1','fore_meiyuan_2','fore_meiyuan_3','fore_meiyuan_4','fore_meiyuan_5','fore_meiyuan_6',
	# 	'fore_psjgzs_1','fore_psjgzs_2','fore_psjgzs_3','fore_psjgzs_4','fore_psjgzs_5','fore_psjgzs_6']
	# 	# 'fore_haiyunBDI_1','fore_haiyunBDI_2','fore_haiyunBDI_3','fore_haiyunBDI_4','fore_haiyunBDI_5','fore_haiyunBDI_6',
	# 	# 'fore_haiyunBCI_1','fore_haiyunBCI_2','fore_haiyunBCI_3','fore_haiyunBCI_4','fore_haiyunBCI_5','fore_haiyunBCI_6',
	# 	# 'fore_haiyunBDTI_1','fore_haiyunBDTI_2','fore_haiyunBDTI_3','fore_haiyunBDTI_4','fore_haiyunBDTI_5','fore_haiyunBDTI_6',
	# 	# 'fore_WTI_1','fore_WTI_2','fore_WTI_3','fore_WTI_4','fore_WTI_5','fore_WTI_6']	

	# # 0.64
	# es = ['fore_meiyuan_1','fore_meiyuan_2','fore_meiyuan_3','fore_meiyuan_4','fore_meiyuan_5','fore_meiyuan_6',
	# 	'fore_psjgzs_1','fore_psjgzs_2','fore_psjgzs_3','fore_psjgzs_4','fore_psjgzs_5','fore_psjgzs_6',
	# 	'fore_haiyunBDI_1','fore_haiyunBDI_2','fore_haiyunBDI_3','fore_haiyunBDI_4','fore_haiyunBDI_5','fore_haiyunBDI_6']
	# 	# 'fore_haiyunBCI_1','fore_haiyunBCI_2','fore_haiyunBCI_3','fore_haiyunBCI_4','fore_haiyunBCI_5','fore_haiyunBCI_6',
	# 	# 'fore_haiyunBDTI_1','fore_haiyunBDTI_2','fore_haiyunBDTI_3','fore_haiyunBDTI_4','fore_haiyunBDTI_5','fore_haiyunBDTI_6',
	# 	# 'fore_WTI_1','fore_WTI_2','fore_WTI_3','fore_WTI_4','fore_WTI_5','fore_WTI_6']

	# 	# 0.85
	# es = ['fore_meiyuan_1','fore_meiyuan_2','fore_meiyuan_3','fore_meiyuan_4','fore_meiyuan_5','fore_meiyuan_6',
	# 	'fore_psjgzs_1','fore_psjgzs_2','fore_psjgzs_3','fore_psjgzs_4','fore_psjgzs_5','fore_psjgzs_6',
	# 	'fore_haiyunBDI_1','fore_haiyunBDI_2','fore_haiyunBDI_3','fore_haiyunBDI_4','fore_haiyunBDI_5','fore_haiyunBDI_6',
	# 	'fore_haiyunBCI_1','fore_haiyunBCI_2','fore_haiyunBCI_3','fore_haiyunBCI_4','fore_haiyunBCI_5','fore_haiyunBCI_6',
	# 	'fore_haiyunBDTI_1','fore_haiyunBDTI_2','fore_haiyunBDTI_3','fore_haiyunBDTI_4','fore_haiyunBDTI_5','fore_haiyunBDTI_6']
	# 	# 'fore_WTI_1','fore_WTI_2','fore_WTI_3','fore_WTI_4','fore_WTI_5','fore_WTI_6']

	# 	# 0.70
	# es = [
	# 	'fore_haiyunBDTI_1','fore_haiyunBDTI_2','fore_haiyunBDTI_3','fore_haiyunBDTI_4','fore_haiyunBDTI_5','fore_haiyunBDTI_6',
	# 	'fore_WTI_1','fore_WTI_2','fore_WTI_3','fore_WTI_4','fore_WTI_5','fore_WTI_6']
	# print(es)

	# # 0.86
	# es = [
	# 	'fore_haiyunBDI_1','fore_haiyunBDI_2','fore_haiyunBDI_3','fore_haiyunBDI_4','fore_haiyunBDI_5','fore_haiyunBDI_6',
	# 	'fore_haiyunBCI_1','fore_haiyunBCI_2','fore_haiyunBCI_3','fore_haiyunBCI_4','fore_haiyunBCI_5','fore_haiyunBCI_6',
	# 	'fore_haiyunBDTI_1','fore_haiyunBDTI_2','fore_haiyunBDTI_3','fore_haiyunBDTI_4','fore_haiyunBDTI_5','fore_haiyunBDTI_6',
	# 	'fore_WTI_1','fore_WTI_2','fore_WTI_3','fore_WTI_4','fore_WTI_5','fore_WTI_6']

 #    # 0.83		
	# es = [
	# 	'fore_haiyunBDI_1','fore_haiyunBDI_2','fore_haiyunBDI_3','fore_haiyunBDI_4','fore_haiyunBDI_5','fore_haiyunBDI_6',
	# 	'fore_haiyunBCI_1','fore_haiyunBCI_2','fore_haiyunBCI_3','fore_haiyunBCI_4','fore_haiyunBCI_5','fore_haiyunBCI_6',
	# 	'fore_haiyunBDTI_1','fore_haiyunBDTI_2','fore_haiyunBDTI_3','fore_haiyunBDTI_4','fore_haiyunBDTI_5','fore_haiyunBDTI_6']
	# 	# 'fore_WTI_1','fore_WTI_2','fore_WTI_3','fore_WTI_4','fore_WTI_5','fore_WTI_6']

 #    # 0.65		
	# es = [
	# 	# 'fore_haiyunBDI_1','fore_haiyunBDI_2','fore_haiyunBDI_3','fore_haiyunBDI_4','fore_haiyunBDI_5','fore_haiyunBDI_6',
	# 	# 'fore_haiyunBCI_1','fore_haiyunBCI_2','fore_haiyunBCI_3','fore_haiyunBCI_4','fore_haiyunBCI_5','fore_haiyunBCI_6',
	# 	# 'fore_haiyunBDTI_1','fore_haiyunBDTI_2','fore_haiyunBDTI_3','fore_haiyunBDTI_4','fore_haiyunBDTI_5','fore_haiyunBDTI_6']
	# 	'fore_WTI_1','fore_WTI_2','fore_WTI_3','fore_WTI_4','fore_WTI_5','fore_WTI_6']


 #    # 0.72		
	# es = [
	# 	# 'fore_haiyunBDI_1','fore_haiyunBDI_2','fore_haiyunBDI_3','fore_haiyunBDI_4','fore_haiyunBDI_5','fore_haiyunBDI_6',
	# 	'fore_haiyunBCI_1','fore_haiyunBCI_2','fore_haiyunBCI_3','fore_haiyunBCI_4','fore_haiyunBCI_5','fore_haiyunBCI_6',
	# 	'fore_haiyunBDTI_1','fore_haiyunBDTI_2','fore_haiyunBDTI_3','fore_haiyunBDTI_4','fore_haiyunBDTI_5','fore_haiyunBDTI_6']
	# 	# 'fore_WTI_1','fore_WTI_2','fore_WTI_3','fore_WTI_4','fore_WTI_5','fore_WTI_6']


 #    # 0.70		
	# es = [
	# 	'fore_haiyunBDI_1','fore_haiyunBDI_2','fore_haiyunBDI_3','fore_haiyunBDI_4','fore_haiyunBDI_5','fore_haiyunBDI_6',
	# 	# 'fore_haiyunBCI_1','fore_haiyunBCI_2','fore_haiyunBCI_3','fore_haiyunBCI_4','fore_haiyunBCI_5','fore_haiyunBCI_6',
	# 	'fore_haiyunBDTI_1','fore_haiyunBDTI_2','fore_haiyunBDTI_3','fore_haiyunBDTI_4','fore_haiyunBDTI_5','fore_haiyunBDTI_6']
	# 	# 'fore_WTI_1','fore_WTI_2','fore_WTI_3','fore_WTI_4','fore_WTI_5','fore_WTI_6']
		
 #    # 0.65		
	# es = [
	# 	# 'fore_haiyunBDI_1','fore_haiyunBDI_2','fore_haiyunBDI_3','fore_haiyunBDI_4','fore_haiyunBDI_5','fore_haiyunBDI_6',
	# 	# 'fore_haiyunBCI_1','fore_haiyunBCI_2','fore_haiyunBCI_3','fore_haiyunBCI_4','fore_haiyunBCI_5','fore_haiyunBCI_6']
	# 	# 'fore_haiyunBDTI_1','fore_haiyunBDTI_2','fore_haiyunBDTI_3','fore_haiyunBDTI_4','fore_haiyunBDTI_5','fore_haiyunBDTI_6']
	# 	'fore_WTI_1','fore_WTI_2','fore_WTI_3','fore_WTI_4','fore_WTI_5','fore_WTI_6']

	# # 0.
	# es = [
	# 	'fore_haiyunBDI_1','fore_haiyunBDI_2','fore_haiyunBDI_3','fore_haiyunBDI_4','fore_haiyunBDI_5','fore_haiyunBDI_6',
	# 	'fore_haiyunBCI_1','fore_haiyunBCI_2','fore_haiyunBCI_3','fore_haiyunBCI_4','fore_haiyunBCI_5','fore_haiyunBCI_6',
	# 	'fore_haiyunBDTI_1','fore_haiyunBDTI_2','fore_haiyunBDTI_3','fore_haiyunBDTI_4','fore_haiyunBDTI_5','fore_haiyunBDTI_6',
	# 	'fore_WTI_1','fore_WTI_2','fore_WTI_3','fore_WTI_4','fore_WTI_5','fore_WTI_6'
	# 	]




	columns_feature=columns.copy()

	# print(columns)
	# print(columns_feature)
	# for col in outputy:
	# 	columns_feature.remove(col)

	for col in els:
		columns_feature.remove(col)

	for col in es:
		columns_feature.remove(col)
	# print(columns_feature)
	# #Y = data['after_1mon', 'after_2mon', 'after_3mon', 'after_4mon', 'after_5mon', 'after_6mon']
	# # data = pd.read_csv('csvfile/external_eles.csv')
	# # feature_cols = ['scrap','cooking_coal','iron_powder','now_ore','import_ore']
	X = data[columns_feature]
	# print(type(X))
	Y = data[outputy]
	# print(type(Y))
	Y_array=np.array(Y)
	# print(type(Y_array))
	origal_mean=Y_array.mean(axis=0)#0表示列，1表示行
	origal_std=Y_array.std(axis=0)
	# print(origal_mean,origal_std)
	data_scale=preprocessing.scale(np.array(data))
	# print(data_scale)
	data_scale_df=pd.DataFrame(data_scale,columns=columns)
	# print(data_scale_df)

	print(columns_feature)
	X_scale=data_scale_df[columns_feature]
	Y_scale=data_scale_df[outputy]
	# print(X_scale)
	# print(Y_scale)
	X_train, X_test, y_train, y_test = train_test_split(X_scale,Y_scale,test_size=0.2,random_state=1)

	# print(y_train)
	# print(X_test[2][2])

	elmr = GenELMRegressor()
	elmr.fit(X_train, y_train)

	# print(y_test)
	y_predict=elmr.predict(X_test)
	# print(type(y_predict))
	# print(type(y_test

	# print(y_predict)
	# y_frame = pd.DataFrame(y_predict,columns=outputy)
	# print(y_frame)

	y_test_1 = np.array(y_test)
	# print(y_test)
	row_num=y_predict.shape[0]
	col_num=y_predict.shape[1]
	# cha = [row_num][col_num]
	# print(range(row_num-1),range(col_num-1))
	flag = 0
	for xi in range(row_num):
		for yi in range(col_num):
			# print("*******************")
			# print(origal_std[yi])
			# print(origal_mean[yi])
			# print(y_predict[xi][yi])
			y_predict[xi][yi]=y_predict[xi][yi]*origal_std[yi]+origal_mean[yi]
			# y_predict[xi][yi] = round(y_predict[xi][yi], 1)

			y_test_1[xi][yi]=y_test_1[xi][yi]*origal_std[yi]+origal_mean[yi]
			# y_test_1[xi][yi] = round(y_test_1[xi][yi], 1)

			y_test_1[xi][yi] = y_predict[xi][yi] - y_test_1[xi][yi] 
			y_test_1[xi][yi] = round(y_test_1[xi][yi], 1)

			cha = y_test_1[xi][yi]/y_predict[xi][yi]
			print(np.fabs(cha))
			if np.fabs(cha)<0.1:
				flag = flag + 1
			# print(y_predict[xi][yi])
	print(type(y_predict))
	# print(y_predict)
	row_num=y_predict.shape[0]
	col_num=y_predict.shape[1]
	# print(row_num,col_num)
	
	# print(y_test)

	# cha = y_predict-y_test_1
	# cha = round(cha, 1)
	'''chazhi'''
	print(y_test_1)
	print(y_test_1.shape)
	# Y_array=np.array(Y)
	# cha = y_predict - y_test
	'''rate 0f cha/predict<0.1'''
	print(flag/642)
	# y_frame = pd.DataFrame(y_predict,columns=outputy)
	# print(y_predict)
	# print(y_test*origal_std[yi]+origal_mean[yi])
	# print(y_frame)


	# '''
	# Returns the coefficient of determination R^2 of the prediction.
	# The coefficient R^2 is defined as (1 - u/v),
	# where u is the regression sum of squares ((y_true - y_pred) ** 2).sum() 
	# and v is the residual sum of squares ((y_true - y_true.mean()) ** 2).sum(). 
	# Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse).
	# A constant model that always predicts the expected value of y, 
	# disregarding the input features, would get a R^2 score of 0.0.
	# '''
	# '''
	error=elmr.score(X_test, y_test)
	print(error)
	#plt.plot(X_test,y_predict)
	# plt.show()

