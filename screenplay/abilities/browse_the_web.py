from screenpy_selenium.abilities import BrowseTheWeb
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

def using_chrome():
    return BrowseTheWeb.using(Chrome(ChromeDriverManager().install()))
