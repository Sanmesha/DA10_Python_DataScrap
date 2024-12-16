import scrapy


class BookspageSpider(scrapy.Spider):
    name = "bookspage"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        
        books = response.css("article.product_pod h3 a::attr(title)").getall()
        
       
        for book in books:
            yield {"title": book}

        
        next_page = response.css("ul.pager li.next a::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
