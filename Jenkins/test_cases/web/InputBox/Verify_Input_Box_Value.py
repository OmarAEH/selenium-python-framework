"""
=======================
VerifyInputBoxValue.py
=======================

:Module Desc: Verify value into text box.

:Test Author: https://github.com/OmarAEH

"""

# Python imports
import allure
import unittest
from selenium import webdriver


@allure.parent_suite("InputBoxes")
class VerifyInputBoxValue(unittest.TestCase):
    """
    :Class Description: Verify value into text box.

    """
    @allure.feature("Verify value into text box.")
    def test_input_box_value(self):
        driver = webdriver.Chrome('../../../driver/chromedriver.exe')
        driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
        driver.find_element_by_id("RESULT_TextField-1").send_keys("OMAR")
        driver.find_element_by_id("RESULT_TextField-2").send_keys("AEH")
        driver.find_element_by_id("RESULT_TextField-3").send_keys("+962791444516")


if __name__ == '__main__':
    unittest.main()
