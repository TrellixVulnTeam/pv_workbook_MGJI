import pandas as pd
events = pd.read_csv('jspevents.csv', index_col = 0)
df = pd.DataFrame(events)
print(df.iloc[[1,2,3],[0]])
