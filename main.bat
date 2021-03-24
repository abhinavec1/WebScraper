call .\venv\Scripts\activate
cd scraper
scrapy crawl necklacespider -o result.csv
scrapy crawl necklacespider -o result.json
deactivate