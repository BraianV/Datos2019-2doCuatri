import pandas as pd
import numpy as np


def get_topicos_in_column(df, topicos, feature_to_find ,feature_new_name):

	dataframe = df.copy()
	dataframe[feature_to_find].fillna("sin dato", inplace = True)

	train_descrip = dataframe.loc[:,['id',feature_to_find]]
	train_descrip[feature_to_find] = train_descrip[feature_to_find].apply(lambda x : clean.clean_text(x))


	train_descrip[feature_new_name] = train_descrip[feature_to_find].apply(lambda x: 1 if any(word in x for word in topicos) else 0)

	return dataframe
