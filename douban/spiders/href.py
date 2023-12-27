

from douban.items import MovieHref
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Request, Rule
from scrapy import Selector, Request,Spider

class HrefSpider(Spider):
    name = "href"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4507.400',
        'Cookie': 'll="118254"; bid=F3nzwyuiz6g; push_noty_num=0; push_doumail_num=0; __utmv=30149280.21750; _pk_id.100001.4cf6=23a9863be56fa092.1703169814.; _vwo_uuid_v2=D5A69A952E3867F076DA8912762C95A75|f29b4a94cf7ad8bbc82b0f06d77cd1e8; __yadk_uid=2Uc5kD6e3u8JyQLIRdOE9tdb6wLBAEBK; _ga_PRH9EWN86K=GS1.2.1703175493.1.0.1703175493.0.0.0; dbcl2="217508596:CF9qjTfz92E"; ck=aguU; _ga=GA1.2.1710192885.1703175296; _gid=GA1.2.1704978320.1703589618; _ck_desktop_mode=1; vmode=pc; _ga_Y4GN1R87RG=GS1.1.1703589617.5.0.1703589619.0.0.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1703589620%2C%22https%3A%2F%2Fm.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1; SL_G_WPT_TO=zh; __utma=30149280.2055416533.1703169789.1703573732.1703589620.19; __utmb=30149280.0.10.1703589620; __utmc=30149280; __utmz=30149280.1703589620.19.15.utmcsr=m.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.771649876.1703169814.1703522083.1703589620.15; __utmb=223695111.0.10.1703589620; __utmc=223695111; __utmz=223695111.1703589620.15.12.utmcsr=m.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; frodotk_db="76b84ebaa3965b696428ec2feac3123b"'
    }
    custom_settings = {
        'ITEM_PIPELINES': {"douban.pipelines.MovieHrefPipeline": 300},
    }

    def start_requests(self):
        for i in range (0,10):

            url = f"https://movie.douban.com/top250?start={i*25}&filter="
            yield Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        selector = Selector(response)
        Href = MovieHref()
        for i in range(1,26):
            Href["href"] = selector.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{i}]/div/div[2]/div[1]/a/@href').extract_first()
            yield Href
   
