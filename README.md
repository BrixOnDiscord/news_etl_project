# Philippines News ETL Pipeline

## Overview
This project implements an ETL pipeline that scrapes news articles from **Philippine Daily Inquirer** and **GMA News Online**, processes the data, and exports it into a structured CSV file. The pipeline handles extraction, data cleaning, enrichment, and storage.

## Technologies Used
- Python
- BeautifulSoup 
- Pandas 

## Project Motivation
This project was created to apply and reinforce foundational data engineering skills, particularly web scraping, data transformation, and data pipeline development. It serves as a hands-on learning experience and portfolio piece.

## Features
- Extracts article titles, publication dates, and links from selected Philippine news sources.
- Cleans and structures raw HTML content.
- Saves processed data into a CSV file for further analysis or archival.

## Scope and Limitations
The original plan was to orchestrate the pipeline using Apache Airflow on a 12-hour schedule. However, this approach was dropped because the source websites do not provide precise timestamps in their `post_date` fields. This causes issues in the code logic and risks generating inaccurate data if enrichment is attempted using fallback methods like `fillna`. Without reliable datetime values, it's not possible to guarantee data consistency across runs.

## License
This project is intended for educational purposes and personal portfolio use.

**Built by Brix — for learning, growth, and practical application.**
