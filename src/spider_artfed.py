import scrapy


class SpiderArtfedSpider(scrapy.Spider):
    name = "parse_bookstore"
    headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0'}

    def start_requests(self):
        yield scrapy.Request('https://books.toscrape.com/catalogue/category/books_1/index.html', self.parse)
        yield scrapy.Request('https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
                             self.parse)
        yield scrapy.Request('https://books.toscrape.com/catalogue/category/books/classics_6/index.html', self.parse)
        yield scrapy.Request('https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html',
                             self.parse)
        yield scrapy.Request('https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
                             self.parse)
        yield scrapy.Request('https://books.toscrape.com/catalogue/category/books/new-adult_20/index.html',
                             self.parse)

    def parse(self, response, **kwargs):
        for h1 in response.xpath('//h1/text()').getall():
            yield {"Title": h1}

        for price in response.xpath('//p[@class="price_color"]/text()').getall():
            yield {'Price: ': price}

        for img in response.xpath('//img/@src').getall():
            yield {'Image href': img}

        next_page_selector = '.next a ::attr(href)'
        # extract the first match, and check if it exists
        next_page = response.css(next_page_selector).extract_first()

        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, self.parse, headers=self.headers)
