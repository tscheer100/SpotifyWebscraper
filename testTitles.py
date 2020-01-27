
import requests
import bs4


res = requests.get('https://ascienceenthusiast.com/?fbclid=IwAR1LrRJiZYPc0fbCCLxHpgAofgX6Zq8FTo91ptA0tIs0cyJwsaiknG5MT3I')

soup = bs4.BeautifulSoup(res.text, 'html.parser')

titles = soup.find_all("h3", class_="entry-title")


for h3 in titles:
    print(h3.text)


print(titles.get_text())


