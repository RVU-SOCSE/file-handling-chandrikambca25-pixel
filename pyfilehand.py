Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> # Read CSV file
>>> df = pd.read_csv('C:/Users/RVUW268/OneDrive/Desktop/5prog_1experience.csv')
>>> print("Full Data:")
Full Data:
>>> print(df)
   YearsExperience
0              1.1
1              1.3
2              1.5
3              2.0
4              2.2
5              2.9
6              3.0
7              3.2
8              3.2
>>> rows, cols = df.shape
>>> print("\nNumber of rows:", rows)

Number of rows: 9
>>> print("Number of columns:", cols)
... 
Number of columns: 1
>>> print("\nLength of dataframe:", len(df))

Length of dataframe: 9
>>> print("\nFirst 2 rows:")

First 2 rows:
>>> print(df.head(2))
   YearsExperience
0              1.1
1              1.3
