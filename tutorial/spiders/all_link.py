from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
import itemloaders

class FollowAllSpider(CrawlSpider):
    name = "follow_all"
	allowed_domains = ["dmoztools.net"]
    start_urls = ["http://dmoztools.net/"]
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self, response):
		pass