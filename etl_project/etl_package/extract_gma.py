import requests
import pandas as pd 
from bs4 import BeautifulSoup

def extract_gma(gma_news_site):

    url = gma_news_site

    headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/114.0.0.0 Safari/537.36"
            )
        }

    response = requests.get(url, headers=headers)
    response_html = response.text 

    soup = BeautifulSoup(response_html, "xml")
    items = soup.find_all("item")


    gma_data = []

    for i, item in enumerate(items):
        title = item.title.get_text(strip=True)
        pub_date = item.pubDate.get_text(strip=True)
        link = item.link.get_text(strip=True)

        gma_data.append({
            'title': title,
            'post_date': pub_date,
            'link': link
        })

    df = pd.DataFrame(gma_data)
    return df


#test = extract_gma('https://data.gmanetwork.com/gno/rss/news/nation/feed.xml')
#print(test)