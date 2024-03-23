import time
import unittest
from infra.infra_web.browser_wrapper import BrowserWrapper
from logic.web_logic.home_page_pathfinder import PathfinderPage
from logic.web_logic.login_page import LoginPage
from logic.web_logic.welcome_page import WelcomePage


class Login_Page_Test(unittest.TestCase):
    def setUp(self):
        self.test_cases = [self.test_log_in]
        self.browser = BrowserWrapper()

    def test_run(self):
        if self.browser.config["grid"]:
            self.browser.build_cap()
            if self.browser.config["grid type"] == "serial":
                self.browser.test_grid_serial(self.test_cases )
            if self.browser.config["grid type"] == "parallel":
                self.browser.test_grid_parallel(self.test_cases )
        else:
            self.browser.run_single_browser(self.test_cases,self.browser.config["browser"] )

    def test_log_in(self,driver):
        self.welcome_page = WelcomePage(driver)
        self.welcome_page.click_log_in()
        self.login_page = LoginPage(driver)
        self.login_page.login_flow("friendola15@gmail.com", "AutomationTester2024")
        self.pathfinder_page = PathfinderPage(driver)
        time.sleep(5)
        cookies = driver.get_cookies()
        for cookie in cookies:
            #if cookie['name'] == 'accessToken':  # Replace with the actual token cookie name
                #token = cookie['value']
                print(cookie)
        import requests

        # ZAP API URL and port (default values)
        zap_api_url = "http://localhost:8081"
        api_key = "pn945odbbs007a8j41litv5gt7"  # Replace with your actual ZAP API key

        # Get the list of messages proxied through ZAP
        response = requests.get(
            f"{zap_api_url}/JSON/core/view/messages/?zapapiformat=JSON&formMethod=GET&apikey={api_key}")

        # Parse the response JSON to get the messages
        messages = response.json()

        # Loop through the messages to find the one with your 'HttpOnly' cookie
        for message in messages.get("messages", []):
            # Check if this is the response you're interested in
            if "Set-Cookie" in message.get("responseHeader", ""):
                # Extract the 'Set-Cookie' value
                set_cookie_header = message["responseHeader"].split("Set-Cookie: ")[1].split(";")[0]
                #if "accessToken" in set_cookie_header:
                print("HttpOnly Cookie Found:", set_cookie_header)
