# Import a library to fetch web content using HTTP requests.
import requests

# Import a library to parse the HTML content of web pages.
from bs4 import BeautifulSoup

import pandas as pd

# Use a snapshot of http://www.bcsfootball.org/ taken on December 8th, 2013.
URL = "http://web.archive.org/web/20131208113724/http://www.bcsfootball.org/"

# Get the HTML content of the web page as a string.
content = requests.get(URL).content

# Use a BeatifulSoup object to parse the HTML with "html.parser".
soup = BeautifulSoup(content, "html.parser")

# Find all <tr> elements (table rows) in the <tbody>
# of the <table class="mod-data"> element.
rows = soup.select('table.mod-data tbody tr')

# Extract the text in each cell and put into a list of lists,
# such that each list in the list represents content in a row.
table_lst = []
for row in rows:
    cell_lst = [cell.text for cell in row]
    table_lst.append(cell_lst)

ranking = pd.DataFrame(table_lst)
ranking.columns = ['ranking', 'state', 'score']
print ranking.head()
