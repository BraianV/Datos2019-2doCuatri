import pandas as pd
import numpy as np
import filter_feature_string as clean



def get_topicos_in_column(df, topicos, feature_to_find ,feature_new_name):

	dataframe = df.copy()
	dataframe[feature_to_find].fillna("sin dato", inplace = True)

	df_with_new_feature = dataframe.loc[:,['id',feature_to_find]]
	df_with_new_feature[feature_to_find] = df_with_new_feature[feature_to_find].apply(lambda x : clean.clean_text(x))


	df_with_new_feature[feature_new_name] = df_with_new_feature[feature_to_find].apply(lambda x: 1 if any(word in x for word in topicos) else 0)

	df_with_new_feature = df_with_new_feature.loc[:,['id',feature_new_name]]

	print("Distribucion del feature : {}".format(feature_new_name))
	print(df_with_new_feature[feature_new_name].value_counts(normalize = True))

	return df_with_new_feature
