import os
import pandas as pd
from bs4 import BeautifulSoup
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_html(url):
    try:
        # Set up headless Chrome browser
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
     
        #chrome_service = Service(os.getcwd() + "\\chromedriver.exe") # CHANGE THIS IF NOT SAME FOLDER)
        chrome_service = Service("/usr/local/bin/chromedriver-linux64/chromedriver")
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        # Load the webpage
        driver.get(url)
        
        # Wait for the table to load
        driver.implicitly_wait(10)
        
        # Get page source
        html_content = driver.page_source
        
        # Close the browser
        driver.quit()
        
        print("HTML content fetched successfully")
        return html_content
    
    except Exception as e:
        print(f"Error occurred while fetching the URL: {url}. Error: {e}")
        return None

def scrap_html(url, datenow):
    try:
        # Get HTML content
        html_doc = get_html(url)
        if html_doc is None:
            raise ValueError("No HTML content found")

        # Parse the HTML content
        soup = BeautifulSoup(html_doc, 'html.parser')

        # Find the table
        table = soup.find('table')
        if table is None:
            raise ValueError("No table found in the HTML content")

        # Extract table headers
        headers = [header.text for header in table.find_all('th')]

        # Extract table rows
        rows = []
        for row in table.find_all('tr'):
            cells = [cell.text.strip() for cell in row.find_all(['td', 'th'])]
            rows.append(cells)

        # Create a DataFrame
        if not rows or len(rows[0]) != len(headers):
            raise ValueError("Mismatch between table headers and rows")

        df = pd.DataFrame(rows[1:], columns=headers)

        # Insert the 'data' column
        df['data'] = datenow

        print(df)

        # Save DataFrame to Parquet format in memory
        parquet_buffer = BytesIO()
        df.to_parquet(parquet_buffer, engine='pyarrow')
        parquet_buffer.seek(0)

        return parquet_buffer

    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")