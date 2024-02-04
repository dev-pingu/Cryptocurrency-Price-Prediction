from overall import *
from libraries import *

choice=-1
while choice !=0:
    print("Enter:\n 0) To exit \n 1) reset data list.\n 2) Run scraper for USDT.\n 3) Run scraper for BTC.\n 4) Run scraper for ETH\n 5) Run scraper for BNB\n 6) Display dataset")
    try:
        choice=int(input("Enter choice:"))
    except:
        print("Enter valid input please!")
    if choice==1:
        datareset()
    elif choice==2:
        Scraper(urlUSDT,urlUSDT2,int(input("Enter number of epochs:")),"USDT")
    elif choice==3:
        Scraper(urlBTC,urlBTC2,int(input("Enter number of epochs:")),"BTC")
    elif choice==4:
        Scraper(urlETH,urlETH2,int(input("Enter number of epochs:")),"ETH")
    elif choice==5:
        Scraper(urlBNB,urlBNB2,int(input("Enter number of epochs:")),"BNB")
    elif choice==6:
        print(pd.read_csv("main/data.csv"))
    elif choice!=0:
        print("Enter valid input.")
    

    
