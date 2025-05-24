import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract_inquirer(news_site):
    url = news_site

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    response_html = response.text

    soup = BeautifulSoup(response_html, 'html.parser')

    h1_tags = soup.find_all("h1")

    title = []
    link = []
    post_date = []

    for tag in h1_tags:
        a_tag = tag.find("a")
        
        # Try to find date in sibling div with id 'ncg-postdate'
        postdate_div = tag.find_next_sibling('div', id='ncg-postdate')

        # If not found, try other plausible locations or attributes
        if not postdate_div:
            # Try finding a <time> tag near this h1 tag
            postdate_time = tag.find_next('time')
            if postdate_time:
                date_text = postdate_time.text.strip()
            else:
                date_text = None
        else:
            date_text = postdate_div.text.strip()

        if a_tag:
            title.append(a_tag.text.strip())
            link.append(a_tag.get("href"))
            post_date.append(date_text)

    df = pd.DataFrame({
        'title': title,
        'post_date': post_date,
        'link': link
    })

    # Debug print: check extracted dates
    print("Extracted post_date samples:")
    print(df['post_date'].head(10))

    return df
