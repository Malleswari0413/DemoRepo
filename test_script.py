from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver (Assuming you have ChromeDriver installed)
driver = webdriver.Chrome()

# Open a website
driver.get("http://example.com")

# Perform actions on the website
print(driver.title)
driver.quit()
