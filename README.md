# E-Commerce Product Scraper

## Overview
This project is a web scraper built using **Scrapy** and **Selenium** to collect product data from an e-commerce platform. It automatically navigates through search result pages and extracts details such as product names, prices, and ratings. The scraped data is stored in a CSV file for further analysis.

In this project, we used "football" as a search term to gather data on related products, and successfully collected 163 items, which are saved in the CSV output.

## Features
- Automated scraping of product details (name, price, rating) across multiple pages
- Handles dynamic content and rotating user agents
- Outputs results in a structured CSV format
- Built-in pagination support for retrieving data from multiple pages of search results

## Requirements
To run this scraper, make sure to have the following installed:
- Python 3.x
- Scrapy
- Selenium
- WebDriver (e.g., ChromeDriver)

You can install the required libraries using:

```bash
pip install selenium
pip install scrapy

