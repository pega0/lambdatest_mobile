import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions

import base


class MyTest:
    def test_open(self):
        remote_url = base.LT_MOBILE_REMOTE_URL
        lambdatest_opts = {
            "LT:options": {
                "platformName": "android",
                "deviceName": "Pixel 7",
                "platformVersion": "13",
                "network": True,
                "build": "cams aqa dev",
                "name": "cams 2.0",
                "tunnel": False,
                "idleTimeout": 600,
                "isRealMobile": True
            }
        }
        lambdatest_opts = {
            "platformName": "android",
            "deviceName": "Pixel 7",
            "platformVersion": "13",
            "network": True,
            "build": "cams aqa dev",
            "name": "cams 2.0",
            "tunnel": False,
            "idleTimeout": 600,
            "isRealMobile": True
        }
        options = ChromeOptions()
        options.set_capability("LT:options", lambdatest_opts)

        driver = webdriver.Remote(
            command_executor=remote_url,
            options=options,

        )
        driver.get('http://cams.com')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="//button[text()='Login']").click()
        wait = WebDriverWait(driver, timeout=2)
        element_locator = (By.XPATH, "//input[@autocomplete='username']")

        wait.until(EC.visibility_of_element_located(element_locator))
        driver.find_element(by=By.XPATH, value="//input[@autocomplete='username']").send_keys(base.USERNAME)
        driver.find_element(by=By.XPATH, value="//input[@autocomplete='password']").send_keys(base.PASSWORD)
        driver.find_element(by=By.XPATH, value="//div[contains(@class,'CamsButton')]/button[text()='Login']").click()
        time.sleep(5)
        driver.close()
        driver.quit()


if __name__ == '__main__':
    my_test = MyTest()
    my_test.test_open()
