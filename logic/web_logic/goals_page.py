from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoalsPage:
    ADD_GOAL_BUTTON = '//button[contains(text(),"Add +")]'

    def __init__(self, driver):
        self._driver =driver
        self.add_goal_button=WebDriverWait(self._driver,15).until(EC.visibility_of_element_located((By.XPATH, self.ADD_GOAL_BUTTON)))