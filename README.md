# Domain Search Automation Script

This Python script uses Selenium to automate the process of searching for available domain names on Namecheap. It checks a list of domain names, searches for them on Namecheap, and retrieves information about whether the domain is available, along with its price.

## Features
- Searches multiple domain names sequentially.
- Automatically checks domain availability and retrieves the domain name and price.
- Stops further searches once an available domain is found for each query.
- Uses Selenium WebDriver for interaction with the Namecheap website.

## Requirements
- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (for Chrome browser)
  
### Install Required Packages
To install the necessary Python packages, use the following command:

```bash
pip install selenium
