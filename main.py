from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.mongolbank.mn/default.aspx")
elem = driver.find_element(By.ID, "ContentPlaceHolder1_lblUSD")
text = elem.get_attribute('innerText')
print(text)
driver.close()
