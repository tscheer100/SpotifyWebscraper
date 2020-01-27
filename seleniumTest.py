from selenium import webdriver
import requests
import bs4



login = open('login.txt','r')

user = login.readline()
password = login.readline()

driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver.get("https://accounts.spotify.com/en/status")


driver.find_element_by_id("login-btn-link").click()
driver.find_element_by_class_name("btn-facebook").click()

driver.find_element_by_id("email").send_keys(user)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_id("loginbutton").click()

print(driver.title)
print(driver.current_url)


driver.get("https://open.spotify.com/collection/tracks")

res = requests.get("https://open.spotify.com/collection/tracks")
soup = bs4.BeautifulSoup(res.text, 'html.parser')

songs = soup.find_all("div", class_="tracklist-name")
artists = soup.find_all("a", class_="tracklist-row__artist-name-link")

print(songs)
"""for div in songs:
    print(div.text)

for a in artists:
    print(a.text)
"""

driver.quit

