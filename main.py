import sys;
from HTMLDecomposer import HTMLDecomposer
from constants import MODE_TYPE_COLLECT_EMAILS, MODE_TYPE_MASS_PAGE_URL_PARSING, MODE_TYPE_PARSE_PAGE_URLS, MODE_TYPE_UPDATE_URL_TYPE, MODE_TYPE_URL, SOURCE_WEBSITE_HOST
from db import getPageURLs, getSourceURLs, insertPageURL, insertURL, updateURLType;
from bs4 import BeautifulSoup as soup
   
def url_parse():
    anchorTagList = HTMLDecomposer.getAnchorTags(sys.argv[2])

    insert_counter = 0;
    for anchor in anchorTagList:
        insert_counter += insertURL({"url": anchor['href']})

    print("INSERTED " + str(insert_counter) + " NEW URLS" )
    return;

def url_parse_page_url():
    anchorTagList = HTMLDecomposer.getPageAnchorTags(sys.argv[2])

    insert_counter = 0;
    for anchor in anchorTagList:
        insert_counter += insertPageURL({"url": anchor['href']})

    print("INSERTED " + str(insert_counter) + " NEW URLS" )
    return;

def mass_url_parse():
    sourceURLsList = getSourceURLs()

    sourceURLsList = sourceURLsList

    for parsedURL in sourceURLsList:
        #find pages
        pageAnchorTagList = HTMLDecomposer.getPageAnchorTags(SOURCE_WEBSITE_HOST + parsedURL['url'])

        #add current url to url_pages
        insertPageURL({"url": parsedURL['url']})
            
        #add pages url
        for pageAnchor in pageAnchorTagList:
            insertPageURL({"url": pageAnchor['href']})
        
    return;

def update_url_type():
    sourceURLsList = getSourceURLs()
    sourceURLsList = sourceURLsList.limit(1)

    for parsedURL in sourceURLsList:
        if(HTMLDecomposer.isCategoryURL(SOURCE_WEBSITE_HOST + parsedURL['url'])):
            updateURLType(parsedURL)
    
    return

def collect_emails():
    pageURLsList = getPageURLs()
    pageURLs = pageURLsList.limit(1)

    for pageURL in pageURLs:
        parsed_html = HTMLDecomposer.parseHTML(SOURCE_WEBSITE_HOST + pageURL['url'])

        companyContainerList = HTMLDecomposer.getCompanyContainers(parsed_html)

        for companyContainer in companyContainerList:
            
            companyTitle = HTMLDecomposer.getCompanyTitle(companyContainer);
            print(companyTitle)
            
            email = HTMLDecomposer.getEmail(companyContainer);
            print(email)
        
            website = HTMLDecomposer.getWebsite(companyContainer);
            print(website)


if(len( sys.argv ) <= 1):
    print("Wrong Parameters")
    exit();


if( sys.argv[1] == MODE_TYPE_URL and 
    len(sys.argv) > 1 ):
    url_parse();
elif (  sys.argv[1] == MODE_TYPE_PARSE_PAGE_URLS and 
        len(sys.argv) > 1 ):
    url_parse_page_url();
elif (  sys.argv[1] == MODE_TYPE_MASS_PAGE_URL_PARSING ) :
    mass_url_parse();
elif (  sys.argv[1] == MODE_TYPE_UPDATE_URL_TYPE ) :
    update_url_type();
elif (  sys.argv[1] == MODE_TYPE_COLLECT_EMAILS ) :
    collect_emails();