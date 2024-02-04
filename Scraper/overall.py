from libraries import *

urlBNB="https://crypto.com/price/bnb" 
urlBTC="https://crypto.com/price/bitcoin"
urlETH="https://crypto.com/price/ethereum"
urlUSDT="https://crypto.com/price/tether"

def Scraper(url,num,coin_name):
    for _ in range(num):
        try:
            res,List=get(url),[coin_name]
        except:
            print("Connection Error!")
        soup=BeautifulSoup(res.content,'html.parser')
        #Current Price
        container_11=soup.find_all('div',{"class":"chakra-stack css-a9porv"})
        container_12=container_11[0].find("h2").find("span")
        List.append(str(container_12))
        #Market Cap(USD_Billion)
        container_21=soup.find_all('div',{"class":"css-95687q"})
        container_22=container_21[0].find_all("p")
        List.append(str(container_22))
        #24H Volume(USD_Billion)
        container_23=container_21[1].find_all("p")
        List.append(str(container_23))
        #Circulating supply(USD_Billion)
        container_41=soup.find_all('div',{"class":"css-8l88pi"})
        container_42=container_41[0].find_all("p")
        List.append(str(container_42))
        Writer(List)
        time.sleep(2)
