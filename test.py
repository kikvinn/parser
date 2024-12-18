import requests
import datetime
from bs4 import BeautifulSoup



def parse_html(url: str):
    r = requests.get(url)
    return r.text

def parse_timetable(name: str):
    html = parse_html(f"https://sirus.su/base/character/x5/{name}/")
    soup = BeautifulSoup(html, 'html.parser')
    
    contents = []
    with open('test.html', 'w') as f:
        f.write(str(soup))
    

contents = parse_timetable("pivogumengo") 
