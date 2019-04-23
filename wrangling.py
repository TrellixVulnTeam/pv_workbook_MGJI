import pandas as pd
a7 = pd.read_csv('a7_plantview.csv', index_col = 0)
df = pd.DataFrame(a7)

# function that exports data to json
# def export(df):
#     print("Exporting data to JSON")
#     with open('a7.json', 'w') as f:
#         f.write(df.to_json(orient='records', lines=True))
# export(df)
print("Alamo 7 production values for April 10, 2019 \n")
print(df['Actual AC Power (kW)'])
