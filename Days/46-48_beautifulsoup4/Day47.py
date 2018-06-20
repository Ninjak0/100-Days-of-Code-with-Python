import bs4
import requests

site = requests.get("https://pybit.es/pages/articles.html")
site.raise_for_status()

soup = bs4.BeautifulSoup(site.text, "html.parser")

all_li = soup.main.find_all("li")

for item in all_li:
    print(item.string)