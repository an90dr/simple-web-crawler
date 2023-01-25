import sys;
from HTMLDecomposer import HTMLDecomposer
from constants import MODE_TYPE_URL
from db import insertURL;

   
def url_parse():
    anchorTagList = HTMLDecomposer.getAnchorTags(sys.argv[2])

    insert_counter = 0;
    for anchor in anchorTagList:
        insert_counter += insertURL({"url": anchor['href']})

    print("INSERTED " + str(insert_counter) + " NEW URLS" )
    return;

def url_parse_page_url():
    #anchorTagList = HTMLDecomposer.getPageAnchorTags(sys.argv[2])

    anchorTagList = HTMLDecomposer.getPageAnchorTags('https://www.oncyprus.com/gr/dir/cyprus_renovations,3.html')

    insert_counter = 0;
    for anchor in anchorTagList:
        insert_counter += insertURL({"url": anchor['href']})

    print("INSERTED " + str(insert_counter) + " NEW URLS" )
    return;

if(len( sys.argv ) <= 1):
    print("Please pass URL")
    exit();


if( sys.argv[1] == MODE_TYPE_URL and 
    len(sys.argv) > 1 ):
    url_parse();
elif ( sys.argv[1] == MODE_TYPE_PARSE_PAGE_URLS and 
    len(sys.argv) > 1 ):
    url_parse_page_url();
   