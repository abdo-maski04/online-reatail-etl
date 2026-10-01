import pandas as pd

def transform_dataOne(df):
    # on supprimes les lignes avec des valeurs manquantes soit pour description soit customerId
    df=df.dropna()
    # on supprimes les doublons
    df=df.drop_duplicates(keep='first')
    # on ajout un colonne total_price=Quantty*UnitPrice
    df["totalPrice"]=df["Quantity"]*df["UnitPrice"]
    # on supprime les lignes ayant un quantity négatif et prix unitaire == 0
    df=df[(df["Quantity"]>0) & (df["UnitPrice"]!=0)]
    # on corrige les types
    df["InvoiceNo"]=df["InvoiceNo"].astype(str)
    df["Description"]=df["Description"].astype(str)
    df["StockCode"]=df["StockCode"].astype(str)
    df["CustomerID"]=df["CustomerID"].astype(int)
    return df

# la différnece entre les deux fonctions est que la fonction transform_dataTwo ne supprime pas les lignes avec un quantity négatif, elle supprime seulement les lignes avec un prix unitaire égal à 0.
def transform_dataTwo(df):
    # on supprimes les lignes avec des valeurs manquantes soit pour description soit customerId
    df=df.dropna()
    # on supprimes les doublons
    df=df.drop_duplicates(keep='first')
    # on ajout un colonne total_price=Quantty*UnitPrice
    df["totalPrice"]=df["Quantity"]*df["UnitPrice"]
    # on supprime les lignes ayant un quantity négatif et prix unitaire == 0
    df=df[df["UnitPrice"]!=0]
    # on corrige les types
    df["InvoiceNo"]=df["InvoiceNo"].astype(str)
    df["Description"]=df["Description"].astype(str)
    df["StockCode"]=df["StockCode"].astype(str)
    df["CustomerID"]=df["CustomerID"].astype(int)
    return df

def extract_revenue(df):
    revenues=df[df["InvoiceNo"].str.startswith(("C"),na=False)]
    revenues=transform_dataTwo(revenues)
    return revenues
