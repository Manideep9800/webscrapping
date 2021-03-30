import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'catalouge'
	#allowed_domains= ['dmoztools.net']
    start_urls = ['http://dmoztools.net/Arts/Animation/']
	#rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]
			
    def parse(self, response):
        for title in response.xpath('//*[@id="site-list-content"]/div'):
            yield {
				#'content': title.xpath('./div[@class="site-descr "]/text()').extract_first(),
				#'content': title.xpath('./div[@class="title-and-desc"]/div[@class="site-descr"]/text()').extract_first(),
				'title':title.path('./div/a/div/text()').extract_first(),
				'url':title.path('./div/a/@href').extract_first()
			}

