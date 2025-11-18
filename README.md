# Books Scraper website → Scrapy framework→ MongoDB 📚

Project that scrapes book data from "Books to Scrape" and stores results in MongoDB.

Target site 🔗
- Example page used: https://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html

Overview ℹ️
- A Scrapy-based project that crawls book listings and saves scraped items to a MongoDB collection.
- The MongoDB connection string has been removed from the repository for security. You must provide it locally (see Configuration).

Requirements ✅
- Python
- Scrapy
- pymongo (or an async MongoDB driver if the pipeline is implemented that way)
- python-dotenv (optional, if using .env)

Quick setup ⚙️
1. Create and activate a virtual environment:
   - python -m venv .venv
   - Windows: .venv\Scripts\activate
   - macOS/Linux: source .venv/bin/activate
2. Install dependencies:
   - pip install scrapy pymongo python-dotenv

Configuration (providing the removed connection string) 🔒
  - Create a file named `.env` in the project root and add:
    MONGODB_URI="mongodb://username:password@host:port/database"
  - The project should read MONGODB_URI from environment variables (or via python-dotenv).

- Ensure the URI you provide has proper credentials and database name.

Running the spider ▶️
- From the project root run:
  - scrapy crawl <spider_name>
  
- If the pipeline is configured to write to MongoDB the spider run will insert items directly into the configured collection.

Scraped item fields (typical) 🧾
- title: string
- price: string (e.g. "£51.77")
- availability: string (e.g. "In stock (22 available)")
- rating: string/number (e.g. "Three" or 3)
- product_page_url: string
- upc: string (if scraped from product page)
- product_description: string
- category: string

Sample MongoDB document 🗂️
{
  "title": "Sharp Objects",
  "price": "£47.82",
  "availability": "In stock (20 available)",
  "rating": "Four",
  "product_page_url": "https://books.toscrape.com/catalogue/sharp-objects_997/index.html",
  "upc": "a1234567890b",
  "product_description": "Book description text...",
  "category": "Mystery"
}

Notes and troubleshooting 🛠️
- Connection refused / authentication errors: verify MONGODB_URI, username/password, and network access to the MongoDB host.
- If using a cloud MongoDB (Atlas), ensure your IP is whitelisted or use the appropriate connection settings.
- Check the Scrapy logs (logs/) for details when runs fail.

Security 🔐
- Do not commit `.env` or `config_local.py` with credentials to version control.
- The repository currently omits the connection string on purpose — add it locally as described above.
