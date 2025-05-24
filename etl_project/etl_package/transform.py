from .extract_inquirer import extract_inquirer
from .extract_gma import extract_gma
from .news_keyword import news_keywords
import pandas as pd 
import datetime as dt
import os 

now = dt.datetime.today()

def categorize_title(title):
    for keyword, category in news_keywords.items():
        if keyword.lower() in title.lower():
            return category
    return 'Uncategorized'

def transform():
    # Extract and transform Inquirer data
    inquirer_raw = extract_inquirer('https://newsinfo.inquirer.net/')
    inquirer_raw["source"] = 'INQUIRER'
    inquirer_raw["time_scraped"] = now.strftime('%Y-%m-%d %H:%M %p')

    inquirer_raw['post_date'] = pd.to_datetime(
        inquirer_raw['post_date'] + f' {now.year}',
        format='%b %d - %I:%M%p %Y',
        errors='coerce'
    )
    inquirer_raw['category'] = inquirer_raw['title'].apply(categorize_title)

    # Extract and transform GMA data
    gma_raw = extract_gma('https://data.gmanetwork.com/gno/rss/news/nation/feed.xml')
    gma_raw["source"] = 'GMA'
    gma_raw["time_scraped"] = now.strftime('%Y-%m-%d %H:%M %p')
    gma_raw["post_date"] = pd.to_datetime(gma_raw["post_date"]).dt.tz_localize(None)
    gma_raw['category'] = gma_raw['title'].apply(categorize_title)

    # Combine datasets
    cleaned_news_data = pd.concat([inquirer_raw, gma_raw], ignore_index=True)
    return cleaned_news_data


#test = transform()
#print(test)