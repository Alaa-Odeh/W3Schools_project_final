import re

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logic.web_logic.svg_tutorial import SvgTutorial


class PathfinderPage(object):
    MY_W3SCHOOLS_LOGGED_IN='//h2[@class="chakra-heading css-wnbja6"]'
    SET_A_GOAL_BUTTON="//button[@class='chakra-button css-1irtsw7']"
    BACKEND_DEVELOPER_BUTTON='//button[contains(text(),"Backend developer")]'
    REMOVE_C_PLUS_PLUS_BUTTON='//button[@aria-label="Remove C++"]'
    CONTINUE_BUTTON='//button[contains(text(),"Continue")]'
    ADD_ADDITIONAL_SKILLS_BUTTON='//button[./*[contains(text(),"Add additional skills")]]'
    SOFT_SKILLS_CHECKBOX="span.chakra-checkbox__control"
    COURSE_LEVEL_BUTTON='//div[@class="chakra-select__wrapper css-jye2s8"]//select'
    TIME_REQUIRED_FOR_COURSE="//p[contains(text(),'Time Required')]"
    HOURS_SLIDER='//*[@id="slider-thumb-slider-duration"]'
    ESTIMATED_GOAL_COMPLETION_TIME='//span[@class="chakra-text css-722v25"]'
    SOFT_SKILLS_LABEL="//label[./span[contains(text(), 'Soft skills')]]"

    RESUME_LEARNING_BUTTON='//div[@class="css-13htum"]'
    TESTS_LINK='//a[./p[contains(text(),"Tests")]]'
    SKILLS_LINK='//a[./p[contains(text(),"Skills")]]'
    TOGGLE_BUTTON='//*[@class="chakra-button css-1lfqljy"]'
    TUTORIALS_BUTTON='//a[@id="navbtn_tutorials"]'
    LEARN_SVG='//a[@class="w3-bar-item w3-button acctop-link ga-top-drop ga-top-drop-tut-svg"]'
    SUBTITLE='//a[@class="user-authenticated tnb-dashboard-btn w3-bar-item w3-button w3-right w3-white ga-top ga-top-dashboard"]'
    UPPER_FRAME='//iframe[@id="top-nav-bar-iframe"]'


    def __init__(self, driver):
        self._driver =driver
        wait = WebDriverWait(driver, 20)  # Timeout of 10 seconds

    def init(self):
        self.set_a_goal_button=WebDriverWait(self._driver,15).until(EC.visibility_of_element_located((By.XPATH, self.SET_A_GOAL_BUTTON)))
        self.tests_button=WebDriverWait(self._driver,20).until(EC.visibility_of_element_located((By.XPATH, self.TESTS_LINK)))
        self.light_mode_button=WebDriverWait(self._driver,15).until(EC.element_to_be_clickable((By.XPATH, self.TOGGLE_BUTTON)))
        self.skills_button=WebDriverWait(self._driver,15).until(EC.visibility_of_element_located((By.XPATH, self.SKILLS_LINK)))

    def extract_user_name(self  ):
        h2_element = self._driver.find_element(By.CSS_SELECTOR, "h2.chakra-heading")
        return h2_element.text.split(", ")[1].split(" ")[0]
    def click_svg_link_tutorials(self):
        self.svg_tutorials_button=WebDriverWait(self._driver,20).until(EC.visibility_of_element_located((By.XPATH, self.LEARN_SVG)))
        self.svg_tutorials_button.click()
    def click_on_tutorials(self):
        self._driver.switch_to.frame(self._driver.find_element(By.XPATH, self.UPPER_FRAME))
        self.tutorials_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.TUTORIALS_BUTTON)))
        self.tutorials_button.click()


    def click_on_light_mode_button(self):
        self.init()
        self.light_mode_button.click()
    def click_skills_button(self):
        self.skills_button.click()
    def click_on_tests_button(self):
        self.init()
        self.tests_button.click()
    def click_on_resume_learning_button(self):
        self.resume_learning_button=WebDriverWait(self._driver,20).until(EC.visibility_of_element_located((By.XPATH, self.RESUME_LEARNING_BUTTON)))
        self.resume_learning_button.click()
    def click_on_set_a_goal_button(self):
        self.set_a_goal_button.click()
        self.backend_developer_button=WebDriverWait(self._driver,15).until(EC.visibility_of_element_located((By.XPATH, self.BACKEND_DEVELOPER_BUTTON)))

    def click_on_backend_developer_button(self):
        self.backend_developer_button.click()
        self.remove_c_plus_plus=WebDriverWait(self._driver,15).until(EC.visibility_of_element_located((By.XPATH, self.REMOVE_C_PLUS_PLUS_BUTTON)))

    def click_on_remove_c_plus_plus_button(self):
        self.remove_c_plus_plus.click()
        self.continue_button=self._driver.find_element(By.XPATH, self.CONTINUE_BUTTON)

    def click_on_continue_button(self):
        self.continue_button.click()
        self.add_additional_skills_button = WebDriverWait(self._driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.ADD_ADDITIONAL_SKILLS_BUTTON)))

    def click_on_add_additional_skills_button(self,choosen_skill):
        self.add_additional_skills_button.click()
        labels='//span[@class="chakra-checkbox__label css-6x44c9"]'
        check_box = ".chakra-checkbox__control"

        labels_el = self._driver.find_elements(By.XPATH,labels)
        checkboxes = self._driver.find_elements(By.CSS_SELECTOR, check_box)

        self.skills_index = None

        for index, label in enumerate(labels_el):
            if choosen_skill in label.text:
                self.skills_index = index
                break
        while True:
            try:
                if self.skills_index is not None:
                    self.skills_checkbox = checkboxes[self.skills_index]
                break
            except:
                self._driver.execute_script("window.scrollBy(0, 350);")


    def click_on_skills_checkbox(self):
        self.skills_checkbox.click()
        all_course_level_button = WebDriverWait(self._driver,10).until(EC.presence_of_all_elements_located((By.XPATH,self.COURSE_LEVEL_BUTTON)))
        self.course_level_button=all_course_level_button[2]


    def set_course_level_to_your_choice(self,level_option):
        Select(self.course_level_button).select_by_visible_text(level_option)
        self.estimation_for_each_course = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.TIME_REQUIRED_FOR_COURSE)))
        self.hours_weekly_slider = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.HOURS_SLIDER)))
        self.total_goal_estimation = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ESTIMATED_GOAL_COMPLETION_TIME)))

    def total_time_required_for_all_courses(self):
        time_required_list = []
        for element in self.estimation_for_each_course:
            text = element.text
            # Use regex to find the number of hours in the text
            hours = re.findall(r"(\d+) hrs", text)
            if hours:
                time_required_list.append(int(hours[0]))
        return sum(time_required_list)



    def set_hours_weekly_slider(self,hours_weekly):
        self._driver.execute_script("arguments[0].scrollIntoView(true);", self.hours_weekly_slider)
        current_value = int(self.hours_weekly_slider.get_attribute("aria-valuenow"))
        offset=(hours_weekly-current_value)
        actions =ActionChains(self._driver)
        actions.click_and_hold(self.hours_weekly_slider).move_by_offset(offset*6, 0)
        actions.release()
        actions.perform()


    def get_total_goal_estimation(self):
        self.init()
        total_estimation=self.total_goal_estimation.text
        total_estimation_list=total_estimation.split(' ')
        months=int(total_estimation_list[0])
        if len(total_estimation_list) > 2:
            weeks=int(total_estimation_list[3])
            total_weeks=weeks+ 4*months
        else:
            total_weeks=4*months
        return total_weeks

    def set_goal_and_calculate_total_estimated_time(self,hours_weekly,choosen_skill,course_level):
        self.init()
        self.click_on_set_a_goal_button()
        self.click_on_backend_developer_button()
        self.click_on_remove_c_plus_plus_button()
        self.click_on_continue_button()
        self.click_on_add_additional_skills_button(choosen_skill)
        self.click_on_skills_checkbox()
        self.set_course_level_to_your_choice(course_level)
        return self.total_time_required_for_all_courses()/hours_weekly

    def set_weekly_hours_slider_and_get_estimated_goal(self,hours_weekly):
        self.set_hours_weekly_slider(hours_weekly)
        return self.get_total_goal_estimation()


    def get_light_mode_label_before(self):
        return self.light_mode_button.get_attribute("aria-label")

    def get_light_mode_label_after(self):
        return self.light_mode_button.get_attribute("aria-label")

    def choose_learn_svg_tutorials(self):
        self.click_on_tutorials()
        self.click_svg_link_tutorials()
        svg_tutorial = SvgTutorial(self._driver)
        self._driver.switch_to.window(self._driver.current_window_handle)
        text=svg_tutorial.get_header().text
        self._driver.back()
        return text





