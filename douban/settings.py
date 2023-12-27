# Scrapy settings for douban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "douban"

SPIDER_MODULES = ["douban.spiders"]
NEWSPIDER_MODULE = "douban.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
LOG_LEVEL = 'WARNING' 
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
   'Cookie': 'BAIDUID_BFESS=0A0D70FEE66912CF31BD0AF2A0B43172:FG=1; jsdk-uuid=b82fd655-86ba-47a2-aaa9-fdf52a722834; __bid_n=18c0ee7d77a2016fdc0ca2; Hm_lvt_246a5e7d3670cfba258184e42d902b31=1702730607; BDUSS=Y4elA2MXI3UlExVFA2dmV4VVY2SDZ3Yn54NVpRQnplNnVOZEY2dGZEUUxCckZsSVFBQUFBJCQAAAAAAAAAAAEAAAAH1c6esru2rrXEv9UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAt5iWULeYllMW; BDUSS_BFESS=Y4elA2MXI3UlExVFA2dmV4VVY2SDZ3Yn54NVpRQnplNnVOZEY2dGZEUUxCckZsSVFBQUFBJCQAAAAAAAAAAAEAAAAH1c6esru2rrXEv9UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAt5iWULeYllMW; RT="z=1&dm=baidu.com&si=899bcf04-b5f9-428c-9011-3553330bf822&ss=lqkwpfah&sl=13&tt=efv&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&nu=5dr2ycr8&cl=ab1n&ld=ab5y&ul=ab1y&hd=ab66"; BIDUPSID=0A0D70FEE66912CF31BD0AF2A0B43172; PSTM=1703591491; H_PS_PSSID=39935_39936_39932_39939_39732_39974_39991_40009_40041'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "douban.middlewares.DoubanSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "douban.middlewares.DoubanDownloaderMiddleware": 543,
#    "douban.middlewares.ProxyMiddleware": 543
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "douban.pipelines.MovieHrefPipeline": 300,
   "douban.pipelines.DoubanPipeline": 400,
    "douban.pipelines.MovieCommentPipeline": 400,
   
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
