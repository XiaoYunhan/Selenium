import random
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

browser = webdriver.Chrome(options=options)

browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

browser.get("https://myaces.nus.edu.sg/htd/htd")

time.sleep(2)

username = browser.find_element_by_id("userNameInput")
password = browser.find_element_by_id("passwordInput")
submit = browser.find_element_by_id("submitButton")

username.clear
username.send_keys("nusstu\\e0253700")
password.clear
password.send_keys("")
submit.send_keys(Keys.RETURN)

time.sleep(5)

radioDeny = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, ".//input[contains(@name, 'symptomsFlag') and contains(@type, 'radio')]"))
)
familyDeny = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, ".//input[contains(@name, 'familySymptomsFlag') and contains(@type, 'radio')]"))
)
temperature = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, ".//input[contains(@id, 'temperature')]"))
)
submitTemp = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, ".//input[contains(@value, 'Submit') and contains(@name, 'Save')]"))
)

radioDeny.click()
time.sleep(1)
familyDeny.click()
time.sleep(1)
tempNumber = random.randrange(356, 367, 1) / 10
tempString = str(tempNumber)
temperature.clear
temperature.send_keys(tempString)
time.sleep(1)

submitTemp.click()

time.sleep(5)

browser.close
browser.quit


