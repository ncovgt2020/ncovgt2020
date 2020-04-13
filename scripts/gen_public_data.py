import pandas as pd 
import numpy as np 


pacientes_full_dir = "../data/pacientes_full.csv"
pacientes_save_dir = "../data/pacientes.csv"
resumen_dir = "../data/resumen_casos.csv"
resumen_save_dir_kaggle = "../../covid19_guatemala/case_summary.csv"
pacientes_save_dir_kaggle = "../../covid19_guatemala/patients.csv"

df = pd.read_csv(pacientes_full_dir, header = 0, parse_dates = True)
df.drop(columns = ['lugar_deteccion','deteccion_lat','deteccion_lon','ubicacion_actual','lat','lon','ISO_31662_Code'], inplace = True)
print("Data local: EXITO")
df.to_csv(pacientes_save_dir,sep=",", na_rep="", index = False)
df.columns = ['id', 'sex', 'birth_date', 'age', 'country', 'department', 'illness', 'group', 'infection_cause', 'arrival_date', 'infected_by', 'symptom_start_date', 'confirmation_date', 'recovery_date', 'deceased_date', 'status', 'source']

cols = df.columns

for col in cols:
	a = df[col]
	for j,el in enumerate( a):
		if type(el) == str:
			if el =='desconocido':
				df.loc[j,col] = 'unknown'



df.to_csv(pacientes_save_dir_kaggle,sep=",", na_rep="", index = False)
print("Data pacientes Kaggle: EXITO")
df = pd.read_csv(resumen_dir, header = 0, parse_dates = True)
df.columns = ['date', 'confirmed','recovered','deceased','source']
df.to_csv(resumen_save_dir_kaggle, sep=",", na_rep = "",index = False)
print("Data resumen Kaggle: EXITO")
