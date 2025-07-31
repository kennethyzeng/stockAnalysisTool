#https://www.geeksforgeeks.org/creating-a-dataframe-using-excel-files/
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html

#1 EXcel to DataFrame #########################
import pandas as pd 
  
# Import the excel file and call it xls_file 
excel_file = pd.ExcelFile('pandasEx.xlsx') 
  
# View the excel_file's sheet names 
print(excel_file.sheet_names) 
  
# Load the excel_file's Sheet1 as a dataframe 
df = excel_file.parse('Sheet1') 
print(df)

#2 ########################################################
# import pandas lib as pd
import pandas as pd
 
# read 2nd sheet of an excel file
dataframe2 = pd.read_excel('SampleWork.xlsx', sheet_name = 1)
 
print(dataframe2)

#########################################################
#3   Pandas Read specific Excel cell value into a variable
#Method 1: Using iloc To access the value of a specific cell in the Excel file, you need to specify the row and column indices of the cell. In pandas, you can do this by using the .iloc method.
import pandas as pd
df = pd.read_excel("path/to/your/excel/file.xlsx")
print(df)
#read the value of the first row and first column of the DataFrame
cell_value = df.iloc[0, 0]
#Using loc and at
#Reading cell at row 0, column 'Name'
cell_value = df.loc[0, 'Name']


######################
#4 write someting to sepcific cell in excel 
#https://stackoverflow.com/questions/39805677/write-values-to-a-particular-cell-in-a-sheet-in-pandas-in-python

####5 check dataframe column name 

df3  = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob', 'Alice a Long Name'], # this is a very long name
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
})
x4 = np.random.randn(100, 2)
df4 = pd.DataFrame(x4)

#print datafrmae 
print(df3)

for i, j in enumerate(df3.columns):
      ##print name of column
      print(j)
      #print indext of corresponding column name 
      print(i)
      #print specific column name 
      print(df3.columns[1])
      #print list of columns
      print(list(df3.columns))
      #print keys()
      print(df3.keys())
      #print columns
      for col in df3.columns:
        print(col)

ticker=yf.Ticker('smci')
ticker_content=ticker.income_stmt 
for col in ticker_content.columns:
    print (col)
    if col in list(ticker_content.columns):
         print("yes")
    
print(type(list(ticker_content.columns)))
print(ticker_content.columns.tolist)

#######