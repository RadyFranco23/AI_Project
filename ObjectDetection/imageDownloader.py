from icrawler.builtin import BingImageCrawler

objetos = ["puros"]

for objeto in objetos:
    crawler = BingImageCrawler(storage={"root_dir": f"dataset/{objeto}"})
    crawler.crawl(keyword=objeto, max_num=50)