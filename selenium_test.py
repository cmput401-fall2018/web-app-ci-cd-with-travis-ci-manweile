import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AssignFourTestCase(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_home(self):
        
        self.driver.get('http://199.116.235.216:8000')
        
        #these are the elements specified to test for in the assignment specs
        elements = ["name", "about", "education", "skills", "work", "contact"]
        
        for id in elements:
            assert self.driver.find_element_by_id(id) != None
        
    def tearDown(self):
        self.addCleanup(self.driver.quit)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)