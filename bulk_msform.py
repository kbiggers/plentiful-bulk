from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(executable_path='/home/krbiggers/plentiful-bulk/chromedriver-linux64/chromedriver'))
driver.get("https://forms.office.com/pages/responsepage.aspx?id=JmyNf_3iYUy8W1ZmqX1jShnGxDcxrjJMv3HeYbIZNHxUQTlRVDZYQjZOQkFROEhXVjNVWVhWRUlKMi4u&route=shorturl")
elem = driver.find_element(By.CLASS_NAME, "-bT-50")
elem.click()
elem.select_by_value("Mixteca")
assert "No results found." not in driver.page_source
driver.close()