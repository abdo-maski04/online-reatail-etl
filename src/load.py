import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

#extract vlues from the .env file
user_db=os.getenv("user_db")
user_password=os.getenv("user_password")
db_host=os.getenv("db_host")
db_port=os.getenv("db_port")
db_name=os.getenv("db_name")

def load_data(df,table_name):
    engine=create_engine(f"postgresql://{user_db}:{user_password}@{db_host}:{db_port}/{db_name}")
    df.to_sql(table_name,engine,if_exists="replace",index=False)

