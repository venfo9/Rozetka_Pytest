import pytest
from selenium import webdriver

class TestHomePage():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("C:/Selenium/chromedriver.exe")
        yield
        driver.close()

    #verify that "Доставка по всей Украине" is present in the meta description on home page
    def test_title(self, test_setup):
        driver.get("https://rozetka.com.ua/")
        page_description = driver.find_element_by_xpath("//meta[@name='description']").get_attribute("content")
        assert "Доставка по всей Украине" in page_description







