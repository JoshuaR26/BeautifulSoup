from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

html_get_confirmation = requests.get(url) 
# print(html_get_confirmation)

html_text = html_get_confirmation.text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
# print(soup)

jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date = job.find('span', 'sim-posted').span.text
    if 'few' in published_date:
        position = job.find('h2').text.replace(' ', '')
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        # print(company_name)

        skills = job.find('span', 'srp-skills').text.replace(' ','')
        # print(skills)

        print(f'''
-----------------------------------------------------------
              
Position: {position}
Compant Name: {company_name}
Required Skills: {skills}
Posted: {published_date}
------------------------------------------------------------
    ''')