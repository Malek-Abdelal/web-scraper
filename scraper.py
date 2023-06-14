import requests
from bs4 import BeautifulSoup
import json


URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    all_ele = soup.find_all('sup', class_="noprint")
    counter = 0
    for ele in all_ele:
        if ele.text == "[citation needed]":
            counter += 1
    return counter

def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    all_ele = soup.find_all('sup', class_="noprint")
    Paragraphs = ""
    for ele in all_ele:
        if ele.text == "[citation needed]":
            Paragraphs += f"{ele.parent.text}\n"
    return Paragraphs


print(get_citations_needed_count(URL))
print(get_citations_needed_report(URL))

# data = json.dumps(get_citations_needed_report(URL))
# with open ('result.json','w') as file:
#     file.write(data)