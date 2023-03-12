from mechanize import Browser
import requests
import os
class Request:
    def __init__(self):
        self.downloaded_path = os.path.abspath(os.curdir) + "/downloaded/"
        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
        self.br = Browser()
        self.br.set_handle_robots(False)
        self.br.set_handle_equiv(True)
        self.br.set_handle_referer(True)
        self.br.addheaders = [('User-Agent',self.ua)]
    
    def getdata(self,url):
        res = self.br.open(url)
        return res.get_data()

    def download(self, url, title, chapter, filename):
        title = str(title)
        title = title.replace("<title>","").replace("</title>","")
        print("Downloading : " + title + "["+chapter+"][" + str(filename) +"]")
        if(os.path.exists(self.downloaded_path + title + "/" + chapter) != True):
            os.makedirs(self.downloaded_path + title + "/" + chapter)
        req = requests.get(url, stream=True, headers={'User-Agent':self.ua})
        with open(self.downloaded_path + title + "/" + chapter + "/" + filename, "wb") as out_file:
            for chunk in req.iter_content(chunk_size=1024):
                out_file.write(chunk)
