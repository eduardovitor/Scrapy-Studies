import scrapy

class QuotesSpider(scrapy.Spider):
    name = "QuotesSpider"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response): # Decidi usar o seletor css para me desafiar
        quotes = response.css("div.quote")
        for q in quotes:
            yield {
                "title": q.css("span.text::text").get(),
                "author": q.css("span").css("small.author::text").get(),
                "tags": q.css("div.quote").css("div.tags")[0].css("a::text").getall()
            }
        next_page = response.css("li.next").css("a::attr(href)").get()
        if next_page is not None:
           yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
