
import requests;
from bs4 import BeautifulSoup as soup
from db import insertURL

class HTMLDecomposer:

    def parseHTML(url):
        htmlText = requests.get(url).text
        parsed_html = soup(htmlText, features="html.parser")
        return parsed_html

    def getAnchorTags(url):
        parsed_html = HTMLDecomposer.parseHTML(url)
        anchorList = parsed_html.body.select('.cnt li>a');
        return anchorList
    
    def getPageAnchorTags(url):
        parsed_html = HTMLDecomposer.parseHTML(url)
        anchorList = parsed_html.body.select('.Search_Bar_Number .Search_Bar_a1');
        return anchorList

    def isCategoryURL(url):
        parsed_html = HTMLDecomposer.parseHTML(url)
        anchorList = parsed_html.body.select('.categories');
        return len(anchorList) > 0
    
    def getCompanyContainers(parsedCompanyContainer):
        companyContainer = parsedCompanyContainer.select('.biz_info_main')
        return companyContainer

    def getCompanyTitle(parsed_element):
        companyElement = parsed_element.select('.biz_info_title');

        if(len(companyElement) == 0):
            return '<NoCompanyTitleFound/>'
        
        return companyElement[0].getText();

    def getEmail(parsed_element):
        emailList = parsed_element.select('.biz_info_email>a');

        if(len(emailList) == 0):
            return '<NoEmailFound/>'

        return emailList[0].getText();

    def getWebsite(parsed_element):
        websiteList = parsed_element.select('.biz_info_description > u > a');

        if(len(websiteList) == 0):
            return '<NoWebsiteFound/>'

        return websiteList[0].getText();