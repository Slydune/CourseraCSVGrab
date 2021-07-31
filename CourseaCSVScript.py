from selenium import webdriver
from time import sleep

class CourseaCSVScript:

    def __init__(self, driver, school_name='', course_name=''):
        self.school_name = school_name
        self.driver = driver
        self.course_name = course_name

    def load_webpage(self):
        self.driver.get('https://www.coursera.org/campus-coursematch')
        try:
            x_button = self.driver.find_element_by_xpath('//*[@id="rendered-content"]/div/div/div[1]/div/div[3]/div[2]/a')
            x_button.click()
            sleep(5)
        except:
            self.load_webpage()

    def search_school(self):
        frame = self.driver.find_element_by_xpath('//iframe[@title="Looker Dashboard"]')
        self.driver.switch_to.frame(frame)
        filter_dropdown = self.driver.find_element_by_xpath('//*[@id="dashboard-filter-section"]/div[1]/div[1]')
        filter_dropdown.click()
        school_name = self.driver.find_element_by_xpath('/html/body/lk-controller/div[1]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/lk-dashboard-filter/lk-filter/table/tbody/tr/td[2]/span[2]/span/span/lk-suggest-picker/div[1]/div/div/span')
        school_name.click()
        school_name_box = self.driver.find_element_by_xpath('/html/body/lk-controller/div[1]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/lk-dashboard-filter/lk-filter/table/tbody/tr/td[2]/span[2]/span/span/lk-suggest-picker/div[1]/div/input[1]')
        school_name_box.send_keys(self.school_name)
        run_button = self.driver.find_element_by_xpath('/html/body/lk-controller/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/button')
        run_button.click()

    def search_course(self):
        frame = self.driver.find_element_by_xpath('//iframe[@title="Looker Dashboard"]')
        self.driver.switch_to.frame(frame)
        filter_dropdown = self.driver.find_element_by_xpath('//*[@id="dashboard-filter-section"]/div[1]/div[1]')
        filter_dropdown.click()
        course_name = self.driver.find_element_by_xpath('/html/body/lk-controller/div[1]/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]/lk-dashboard-filter/lk-filter/table/tbody/tr/td[2]/span[2]/span/span/lk-suggest-picker/div[1]/div/div/input[1]')
        course_name.click()
        school_name_box = self.driver.find_element_by_xpath('/html/body/lk-controller/div[1]/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]/lk-dashboard-filter/lk-filter/table/tbody/tr/td[2]/span[2]/span/span/lk-suggest-picker/div[1]/div/div/input[1]')
        school_name_box.send_keys(self.school_name)
        run_button = self.driver.find_element_by_xpath('/html/body/lk-controller/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/button')
        run_button.click()

    def download(self):
        csv_dropdown = self.driver.find_element_by_xpath('/html/body/lk-controller/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div')
        csv_dropdown.click()
        csv_link = self.driver.find_element_by_xpath('/html/body/lk-controller/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li[3]/a[2]')
        csv_link.click()
