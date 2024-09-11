# Selenium settings
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Proxy settings
PROXY = "IpOfTheProxy:PORT"  # Replace with the actual proxy

# Corrected Chrome options
SELENIUM_DRIVER_ARGUMENTS = ["--headless"]  # Correct argument


def get_chrome_webdriver():
    chrome_driver_path = r"C:\Users\zaids\OneDrive\Desktop\Zaid\chromedriver.exe"
    chrome_options = Options()

    # Add proxy to Chrome options
    chrome_options.add_argument(f"--proxy-server={PROXY}")

    for arg in SELENIUM_DRIVER_ARGUMENTS:
        chrome_options.add_argument(arg)

    service = Service(chrome_driver_path)
    return webdriver.Chrome(service=service, options=chrome_options)


# Custom middleware configuration
DOWNLOADER_MIDDLEWARES = {
    "scrapy_selenium.SeleniumMiddleware": 800,
    "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 400,
}

SELENIUM_BROWSER = get_chrome_webdriver


BOT_NAME = "destroyamazon"

SPIDER_MODULES = ["destroyamazon.spiders"]
NEWSPIDER_MODULE = "destroyamazon.spiders"

DOWNLOAD_DELAY = 2
RETRY_ENABLED = True
RETRY_TIMES = 3


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "destroyamazon (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "destroyamazon.middlewares.DestroyamazonSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "destroyamazon.middlewares.DestroyamazonDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "destroyamazon.pipelines.DestroyamazonPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
