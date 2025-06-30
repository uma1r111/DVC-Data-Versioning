import pandas as pd
import os

# create a sample DataFrame with column names
data={'Name': ['Alice', 'Bob', 'Charlie0'],
      'Age': [25, 30, 35],
      'City': ['New York', 'Los Angeles', 'Chicago']
      }

df=pd.DataFrame(data)

# # adding new row to df for v2
new_row_loc={'Name': 'Selena', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc

# # adding new row to df for v3
new_row_loc2={'Name': 'Bella', 'Age': 30, 'City': 'City2'}
df.loc[len(df.index)] = new_row_loc2

# ensure the "data" directory exists at root level
data_dir='data'
os.makedirs(data_dir, exist_ok=True)

# define the file path
file_path=os.path.join(data_dir, 'sample_data.csv')

# save dataframe to csv file, including column names
df.to_csv(file_path, index=False)

print(f"csv file saved to {file_path}")