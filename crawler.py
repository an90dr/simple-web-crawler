import argparse
from FileProcessing.File import File

from DataManipulator.DataManipulator import DataManipulator
from Numbers.Numbers import Numbers
from constants import NON_SECURE_PROTOCOL, SECURE_PROTOCOL
from personal.HTMLDecomposer import HTMLDecomposer

anchorSet = set()
processedAnchorTagSet = set()
iterationList = []

parser = argparse.ArgumentParser(
    prog='Crawler',
    description='Crawl through a given url and export html elements',
    epilog='Thank you')


parser.add_argument('-u', '--url')      # option that takes a value
parser.add_argument('-s', '--selector')
parser.add_argument('-e', '--export')
parser.add_argument('-d', '--domain')
parser.add_argument('-duo', '--domain_urls_only',
                    action='store_true')
parser.add_argument('-r', '--recursive',
                    action='store_true')

args = parser.parse_args()
parsed_html = HTMLDecomposer.parseHTML(args.url)
htmlElements = parsed_html.body.select(args.selector)


if (args.recursive):

    # add args.url list to processed list
    DataManipulator.addElementToSet(args.url, processedAnchorTagSet)

    # get first url anchor list
    firstPageAnchorList = DataManipulator.elementsToHrefSet(args,parsed_html.body.select('a'))
    anchorSet = set(firstPageAnchorList)
    DataManipulator.addSetToIterationList(anchorSet, iterationList)

    for anchor in iterationList:
        parsed_html = HTMLDecomposer.parseHTML(anchor)
        if (parsed_html is not None and
                parsed_html.body is not None):

            hrefElements = DataManipulator.elementsToHrefSet(args, parsed_html.body.select('a'))
            DataManipulator.addElementToSet(hrefElements, anchorSet)
            DataManipulator.addSetToIterationList(anchorSet, iterationList)

            DataManipulator.addElementToSet(anchor, processedAnchorTagSet)

            progress = Numbers.resolveProgress(len(processedAnchorTagSet), len(anchorSet))
            print(progress)
            File.appendContents(args.export, anchor)

else:

    for element in htmlElements:
        if element.has_key('href'):
            url = DataManipulator.resolveURL(args, element['href'])
            File.appendContents(args.export, url)
