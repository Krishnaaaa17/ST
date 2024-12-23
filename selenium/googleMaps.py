import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleMapsAutomation:
    def setUp(self):
        self.driver = webdriver.Chrome()

    def search_location(self):
        try:
            g_link = "https://www.google.com/maps"
            self.driver.get(g_link)
            time.sleep(2)

            name = input("Enter Location: ")
            self.driver.find_element(By.ID, "searchboxinput").send_keys(name)
            time.sleep(2)

            self.driver.find_element(By.ID, "searchbox-searchbutton").click()
            time.sleep(5)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    automation = GoogleMapsAutomation()
    automation.setUp()
    automation.search_location()
    automation.tearDown()
