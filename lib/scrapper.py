from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self, html):
        self.bs = BeautifulSoup(html, 'html5lib')
        
    def get_datasrc(self):
        
        listofdiv = self.bs.find('div',{'class':'reading-content'}).find_all('div',{'class':'page-break no-gaps'})
        
        data_src = []
        
        for div in listofdiv:
            data_src.append(div.find('img')['data-src'].replace('\t','').replace('\n',''))
        
        return data_src
    
    def get_title(self):
        return self.bs.title
    