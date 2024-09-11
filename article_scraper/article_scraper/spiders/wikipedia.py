import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
import time

def wait(driver):
    time.sleep(1)
    return True


class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org"]

    rules = [
        Rule(
            LinkExtractor(allow=r"wiki/((?!:).)*$"), callback="parse_info", follow=True
        )
    ]

    def start_requests(self):
        for url in self.start_urls:
         yield SeleniumRequest(url=url, wait_time=10, wait_until=wait, callback=self.parse_info)

    def parse_info(self, response):
        driver = response.request.meta['driver']

        search = driver.find_element_by_xpath("//form[@id='searchform' and @class='cdx-typeahead-search__form' and @action='/w/index.php']")
        search.send_keys('mountain')

        submit = driver.find_element_by_xpath("//button[contains(@class, 'cdx-button') and contains(@class, 'cdx-button--action-default') and contains(@class, 'cdx-button--weight-normal') and contains(@class, 'cdx-button--size-medium') and contains(@class, 'cdx-button--framed') and contains(@class, 'cdx-search-input__end-button') and text()='Search']")
        submit.click()


        time.sleep(5)


