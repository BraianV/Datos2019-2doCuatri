import pandas as pd
import numpy as np


def featurizer(data):

	train = data.copy()

	train.fecha = pd.to_datetime(train.fecha)
	train['year'] = train.fecha.dt.year
	train['mes'] = train.fecha.dt.month
	train['dia_del_mes'] = train.fecha.dt.day
	train['dia_del_anio'] = train.fecha.dt.dayofyear
	train['quarter'] = train.fecha.dt.quarter


	train.year = train.year.astype(float)
	train.mes = train.mes.astype(float)
	train.dia_del_anio = train.dia_del_anio.astype(float)
	train.dia_del_mes = train.dia_del_mes.astype(float)
	train.quarter = train.quarter.astype(float)

	train['aire_libre'] = train.metrostotales - train.metroscubiertos
	train.aire_libre.fillna(0,inplace = True)

	train['metro_promedio_por_cuadricula'] = (train.habitaciones + train.banos +1 - train.garages) /  train.metroscubiertos  #El 1 representa el ambiente en comun
	train['metro_promedio_por_cuadricula'].fillna(train['metro_promedio_por_cuadricula'].mean(),inplace = True)

	train['is_DF'] = ((train.provincia == 'Distrito Federal') | (train.provincia == 'Edo. de México'))

	train['tipodepropiedad'].fillna(train['tipodepropiedad'].value_counts().idxmax(), inplace=True)
	#train['ciudad'].fillna(train['ciudad'].value_counts().idxmax(), inplace=True)
	train['provincia'].fillna(train['provincia'].value_counts().idxmax(), inplace=True)

	train['antiguedad'].fillna((train['antiguedad'].mean()), inplace=True)
	train['habitaciones'].fillna(0,inplace=True)
	train['banos'].fillna(0,inplace=True)
	train['metroscubiertos'].fillna((train['metroscubiertos'].mean()), inplace=True)
	train['metrostotales'].fillna((train['metrostotales'].mean()), inplace=True)
	train['garages'].fillna(0,inplace = True)

	

	return train
