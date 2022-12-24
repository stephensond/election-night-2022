import pandas as pd
 
renamed_columns = {
 'mean_netpartymargin': 'net',
 'voteshare_mean_D1': 'D vote',
 'voteshare_mean_R1': 'R vote',
 'name_D1': 'D',
 'name_R1': 'R'
}
 
columns_to_get = ['district', 'net', 'D', 'D vote', 'R', 'R vote']
 
def filter_df_competitive(df):
 return df.loc[(df['forecastdate'] == '11/8/22')
   & (df['expression'] == '_deluxe')
   & (df['net'] > -10)
   & (df['net'] < 10)]
 
def filter_df_all(df):
 return df.loc[(df['forecastdate'] == '11/8/22')
   & (df['expression'] == '_deluxe')]
 
 
# get house predictions
df_house = pd.read_csv("input/house_district_toplines_2022.csv")
df_house = df_house.rename(columns=renamed_columns)

# get the median house seat
df_house = filter_df_all(df_house)
df_house = df_house.sort_values(by='net')
df_house = df_house.reset_index()
print(f"median seat: {df_house.iloc[217]['district']}")
df_house.to_csv("output/house_all.csv", columns = columns_to_get, index = False, float_format = "%.1f")

df_house = df_house.sort_values(by='district')
df_house.to_csv("output/house_by_state_all.csv", columns = columns_to_get, index = False, float_format = "%.1f")
 
df_house = filter_df_competitive(df_house)
df_house = df_house.sort_values(by='net')
df_house.to_csv("output/house_competitive.csv", columns = columns_to_get, index = False, float_format = "%.1f")
 
df_house = df_house.sort_values(by='district')
df_house.to_csv("output/house_by_state_competitive.csv", columns = columns_to_get, index = False, float_format = "%.1f")
 
 
# get senate predictions
df_senate = pd.read_csv("input/senate_state_toplines_2022.csv")
df_senate = df_senate.rename(columns=renamed_columns)
df_senate = df_senate.sort_values(by='net')

df_senate = filter_df_all(df_senate)
df_senate.to_csv("output/senate_all.csv", columns = columns_to_get, index = False, float_format = "%.1f")

df_senate = filter_df_competitive(df_senate)
df_senate.to_csv("output/senate_competitive.csv", columns = columns_to_get, index = False, float_format = "%.1f")
 
 
# get governor predictions
df_gov = pd.read_csv("input/governor_state_toplines_2022.csv")
df_gov = df_gov.rename(columns=renamed_columns)
df_gov = df_gov.sort_values(by='net')

df_gov = filter_df_all(df_gov)
df_gov.to_csv("output/gov_all.csv", columns = columns_to_get, index = False, float_format = "%.1f")

df_gov = filter_df_competitive(df_gov)
df_gov.to_csv("output/gov_competitive.csv", columns = columns_to_get, index = False, float_format = "%.1f")
