import requests
import re
import sqlite3
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://myneta.info/andhrapradesh2019/index.php?action=summary&subAction=crime&sort=liabi'

# Send a GET request to the URL and fetch the HTML content
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

content = response.content.decode('utf-8')

# Define regular expressions to match the data in the table
row_pattern = r'<tr[^>]*>(.*?)<\/tr>'
cell_pattern = r'<td[^>]*>(.*?)<\/td>'

#DB
conn = sqlite3.connect('ap_data.db')
cursor = conn.cursor()

    # Create a table to store the candidate data
cursor.execute('''
        CREATE TABLE IF NOT EXISTS criminal_cases (
            Sno VARCHAR,
            Candidate VARCHAR,
            Constituency VARCHAR,
            Party VARCHAR,
            Criminal_Cases VARCHAR,
            Education VARCHAR,
            Total_Assets VARCHAR,
            Liabilities VARCHAR
        )
    ''')