---- About ProcDNA ----

ProcDNA is a global consulting firm that provides commercial analytics and technology solutions for healthcare companies. They use design thinking and technology to create solutions for their clients. Some of their services include: 
 
Commercial analytics: ProcDNA helps clients improve their commercial effectiveness. 
 
Patient analytics: ProcDNA helps clients improve patient adherence and understand reasons for patient abandonment. 
 
Managed markets: ProcDNA helps clients with managed markets. 
 
Technology solutions: ProcDNA provides technology solutions to clients. 
 
---- About Project ----

 ProcDNA Web Scraper

## Project Overview

The ProcDNA Web Scraper is a Python-based web scraping tool designed to extract and save data from various sections of the ProcDNA website. This project uses BeautifulSoup, a popular library for web scraping, to parse HTML content and retrieve specific information from pages related to Analytics, Technology, Data Science, Case Studies, Articles, and News. The extracted data is then saved in a text file for further analysis or reporting.

## Features

- **Analytics**: Scrapes headings and descriptions from the Analytics page.
- **Technology**: Extracts headings and descriptions from the Technology page.
- **Data Science**: Retrieves headings and descriptions from the Data Science page.
- **Case Studies**: Gathers headings, serial numbers, and descriptions from the Case Studies page.
- **Articles**: Collects headings and descriptions from the Articles page.
- **News**: Pulls time, location, news content, and descriptions from the News page.

## Requirements

- Python 3.x
- BeautifulSoup4
- Requests
- lxml

You can install the required Python libraries using pip:

```bash
pip install beautifulsoup4 requests lxml
