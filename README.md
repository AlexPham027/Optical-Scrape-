# Optical-Scrape


This project involves developing a Python script that uses Beautiful Soup and Google Cloud Console to scrape the Sunglass Hut website. The goal is to monitor the site for new sunglasses and send email alerts when new products are in stock, helping businesses stay competitive.

## Features

- **Web Scraping**: Extracts product information from the Sunglass Hut website using Beautiful Soup.  
- **Google Cloud Console Integration**: Utilizes Google Cloud Console for secure email notifications with OAuth 2.0 authentication.  
- **Email Alerts**: Sends notifications about new product arrivals.  
- **Data Storage**: Compares newly scraped data with previously stored data to identify new products.  
- **Regular Monitoring**: Scheduled checks for new products at regular intervals.

## Technologies Used

- **Python**: Core programming language.
- **Beautiful Soup**: For parsing HTML and extracting product data.
- **Google Cloud Console**: For OAuth 2.0 authentication and secure email sending.
- **SMTP**: For sending email notifications.
- **JSON**: For data storage and comparison.
