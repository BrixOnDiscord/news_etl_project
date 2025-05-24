from .extract_inquirer import extract_inquirer
from .extract_gma import extract_gma
from .transform import transform
from .news_keyword import news_keywords
import pandas as pd 

cleaned_news_data = transform()

def load_csv(filepath):
    cleaned_news_data.to_csv(filepath)
    pass
#load_csv('news_data.csv')