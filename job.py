from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

unfamiliar_skill = input('Enter skills you are not familiar with: ')
# unfamiliar_skills_list = unfamiliar_skills.split(',')

# print(unfamiliar_skills_list)
def find_jobs():
    html_get_confirmation = requests.get(url) 
    html_text = html_get_confirmation.text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', 'sim-posted').span.text
        if 'few' in published_date:
            position = job.find('h2').text.replace(' ', '')
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                file_path = f'Posts/{index}.txt'
                with open(file_path, 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Position: {position.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'More Info: {more_info} \n')
                print(f'File saved as {file_path}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'{time_wait}min before each refresh...')
        time.sleep(time_wait * 60)