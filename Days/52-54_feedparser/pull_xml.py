import requests

URL = "http://store.steampowered.com/feeds/newrelease.xml"

if __name__ == '__main__':
    r = requests.get(URL)
    with open("newreleases.xml", "wb",) as f:
        f.write(r.content)