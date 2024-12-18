import requests
import datetime
from bs4 import BeautifulSoup

# https://timetable.marsu.ru/timetable/web/timetable/group?group=897&week=202452

GROUP : int = 897


def weeks(day: tuple) -> str:
    """
        Args:
            day: tuple - (year, month, day)
        Return:
            year+week_number: str - "yearweek"
    """
    a = datetime.datetime(*day).isocalendar()
    return f"{a.year}{a.week}"

def parse_html(url: str):
    r = requests.get(url)
    return r.text

def parse_timetable(date: tuple, group: int):

    timetable = []

    week = weeks(date)
    html = parse_html(f"https://timetable.marsu.ru/timetable/web/timetable/group?group={group}&week={week}")
    soup = BeautifulSoup(html, 'html.parser')
    day = soup.find_all('li', class_ = 'schedule__day')
    for i in day:
        sh_date = i.find('div', class_ = 'schedule__date').get_text(strip=True)
        lessons = []
        for j in i.find_all('li', class_ = 'lesson'):
            times = j.find('div', class_ = 'times').get_text(strip=True)
            subject = j.find('div', class_ = 'subject').contents[0].strip()
            location = j.find('div', class_ = 'location').get_text(strip=True)
            lessons.append({'date': sh_date, 'times': times, 'subject': subject, 'location': location})
        timetable.append(lessons)
    return timetable

print(parse_timetable((2024, 12,18), GROUP)[0])