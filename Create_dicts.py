import pandas as pd

df_interventions = pd.read_csv("Table.csv",sep=';')

slopes = df_interventions.Slope.unique()
locations = df_interventions.Location.unique()
beds = df_interventions.Bed.unique()
widths = df_interventions.Width.unique()

df_interventions.set_index(["Slope", "Location", "Bed", "Width"], inplace=True)
interventions_dict = df_interventions.to_dict(orient='index')

#####
df_info = pd.read_csv("intervention_info.csv",sep=';')
df_info.set_index(["Interventions"],inplace=True)
info_dict = df_info.to_dict(orient='index')
