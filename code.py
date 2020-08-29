from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import numpy
import re
import time

start = time.time()
url = 'https://venmurasu.in/mutharkanal/chapter-1'
#url = 'https://venmurasu.in/muthalaavin/chapter-10'
f = open("data.txt", 'r', encoding='utf-8')
li = list(f.read().split('\n'))
f.close();
f = open("data.txt", 'w', encoding='utf-8')
nextlink='1'
while(nextlink):
    client = ureq(url)
    pagehtml = client.read()
    client.close()
    pagesoup = soup(pagehtml, "html.parser")
    containers = pagesoup.findAll("div", {"class": "content"})
    paras = containers[0].find_all('p')
    words = ""
    for j in range(len(paras)):
        words = str(paras[j].text)
        li.extend(re.split('…|”|[.,;# ?\=]| ',words))

    nextlink = pagesoup.findAll("a", {
        "class": "flex items-center ml-auto text-ui-primary font-bold px-4 py-2 border border-ui-border rounded-lg hover:bg-ui-primary hover:text-white transition-colors"})
    if(nextlink):
        url = "https://venmurasu.in" + str(nextlink[0].attrs['href'])
arr = numpy.asarray(li)
li = sorted(arr, key=len, reverse=True)
del li[10:]
f.write("Top 10 Longest words:\n")
for i in li:
    print(len(i), '*', i, '\n')
    f.write("Word: "+i + " Length:"+str(len(i))+"\n")

f.close()
end = time.time()
print("Time-taken: ",end="")
print(f"{end - start}")

