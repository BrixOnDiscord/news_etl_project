from etl_package.extract_gma import extract_gma
from etl_package.extract_inquirer import extract_inquirer
from etl_package.transform import transform
from etl_package.load import load_csv
import pandas as pd 

raw_gma = extract_gma("https://data.gmanetwork.com/gno/rss/news/nation/feed.xml")
raw_inquirer = extract_inquirer("https://www.inquirer.net/")

cleaned_data = transform()

load_csv('cleaned_news.csv')