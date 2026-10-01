import pandas as pd

def extract_data(file_path):
    df=pd.read_excel(file_path)
    return df