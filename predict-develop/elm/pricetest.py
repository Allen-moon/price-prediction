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
	with open('pb.csv', 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
		sql='SELECT * FROM PB'
		columns=db_conn.get_col_names(sql)
		spamwriter.writerow(columns)
		rs= db_conn.select(sql)
		print(len(rs))
		for r in rs:
			spamwriter.writerow(r)
	data = pd.read_csv('pb.csv')
	outputy=['after_1mon', 'after_2mon', 'after_3mon', 'after_4mon', 'after_5mon', 'after_6mon']
	columns_feature=columns.copy()
	for col in outputy:
		columns_feature.remove(col)
	# print(columns)
	#Y = data['after_1mon', 'after_2mon', 'after_3mon', 'after_4mon', 'after_5mon', 'after_6mon']
	# data = pd.read_csv('csvfile/external_eles.csv')
	# feature_cols = ['scrap','cooking_coal','iron_powder','now_ore','import_ore']
	X = data[columns_feature]
	Y = data[outputy]
	Y_array=np.array(Y)
	origal_mean=Y_array.mean(axis=0)#0表示列，1表示行
	origal_std=Y_array.std(axis=0)

	data_scale=preprocessing.scale(np.array(data))
	# print(type(data_scale))
	data_scale_df=pd.DataFrame(data_scale,columns=columns)
	# print(data_scale_df)
	X_scale=data_scale_df[columns_feature]
	Y_scale=data_scale_df[outputy]
	# print(X_scale)
	# print(Y_scale)
	X_train, X_test, y_train, y_test = train_test_split(X_scale,Y_scale,test_size=0.2,random_state=1)

	print(y_test)

	elmr = ELMRegressor(activation_func='inv_tribas', random_state=0)
	elmr.fit(X_train, y_train)
	y_predict=elmr.predict(X_test)
	# print(y_predict)
	# print(y_test)
	row_num=y_predict.shape[0]
	col_num=y_predict.shape[1]
	for xi in range(row_num):
		for yi in range(col_num):
			# print("*******************")
			# print(origal_std[yi])
			# print(origal_mean[yi])
			y_predict[xi][yi]=y_predict[xi][yi]*origal_std[yi]+origal_mean[yi]
			# print(y_predict[xi][yi])
	# print(y_predict)
	'''
	Returns the coefficient of determination R^2 of the prediction.
	The coefficient R^2 is defined as (1 - u/v),
	where u is the regression sum of squares ((y_true - y_pred) ** 2).sum() 
	and v is the residual sum of squares ((y_true - y_true.mean()) ** 2).sum(). 
	Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse).
	A constant model that always predicts the expected value of y, 
	disregarding the input features, would get a R^2 score of 0.0.
	'''
	error=elmr.score( X_test, y_test)
	print(error)
	#plt.plot(X_test,y_predict)
	# plt.show()