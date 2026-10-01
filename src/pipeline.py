from extract import extract_data
from transform import transform_dataOne,transform_dataTwo,extract_revenue
from load import load_data

# extract data from the excel file
df=extract_data("data/raw/Online Retail.xlsx")

# copy data for having the original version of the data
db=df.copy()

# fusion of the two dataframes sales and revenues with apply of many transformation operations on the dataframes
sales=transform_dataOne(db)
revenues=extract_revenue(db)

# load of data
load_data(sales,"sales")
load_data(revenues,"revenues")