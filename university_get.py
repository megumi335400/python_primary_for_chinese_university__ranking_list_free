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
            
            

    

def printUnivList(uList,num):
    count=0
    with open('list.txt','w',encoding='utf-8') as f:
        for i in range(num):
            u=uList[i]
            print(u[0],u[1],u[2])
            for j in range(len(uList[i])):
                f.write(str(uList[i][j]))
                count=count+1
                if count ==3:
                    count=0
                    f.write('\n')
    f.close()
    

def main():
    url = 'http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html'
    uinfo=[]
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,50)

main()


