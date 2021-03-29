import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'catalouge'
	allowed_domains= ['dmoztools.net']
    start_urls = ['http://dmoztools.net/Arts/Animation/']
			
    def parse(self, response):
        for title in response.xpath('//*[@id="site-item"]'):
            yield {
				#'content': title.xpath('./div[@class="site-descr "]/text()').extract_first(),
				'content': title.xpath('./div[@class="title-and-desc"]/div[@class="site-descr"]/text()').extract_first(),
				#'title':title.path('./div[@class="title-and-desc"]/a/div[@class="site-title"]/text()').extract_first(),
				#'url':title.path('./div[@class="title-and-desc"]/a/href').extract_first()
			}

