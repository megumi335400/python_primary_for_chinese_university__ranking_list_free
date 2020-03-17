from bs4 import BeautifulSoup
import  requests 
import bs4

def getHTMLText(url):
    r=requests.get(url,headers={'user-agent':'Mozilla/5.0'})
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    return r.text


def fillUnivList(uList,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            uList.append([tds[0].string,tds[1].string,tds[3].string])
    return uList
            

    

def printUnivList(uList,num):
        for i in range(num):
            u=uList[i]
            print(u[0],u[1],u[2])
    

def main():
    url = 'http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html'
    uinfo=[]
    html = getHTMLText(url)
    newList=fillUnivList(uinfo,html)
    printUnivList(newList,5)
    #print(newList)

main()


