from bs4 import BeautifulSoup
import requests
import csv

tmp = []
url = "https://www.smsupermalls.com/mall-directory/sm-city-davao/information/"
resp = requests.get(url)
html_str = resp.text
soup = BeautifulSoup(html_str, "html.parser")
for i in soup.find_all(class_="brand-description"):
    tmp.append([i.get_text().strip()])
    #print(i.get_text().strip())

with open('SM_city_davao.csv', 'w') as outputFile:
    writer = csv.writer(outputFile)
    writer.writerows(tmp)
