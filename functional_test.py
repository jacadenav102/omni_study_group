from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

import unittest

class NewVisitorTest(unittest.TestCase):
   def setUp(self) -> None:
      self.browser = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                      desired_capabilities=DesiredCapabilities.CHROME)
   def tearDown(self) -> None:
      self.browser.quit()
   
   def test_can_start_a_list_and_retrieve_it_later(self):
      self.browser.get('http://127.0.0.1:8000/')
      self.assertIn("invalid session id", self.browser.title)
#      self.fail('Finish the test!')
if __name__ == "__main__":
   unittest.main(warnings='ignore')
