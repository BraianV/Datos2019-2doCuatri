from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np




def label_encoder(datafram):

	labelencoder = LabelEncoder()
	X = datafram.copy()

	X.tipodepropiedad = labelencoder.fit_transform(X.tipodepropiedad)
	X.provincia = labelencoder.fit_transform(X.provincia)
	X.ciudad = labelencoder.fit_transform(X.ciudad)

	return X