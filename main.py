from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# URL of the wikipedia page
url = "https://www.allmusicals.com/lyrics/hamilton/script.htm"

# Using Selenium to get the text of the page, then putting it into a beautiful soup object
driver = webdriver.Chrome()
driver.get(url)
soup = BeautifulSoup(driver.page_source, "html.parser")

driver.close()

# Seperating every word and putting it into a list
words = soup.get_text().lower().split()

# Sorting the list alphanumericly
words = sorted(words)

# Formatting the output
out = ""
for word in words:
    out += word + " "

print(out)