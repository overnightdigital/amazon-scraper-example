from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AmazonScraper:
    def __init__(self, term):
      self.term = term
    
    def init_driver(self):
      # self.driver = webdriver.Chrome('./chromedriver.exe')
      self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def crawl(self):
       self.driver.get('https://www.amazon.com/s?k='+self.term)



if __name__ == '__main__':
    amazonScraper = AmazonScraper("iphone 11")
    amazonScraper.init_driver()
    amazonScraper.crawl()
