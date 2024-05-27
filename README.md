# Hacker News Web Scraping Project

## Overview
This project is a web scraper that targets the popular technology and startup news site, Hacker News. The goal of this project is to filter and identify the most recent news articles that have received the highest number of votes, thereby determining which articles are most worth reading.

## Features
- **Web Scraping**: Utilizes Python to scrape data from Hacker News.
- **Data Filtering**: Filters out articles based on the number of votes they have received.
- **Data Extraction**: Extracts valuable information such as article title, link, and number of votes.

## Data Storage
This project includes a feature to store the scraped data into a CSV file. The CSV file, named 'list_hn.csv', organizes the data into the following columns:
- 'title': The title of the news article.
- 'link': The URL link to the news article.
- 'votes': The number of votes the news article has received.

This CSV file provides an easy way to view and analyze the scraped data. You can open it with any software that can read CSV files, such as Microsoft Excel, Google Sheets, or even a simple text editor.

## How It Works
The web scraper navigates to the Hacker News site, specifically focusing on recent news articles. It then extracts the relevant data (article title, link, and number of votes) and filters this data to only include articles that have received a significant number of votes. This filtered list of articles is then available for further analysis or reading.

## Requirements
- Python 3.x
- Libraries: Beautiful Soup, requests, csv

## Usage
1. Ensure that you have the required software and libraries installed.
2. Run the Python script to start the web scraper.
3. The script will output a list of recent high-vote articles from Hacker News.

## Future Improvements
Future versions of this project may include additional features such as automatic daily or hourly scraping, user-defined vote thresholds, or integration with a front-end interface for easier reading and navigation of articles.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.