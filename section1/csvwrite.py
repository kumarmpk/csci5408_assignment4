# Load the Pandas libraries with alias 'pd'
import pandas as pd
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("pika.csv")
# Preview the first 5 lines of the loaded data
# print(data.head())
col1 = data["hmdy"]
col2 = data["hmax"]
col3 = data["hmin"]
joined_list = [*col1, *col2,*col3]
myset = set(joined_list)
finalist = list(myset)
my_df = pd.DataFrame(finalist)
my_df.to_csv("humidity.csv",header=['humidity'],index=True,index_label="Key")