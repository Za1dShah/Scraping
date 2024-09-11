import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import random


class Zon1Spider(scrapy.Spider):
    name = "zon1"
    allowed_domains = ["-------"]
    start_urls = ["https://www.-------.ae/"]

    useragentarray = [
    # Google Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:118.0) Gecko/20100101 Firefox/118.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:117.0) Gecko/20100101 Firefox/117.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:116.0) Gecko/20100101 Firefox/116.0",
    
    # Mozilla Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    

]


    def __init__(self, *args, **kwargs):
        super(Zon1Spider, self).__init__(*args, **kwargs)
        path = r"C:\Users\zaids\OneDrive\Desktop\Zaid\chromedriver.exe"
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        self.service = Service(path)
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)

        # Set a random user agent
        user_agent = random.choice(self.useragentarray)
        self.driver.execute_cdp_cmd(
            "Network.setUserAgentOverride", {"userAgent": user_agent}
        )

    def parse(self, response):
        try:
            self.driver.get("https://www.------.ae/")
            print("Navigated to ------")
            search = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )
            search.send_keys("football")
            search.send_keys(Keys.RETURN)
            print("Search completed")
        except Exception as e:
            self.logger.error(f"Error locating search box: {e}")
            self.driver.quit()
            return

        while True:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.CSS_SELECTOR,
                            "a.a-link-normal.s-no-hover.s-underline-text.s-underline-link-text.s-link-style.a-text-normal",
                        )
                    )
                )
                product_links = self.driver.find_elements(
                    By.CSS_SELECTOR,
                    "a.a-link-normal.s-no-hover.s-underline-text.s-underline-link-text.s-link-style.a-text-normal",
                )
                print(f"Found {len(product_links)} product links")

                if not product_links:
                    self.logger.info("No more products found on this page.")
                    break

                for link in product_links:
                    href = link.get_attribute("href")
                    yield scrapy.Request(href, callback=self.parse_product_page)

                next_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']",
                        )
                    )
                )
                print("Found next button")

                if next_button.is_enabled():
                    next_button.click()
                    print("Clicked next button")
                    WebDriverWait(self.driver, 10).until(
                        EC.staleness_of(next_button)
                    )
                else:
                    self.logger.info("Next button is disabled or not clickable.")
            except Exception as e:
                self.logger.error(f"Error during parsing: {e}")
                break


    def parse_product_page(self, response):
        self.driver.get(response.url)

        # Waiting for the page to load completely
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "productTitle"))
        )

        # Extract product details
        title = (
            WebDriverWait(self.driver, 10)
            .until(EC.presence_of_element_located((By.ID, "productTitle")))
            .text
        )

        # Extract the price 
        price = response.xpath('//input[@id="attach-base-product-price"]/@value').get()
        if not price:
            price = response.xpath("//span[@class='a-price-whole']/text()").get()
        if not price:
            price = response.xpath(
                "//span[@class='a-price a-text-price a-size-medium apexPriceToPay']//span[@class='a-offscreen']/text()"
            ).get()
        if not price:
            price = response.xpath(
                "//input[@name='items[0.base][customerVisiblePrice][amount]']/@value"
            ).get()
        if not price:
            price = response.xpath(
                "//span[@class='a-price a-text-price a-size-medium apexPriceToPay']/span[@class='a-offscreen']/text()"
            ).get()

        if not price:
            try:
                price_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".a-price-whole"))
                )
                price = price_element.text
            except Exception as e:
                price = "Price not found"

        # Extract the rating
        rating = self.driver.find_element(By.ID, "acrPopover").get_attribute("title")

        yield {"title": title, "price": price, "rating": rating, "url": response.url}

    def closed(self, reason):
        self.driver.quit()
