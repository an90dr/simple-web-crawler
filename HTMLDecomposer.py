
import requests;
from bs4 import BeautifulSoup as soup
from db import insertURL

class HTMLDecomposer:

    def getAnchorTags(url):
        htmlText = requests.get(url).text
        parsed_html = soup(htmlText, features="html.parser")
        anchorList = parsed_html.body.select('.cnt li>a');
        return anchorList