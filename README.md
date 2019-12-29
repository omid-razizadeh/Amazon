# Amazon
DP
There are different ways to extract information from webpages:
1.Computer vision
2.Using regular expressions
3.Web scraping like beautifulsoup or crawlers in python
We choose the third one and we want to extract some information from amazon and ebay website.
For this we need to know a little bit of css or xpath and the structure of scrapy library in python.

**In xpath:**

@ represents "attribute"
examples:
@class

@id

@href

Some examples:

Xpath and CSS equivalency:

xpath = '/html/body//div/p[2]'

css = 'html > body div > p:nth-of-type(2)'


Now, We can jump a little bit in more details:
::attr(attr-name)
css_locator = 'div#uid > a::attr(href)'

**Text extraction(::text)**
Example:
Hello world!
sel.css('p#p-example::text').extract()
Now for Scraping we need to know one more thing response:
product_name = response.css('h3.s-item__title::text').extract()
Structure of scrapy:
We need to first name the class and then define parse function and finally by using response extract the desired information.

**Note1.:For some websites like amazon they block to scrape. To overcome this difficulty there are some ways. I used proxy in my project.**
More information about how to set up proxy in your scrapy projects can be found on some github pages like:
https://github.com/hyan15/scrapy-proxy-pool

**Pagination:**
Another problem in web scraping is that our scrapy be able to go to next pages and scrape next page information as well. 
We can do this by defining by something like this:
```python
next_page = 'https://www.amazon.com/s?i=grocery&rh=n%3A16310101%2Cn%3A16310211%2Cn%3A16310231%2Cn%3A16521305011%2Cn%3A16318401%2Cn%3A16318511&page=' + str(AmazonSpiderSpider.page_number) + '&qid=1576114939&ref=sr_pg_2'
        if AmazonSpiderSpider.page_number <= 8:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback= self.parse)
```
