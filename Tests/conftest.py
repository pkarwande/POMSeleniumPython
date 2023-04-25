import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        web_driver.get(TestData.URL)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        web_driver.get(TestData.URL)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()


