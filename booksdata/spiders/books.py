import scrapy
from pathlib import Path
from pymongo import MongoClient
import datetime

client = MongoClient("CONNECTION_STRING_HERE")
db = client["books_database"]
 

def insert_into_mongo(page, title, image, rating, price, inStock):
    collection = db[page]
    doc= {
        "title": title,
        "rating": rating,
        "price": price,
        "date": datetime.datetime.now(),
        "image": image,
        "inStock": inStock
    }
    inserted = collection.insert_one(doc)
    
    print(f"Inserted document with id: {inserted.inserted_id}")
    return inserted.inserted_id
    
    


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://toscrape.com"]


    async def start(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"books-{page}.html"
        bookdetail={}
        
        
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        # a = response.css(".product_pod").get()
        # print(a)
        # a = response.css(".product_pod")
        # b = a.css("a")
        # print(b)
        cards = response.css(".product_pod")
        for card in cards:
            #get titles
            title = card.css("h3>a::text").get()
            print(title)
            
            #get images
            # image = card.css(".image_container img").get()
            # print(image)
            
            image = card.css(".image_container img") #.get() HUDAINA because we want the selector object & this methods gives string instead.
            # print(image.attrib['src'])
            image = image.attrib['src'].replace("../../../../media/","https://books.toscrape.com/media/")
            
            #get rating
            rating = card.css(".star-rating").attrib['class'].split(" ")[1]
            print(rating)
            
            #get price
            price = card.css(".price_color::text").get()
            print(price)
            
            #get availability
            availablity = card.css(".availability")
            
            
            if len(availablity.css(".icon-ok")) > 0:
                inStock = True
            else:
                inStock = False
                
            # Store the extracted data into MongoDB
            insert_into_mongo(filename, title, image, rating, price, inStock)