
import requests;
from bs4 import BeautifulSoup as soup

class HTMLDownloader:
    def getHTML(url):
        htmlText = requests.get(url).text
        parsed_html = soup(htmlText, features="html.parser")
        anchorList = parsed_html.body.select('.cnt li>a');

        hrefs = '';
        for anchor in anchorList:
           hrefs = hrefs + anchor['href'] + '\n';

        return hrefs; 
        
