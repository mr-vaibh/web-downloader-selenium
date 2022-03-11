from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL_TO_WEBSITE = 'https://getintopc.com/softwares/sony-vegas-pro-2020-free-download/'
DOWNLOAD_BTN_XPATH = '//*[@id="post-181405"]/div[1]/form/div/button'

driver.get(URL_TO_WEBSITE)

downloadBtn = driver.find_element(by=By.XPATH, value=DOWNLOAD_BTN_XPATH)
downloadBtn.send_keys(Keys.ENTER)
