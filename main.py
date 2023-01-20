import sys;
from HTMLDecomposer import HTMLDecomposer
from db import insertURL;


if(len( sys.argv ) <= 1):
    print("Please pass URL")
    exit();

anchorTagList = HTMLDecomposer.getAnchorTags(sys.argv[1])

insert_counter = 0;
for anchor in anchorTagList:
    insert_counter += insertURL({"url": anchor['href']})

print("INSERTED " + str(insert_counter) + " NEW URLS" )