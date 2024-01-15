from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

unfamiliar_skill = input('Enter skills you are not familiar with: ')

html_get_confirmation = requests.get(url) 

html_text = html_get_confirmation.text

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date = job.find('span', 'sim-posted').span.text
    if 'few' in published_date:
        position = job.find('h2').text.replace(' ', '')
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', 'srp-skills').text.replace(' ','')
        more_info = job.header.h2.a['href']

        if unfamiliar_skill not in skills:
            print()
            print(f'Position: {position.strip()}')
            print(f'Company Name: {company_name.strip()}')
            print(f'Required Skills: {skills.strip()}')
            print(f'More Info: {more_info}')
            print()