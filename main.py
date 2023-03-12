from lib import scrapper as Scrapper
from lib import request as Request

def main():
    
    url = input("url : ")
    
    request = Request.Request()
    html = request.getdata(url)
    
    scrapper = Scrapper.Scrapper(html)

    data_src = scrapper.get_datasrc()
    title = scrapper.get_title()
    chapter = [x for x in url.split("/") if x != '']
    for url in data_src:
        urls = [x for x in url.split("/") if x != '']
        filename = urls[-1]

        request.download(url, title, chapter[-1], filename)
    
if __name__ == '__main__':
    main()