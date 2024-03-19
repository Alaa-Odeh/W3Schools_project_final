from selenium.webdriver.common.by import By

class WelcomePage:
    LOG_IN_BUTTON='//a[@class="user-anonymous tnb-login-btn w3-bar-item w3-btn bar-item-hover w3-right ws-light-green ga-top ga-top-login"]'
    UPPER_FRAME='//iframe[@id="top-nav-bar-iframe"]'


    def __init__(self, driver):
        self._driver =driver
        #self._driver.switch_to.frame(driver.find_element(By.XPATH,self.UPPER_FRAME ))
        self.log_in_button=self._driver.find_element(By.XPATH, self.LOG_IN_BUTTON)
        #self._driver.switch_to.default_content()

    def click_log_in(self):
        self.log_in_button.click()