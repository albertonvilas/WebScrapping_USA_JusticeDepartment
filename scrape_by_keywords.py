from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import time



def get_info(soup,cat):
    processes = soup.find_all('div', {'class' : 'content-block-item result'})

    info = []
    for elem in processes:
        print(elem.text)
        title = elem.find('h4').text
        link = soup.find('span', {'class' : 'url'}).text
        info.append([title,link,cat])
        #print(title)
        #print(link)
    df = pd.DataFrame(info)
    df.to_csv('main.csv', mode='a', header=False)

categories = ["intellectual property theft","trade secrets","patent infrigement", "trademark","copyright","trade secrets", "economix espionage", "industrial espionage", "cyberattack", "cybercrime"]
i=0
nr_page=0


while i < len(categories[:1]):

    cat = categories[i]
    cat = cat.replace(" ","+")
    cat = cat+"+china"
    print(cat)
    print(nr_page)

    time.sleep(2)
    page = requests.get("https://search.justice.gov/search?affiliate=justice-archive&op=Search&page="+str(1)+"&query="+cat).text
    soup = BeautifulSoup(page, 'lxml')
    pager = soup.find('a', {'class' : 'next_page'})
    get_info(soup,cat)
    if pager:
        nr_page +=1
    else:
        i+=1
        nr_page = 0
        print("end this category")
        time.sleep(10)
        





