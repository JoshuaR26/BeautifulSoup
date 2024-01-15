from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

html_get_confirmation = requests.get(url) 
# print(html_get_confirmation)

html_text = html_get_confirmation.text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
# print(soup)

job = soup.find('li', class_= 'clearfix job-bx wht-shd-bx')
# for job in jobs:
company = job.find('h3', class_='joblist-comp-name').text.replace(' T', '')
print(company)