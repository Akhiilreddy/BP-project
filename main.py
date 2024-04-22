import requests
import re
import sqlite3
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://myneta.info/andhrapradesh2019/index.php?action=summary&subAction=crime&sort=liabi'