%pip install xlrd openpyxl
import pandas as pd

from pyodide.http import pyfetch
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())


await download(filename, "Product-sales.csv")


df = pd.read_csv("Product-sales.csv")
print("Printing the csv file")
print(df.head())
# Read data from Excel File and print the first five rows

xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'

await download(xlsx_path, "Product-sales.xlsx")
df = pd.read_excel("Product-sales.xlsx")
print("Printing the .xlsx file")
print(df.head())
x = df[['Quantity','Product','Price']]
type(x)
df.iloc[0,1]
df.iloc[0,0]
print(df.loc[1,"Product"])
print(df.loc[2,"OrderDate"])
print(df.iloc[0:2,0:3])
print(df.loc[0:2,"OrderID":"Category"])

q = df[["Price"]]
print(q)

q = df[["Product","Category"]]
print(q)

print(df.iloc[[1,2]])
