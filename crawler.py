import sys;
from HTMLDownloader import HTMLDownloader;


if(len( sys.argv ) <= 1):
    print("Please pass URL")
    exit();

html = HTMLDownloader.getHTML(sys.argv[1])
print(html);