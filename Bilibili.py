import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--headless')

browser = webdriver.Chrome(chrome_options=options)

browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

browser.get("https://space.bilibili.com/1935882/fans/fans")

time.sleep(30)

for i in range(100):
    nextPage = browser.find_element_by_xpath("//li[contains(@title, '下一页')]/a")
    nextPage.click()
    time.sleep(5)
    print(i)

time.sleep(5)

browser.close