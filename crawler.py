import argparse
import collections.abc
import bs4

from HTMLDecomposer import HTMLDecomposer

anchorList = [];
processedAnchorTagList = [];

def getAnchorTags(url):
    parsed_html = HTMLDecomposer.parseHTML(url)
    anchorList = parsed_html.body.select('a');
    return anchorList

def appendElementToList(urls, list):
    if type(urls) is bs4.ResultSet:
        for url in urls:
            if url not in list :
                if (args.domain in url['href'] or 
                    'http://' in url['href'] or 
                    'https://' in url['href']):
                    list.append(url['href']) 
                else: 
                    list.append(args.domain + url['href']);
    else:
        if urls not in list :
            list.append(urls);


parser = argparse.ArgumentParser(
                    prog = 'Crawler',
                    description = 'Crawl through a given url and export html elements',
                    epilog = 'Thank you')


parser.add_argument('-u', '--url')      # option that takes a value
parser.add_argument('-s', '--selector')
parser.add_argument('-e', '--export')
parser.add_argument('-d', '--domain')
parser.add_argument('-r', '--recursive',
                    action='store_true')

args = parser.parse_args()
parsed_html = HTMLDecomposer.parseHTML(args.url)
htmlElements = parsed_html.body.select(args.selector);

if(args.recursive):
    
    #add args.url list to processed list
    appendElementToList(args.url, processedAnchorTagList);
    
    #get first url anchor list
    firstPageAnchorList = parsed_html.body.select('a');
    appendElementToList(firstPageAnchorList, anchorList);
    
    for anchor in anchorList:
        parsed_html = HTMLDecomposer.parseHTML(anchor)
        htmlElements = parsed_html.body.select('a');
        appendElementToList(firstPageAnchorList, anchorList);
        appendElementToList(anchor, processedAnchorTagList);
        print(str(len(processedAnchorTagList)) + " / " + str(len(anchorList)));

file1 = open(args.export, 'w')

for element in htmlElements:
    file1.write(str(element) + '\n')

file1.close()



