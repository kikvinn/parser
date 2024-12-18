import requests
from datetime import datetime
from bs4 import BeautifulSoup

import locale
locale.setlocale(locale.LC_ALL, "")
# https://timetable.marsu.ru/timetable/web/timetable/group?group=897&week=202452

GROUP : int = 897

def date_convert(date: str):
    #'16 Дек., пн.'
    year = datetime.now().year
    date = datetime.strptime(date[:-6] + f' {year}', '%d %b %Y')
    return date

def parse_html(url: str):
    r = requests.get(url)
    return r.text

def parse_timetable(date: str, group: int):

    timetable = []

    html = parse_html(f"https://timetable.marsu.ru/timetable/web/timetable/group?group={group}&week={date}")
    soup = BeautifulSoup(html, 'html.parser')
    day = soup.find_all('li', class_ = 'schedule__day')
    for i in day:
        locale_date = i.find('div', class_ = 'schedule__date').get_text(strip=True)
        full_date = date_convert(locale_date)
        lessons = []
        for j in i.find_all('li', class_ = 'lesson'):
            times = j.find('div', class_ = 'times').get_text(strip=True)
            subject = j.find('div', class_ = 'subject').contents[0].strip()
            location = j.find('div', class_ = 'location').get_text(strip=True)
            lessons.append({'date': full_date, 'times': times, 'subject': subject, 'location': location})
        timetable.append(lessons)
    return timetable