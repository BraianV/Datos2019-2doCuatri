from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np




def label_encoder(datafram):

	labelencoder = LabelEncoder()
	X = datafram.copy()

	X.tipodepropiedad.fillna("Sin datos",inplace = True)
	X.tipodepropiedad = labelencoder.fit_transform(X.tipodepropiedad)
	
	X.provincia.fillna("Sin datos",inplace = True)
	X.provincia = labelencoder.fit_transform(X.provincia)
	
	X.ciudad.fillna("Sin datos",inplace = True)
	X.ciudad = labelencoder.fit_transform(X.ciudad)

	return X



def oneHotEncoder(train_df, test_df):

	train_oh = pd.get_dummies(train_df, dummy_na=False)
	test_oh = pd.get_dummies(test_df, dummy_na=False)
	listDropTrain = []
	listDropTest = []
	if(train_oh.shape[1] != test_oh.shape[1]):
		
		listDropTrain = listDropTrain + list(set(train_oh.columns) - set(test_oh.columns))
		listDropTest = listDropTest + list(set(test_oh.columns) - set(train_oh.columns))

	train_oh = train_oh.drop(listDropTrain, axis = 1)
	test_oh = test_oh.drop(listDropTest, axis = 1)
	return train_oh,test_oh
