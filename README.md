# Optical-Scrape-

This project involves developing a Python script that utilizes Beautiful Soup and Google Cloud Console to scrape the Sunglass Hut website. The primary objective of this script is to monitor the site for new sunglasses arrivals and send email alerts whenever new products are in stock. This tool is designed to help businesses stay competitive by keeping them updated on the latest product offerings from Sunglass Hut.

Features
Web Scraping: Uses Beautiful Soup to extract product information from the Sunglass Hut website.
Google Cloud Console Integration: Employs Google Cloud Console for secure email notifications using OAuth 2.0 authentication.
Email Alerts: Automatically sends email notifications about new product arrivals to keep users informed.
Data Storage: Stores previously scraped data to compare and identify new products.
Regular Monitoring: Scheduled to check the website periodically for new products.


Technologies Used
Python: Core programming language used for the script.
Beautiful Soup: Library for web scraping to parse HTML and extract product information.
Google Cloud Console: Utilized for secure OAuth 2.0 authentication to send email alerts.
SMTP: Simple Mail Transfer Protocol used for sending email notifications.
JSON: For data storage and comparison of previously scraped data.
