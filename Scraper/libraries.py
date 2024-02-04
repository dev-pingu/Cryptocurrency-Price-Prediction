from bs4 import BeautifulSoup
from requests import get
import datetime
import time
import pandas as pd

def datareset():
    with open('data.csv','w') as f:
        f.write("Coin_name,Current_price,Market_Cap(USD_Billion),24H_Volume(USD_Billion),Circulating_supply(USD_Billion),Date(dd/mm/yyyy)\n")
        f.flush()
        pass
def value_extractor(s):
    for i in range(len(s)):
        if s[i]=='>':
            if s[i+1]=="$":
                s=s[i+2:]
            else:
                s=s[i+1:]
            break
    for i in range(len(s)):
        if s[i]==",":
            s=s[:i]+s[i+1:]
        if s[i]==" ":
            s=s[:i]
            break
        if s[i]=="<":
            s=s[:i]
            break
    """s=list(s).remove(",")
    s="".join(s)"""
    return s
def Writer(List):
    with open('data.csv','a') as f:
        c_time = datetime.datetime.now()
        t = str(c_time.day) + '/' + str(c_time.month) + '/' + str(c_time.year)
        f.write(List[0]+ ",")
        List=List[1:]
        for i in range(len(List)-1):
            f.write(value_extractor(List[i])+",")
        f.write(value_extractor((List[len(List)-1])))
        f.write(', ')
        f.write(t)
        f.write("\n")
        f.flush()
