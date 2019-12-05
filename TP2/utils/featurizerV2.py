import pandas as pd
import numpy as np


def featurizerv2(dataframe, type_df):

	df = dataframe.copy()
	
	path_seguridad = "features_notebooks/features_csvs/{}_descripcion_con_seguridad.csv".format(type_df)
	path_plazas = "features_notebooks/features_csvs/{}_descripcion_con_plazas.csv".format(type_df)
	path_jardin = "features_notebooks/features_csvs/{}_descripcion_con_jardin.csv".format(type_df)
	path_avenidas = "features_notebooks/features_csvs/{}_direccion_con_avenidas.csv".format(type_df)
	path_acuatica = "features_notebooks/features_csvs/{}_descripcion_con_referencias_acuaticas.csv".format(type_df)
	path_beneficios = "features_notebooks/features_csvs/{}_con_beneficios.csv".format(type_df)
	path_turismo = "features_notebooks/features_csvs/{}_descripcion_con_referencias_turisticas.csv".format(type_df)
	path_habitables = "features_notebooks/features_csvs/{}_con_propiedades_habitables.csv".format(type_df)
	path_dolar = "features_notebooks/features_csvs/{}_con_dolar_y_devaluacion.csv".format(type_df)
	path_fecha = "features_notebooks/features_csvs/{}_con_fechas_features.csv".format(type_df)
	path_mean_por_tipo_de_propiedad = "features_notebooks/features_csvs/{}_promedios_de_variables_numericas_iniciales_por_tipo_de_propiedad.csv".format(type_df)
	#path_mean_por_provincia = "features_notebooks/features_csvs/{}_promedios_de_variables_numericas_iniciales_por_provincia.csv".format(type_df)
	#path_mean_por_ciudad = "features_notebooks/features_csvs/{}_promedios_de_variables_numericas_iniciales_por_ciudad.csv".format(type_df)
	path_time_last_sell = "features_notebooks/features_csvs/{}_con_tiempo_en_dias_de_la_ultima_compra_del_mismo_tipo.csv".format(type_df)
	path_lujos ="features_notebooks/features_csvs/{}_descripcion_con_lujos.csv".format(type_df)
	path_fechas_2 = "features_notebooks/features_csvs/{}_con_fechas_features_v2.csv".format(type_df)


	df_seguridad = pd.read_csv(path_seguridad)
	df_plazas = pd.read_csv(path_plazas)
	df_jardin = pd.read_csv(path_jardin)
	df_avenidas = pd.read_csv(path_avenidas)
	df_acuaticas = pd.read_csv(path_acuatica)
	df_beneficios = pd.read_csv(path_beneficios)
	df_turismo = pd.read_csv(path_turismo)
	df_habitables = pd.read_csv(path_habitables)
	df_dolar = pd.read_csv(path_dolar)
	df_fecha = pd.read_csv(path_fecha)

	df_mean_por_tipo_de_propiedad = pd.read_csv(path_mean_por_tipo_de_propiedad)
	#df_mean_por_provincia = pd.read_csv(path_mean_por_provincia)
	#df_mean_por_ciudad = pd.read_csv(path_mean_por_ciudad)
	df_time_last_sell = pd.read_csv(path_time_last_sell)
	df_lujos = pd.read_csv(path_lujos)
	df_fechas_v2 = pd.read_csv(path_fechas_2)

	df = pd.merge(df, df_seguridad,on = 'id', how = 'inner')
	df = pd.merge(df, df_plazas,on = 'id', how = 'inner')
	df = pd.merge(df, df_jardin,on = 'id', how = 'inner')
	df = pd.merge(df, df_avenidas,on = 'id', how = 'inner')
	df = pd.merge(df, df_acuaticas,on = 'id', how = 'inner')
	df = pd.merge(df, df_beneficios,on = 'id', how = 'inner')
	df = pd.merge(df, df_turismo,on = 'id', how = 'inner')
	df = pd.merge(df, df_habitables,on = 'id', how = 'inner')
	df = pd.merge(df, df_dolar,on = 'id', how = 'inner')
	df = pd.merge(df, df_fecha,on = 'id', how = 'inner')


	# rellenado de nans

	df['aire_libre'] = df.metrostotales - df.metroscubiertos
	df.aire_libre.fillna(0,inplace = True)

	df['is_DF'] = ((df.provincia == 'Distrito Federal') | (df.provincia == 'Edo. de México'))

	df['tipodepropiedad'].fillna(df['tipodepropiedad'].value_counts().idxmax(), inplace=True)
	df['provincia'].fillna(df['provincia'].value_counts().idxmax(), inplace=True)

	df['antiguedad'].fillna((df['antiguedad'].mean()), inplace=True)
	df['habitaciones'].fillna(0,inplace=True)
	df['banos'].fillna(0,inplace=True)
	df['metroscubiertos'].fillna((df['metroscubiertos'].mean()), inplace=True)
	df['metrostotales'].fillna((df['metrostotales'].mean()), inplace=True)
	df['garages'].fillna(0,inplace = True)



	# rellenado de nans en latitude, longitude y idzona
	df['x'] = np.cos(df.lat) * np.cos(df.lng)
	df['y'] = np.cos(df.lat) * np.sin(df.lng)
	df['z'] = np.sin(df.lat)

	df.lat.fillna(0,inplace = True)
	df.lng.fillna(0,inplace = True)

	df.x.fillna(0,inplace = True)
	df.y.fillna(0,inplace = True)
	df.z.fillna(0,inplace = True)

	df.idzona.fillna(0,inplace = True)

	#rello ciudad
	df.ciudad.fillna('sin datos',inplace = True)


	#agregamos promedios

	#Tipo de propiedad mean()
	df_mean_por_tipo_de_propiedad.columns	
	df = pd.merge(df, df_mean_por_tipo_de_propiedad, on='tipodepropiedad', how='left')
	df.mean_metroscubiertos_tipodepropiedad.fillna(df.mean_metroscubiertos_tipodepropiedad.mean(),inplace = True)
	df.mean_metrostotales_tipodepropiedad.fillna(df.mean_metrostotales_tipodepropiedad.mean(),inplace = True)
	df.mean_gimnasio_tipodepropiedad.fillna(df.mean_gimnasio_tipodepropiedad.mean(),inplace = True)
	df.mean_usosmultiples_tipodepropiedad.fillna(df.mean_usosmultiples_tipodepropiedad.mean(),inplace = True)
	df.mean_piscina_tipodepropiedad.fillna(df.mean_piscina_tipodepropiedad.mean(),inplace = True)
	df.mean_escuelascercanas_tipodepropiedad.fillna(df.mean_escuelascercanas_tipodepropiedad.mean(),inplace = True)
	df.mean_centroscomercialescercanos_tipodepropiedad.fillna(df.mean_centroscomercialescercanos_tipodepropiedad.mean(),inplace = True)
	df.mean_garages_tipodepropiedad.fillna(df.mean_garages_tipodepropiedad.mean(),inplace = True)
	df.mean_banos_tipodepropiedad.fillna(df.mean_banos_tipodepropiedad.mean(),inplace = True)

	#Provincia mean()
	#df = pd.merge(df, df_mean_por_provincia, on='provincia', how='left')
	#df.mean_metroscubiertos_provincia.fillna(df.mean_metroscubiertos_provincia.mean(),inplace = True)
	#df.mean_metrostotales_provincia.fillna(df.mean_metrostotales_provincia.mean(),inplace = True)
	#df.mean_gimnasio_provincia.fillna(df.mean_gimnasio_provincia.mean(),inplace = True)
	#df.mean_usosmultiples_provincia.fillna(df.mean_usosmultiples_provincia.mean(),inplace = True)
	#df.mean_piscina_provincia.fillna(df.mean_piscina_provincia.mean(),inplace = True)
	#df.mean_escuelascercanas_provincia.fillna(df.mean_escuelascercanas_provincia.mean(),inplace = True)
	#df.mean_centroscomercialescercanos_provincia.fillna(df.mean_centroscomercialescercanos_provincia.mean(),inplace = True)
	#df.mean_garages_provincia.fillna(df.mean_garages_provincia.mean(),inplace = True)
	#df.mean_banos_provincia.fillna(df.mean_banos_provincia.mean(),inplace = True)

	#Ciudad mean()
	#df = pd.merge(df, df_mean_por_ciudad, on='ciudad', how='left')
	#df.mean_metroscubiertos_ciudad.fillna(df.mean_metroscubiertos_ciudad.mean(),inplace = True)
	#df.mean_metrostotales_ciudad.fillna(df.mean_metrostotales_ciudad.mean(),inplace = True)
	#df.mean_gimnasio_ciudad.fillna(df.mean_gimnasio_ciudad.mean(),inplace = True)
	#df.mean_usosmultiples_ciudad.fillna(df.mean_usosmultiples_ciudad.mean(),inplace = True)
	#df.mean_piscina_ciudad.fillna(df.mean_piscina_ciudad.mean(),inplace = True)
	#df.mean_escuelascercanas_ciudad.fillna(df.mean_escuelascercanas_ciudad.mean(),inplace = True)
	#df.mean_centroscomercialescercanos_ciudad.fillna(df.mean_centroscomercialescercanos_ciudad.mean(),inplace = True)
	#df.mean_garages_ciudad.fillna(df.mean_garages_ciudad.mean(),inplace = True)
	#df.mean_banos_ciudad.fillna(df.mean_banos_ciudad.mean(),inplace = True)


	df = pd.merge(df, df_time_last_sell,on='id', how='left')
	df = pd.merge(df,df_lujos,on = 'id', how = 'inner')
	df = pd.merge(df, df_fechas_v2,on = 'id', how = 'inner')
	


	return df
