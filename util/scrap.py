from datetime import datetime
import re
from time import sleep
import os
import pandas as pd
from bs4 import BeautifulSoup
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select

def get_html(url, driver):
    try:
        # Load the webpage
        driver.get(url)
        
        # Wait for the table to load
        sleep(1)

        # Locate the select element with the id "segment" 
        select_element = driver.find_element(By.ID, 'segment') 
        # Create a Select object 
        select = Select(select_element) 
        # Change the value of the select element to "2" 
        select.select_by_value('2') 

        sleep(1)
        
        # Get page source
        html_content = driver.page_source
       
        print("HTML content fetched successfully")
        return html_content
    
    except Exception as e:
        print(f"Error occurred while fetching the URL: {url}. Error: {e}")
        return None

def scrap_html(url, datenow):
    try:
        # Set up headless Chrome browser
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
     
        #chrome_service = Service(os.getcwd() + "\\chromedriver.exe") # CHANGE THIS IF NOT SAME FOLDER
        chrome_service = Service("/usr/local/bin/chromedriver-linux64/chromedriver")
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        # Get HTML content
        html_doc = get_html(url, driver)
        data = []
        headers = []

        while True:
            if html_doc is None:
                raise ValueError("No HTML content found")

            # Parse the HTML content
            soup = BeautifulSoup(html_doc, 'html.parser')

            # Find the table
            table = soup.find('table', {'class': 'table'}) 
            if table is None:
                raise ValueError("No table found in the HTML content")

            # Rewrite the headers 
            headers = ['Setor', 'Codigo', 'Acao', 'Tipo', 'Quant. Teorica', 'Part. Carteira', 'Part. Setor']

            # Extract table rows 
            for row in table.find_all('tr')[2:]: 
                # Skip the header rows 
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols] 
                if cols: 
                    data.append(cols)

            #Go to next page
            try:
                next_button = driver.find_element(By.XPATH, '//li[@class="pagination-next"]/a[@aria-label=" page"]')
                next_button.click()

                # Wait for the next page to load
                sleep(1)

                # Get page source
                html_doc = driver.page_source
            except:
                break

        #If no data found, raise an error
        if len(data) == 0:
            raise ValueError("No data found in the HTML content")
        
        #Search date in h2
        h2_text = soup.find('h2').get_text() 
        date_pattern = re.compile(r'\d{2}/\d{2}/\d{2}') 
        date_str = date_pattern.search(h2_text).group()
        if date_str is not None:
            #String to datetime
            date_obj = datetime.strptime(date_str, '%d/%m/%y')
            datenow = date_obj.strftime('%Y%m%d')

        # Create a DataFrame
        df = pd.DataFrame(data, columns=headers)

        # Insert the 'data' column
        df['data'] = datenow

        print(df)

        # Save DataFrame to Parquet format in memory
        parquet_buffer = BytesIO()
        df.to_parquet(parquet_buffer, engine='pyarrow')
        parquet_buffer.seek(0)

        return parquet_buffer, datenow

    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()