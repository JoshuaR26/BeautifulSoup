from bs4 import BeautifulSoup

with open('home.html', 'r') as file:
    content = file.read()
    # print(type(content))

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    # print(type(soup))

    course_cards = soup.find_all('div', class_='card')
    # print(course_cards)

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')
    