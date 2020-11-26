import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class crawledArticle():
    def __init__(self,title,price):
        self.title=title
        #self.rating=rating
        self.price=price

class b:

    def article(self, name):
        count = 1
        page = 1
        pageIncrement = 10
        maxRetrieves = 100

        a = []

        url = "https://www.amazon.com/s?k=" + name + "&page=" + str(page)

        options = Options()
        options.headless = False
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        browser.maximize_window()
        browser.get(url)
        browser.set_page_load_timeout(10)      

        while True:
            try:
                if pageIncrement*page > maxRetrieves:
                    break
                
                if count > pageIncrement:
                    count = 1
                    page += 1

                # Get Title
                xPathTitle = '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[' + str(count) + ']/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span'
                title = browser.find_element_by_xpath(xPathTitle)
                titleText = title.get_attribute("innerHTML").splitlines()[0]
                title.click()
                
                # Get Price
                xPathPrice = '//*[@id="price_inside_buybox"]'
                price = browser.find_element_by_xpath(xPathPrice)
                priceText = price.get_attribute("innerHTML")

                url = "https://www.amazon.com/s?k=iphone+11&page=" + str(page)
                browser.get(url)
                browser.set_page_load_timeout(10) 

                info = crawledArticle(titleText, priceText)
                a.append(info)
                
                count += 1

            except Exception as e:
                # print("Exception On Count", count, e)
                count += 1

                if pageIncrement*page > maxRetrieves:
                    break
                
                if count > pageIncrement:
                    count = 1
                    page += 1

                url = "https://www.amazon.com/s?k=iphone+11&page=" + str(page)
                browser.get(url)
                browser.set_page_load_timeout(10) 


        browser.close()

        return a


fetcher = b()

with open('pro.csv', 'w', newline='', encoding='utf-8') as csvfile:
    articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for article in fetcher.article("iphone 11"):
        articlewriter.writerow([article.title,article.price])
