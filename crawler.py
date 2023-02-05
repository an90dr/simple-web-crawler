import argparse

from HTMLDecomposer import HTMLDecomposer

parser = argparse.ArgumentParser(
                    prog = 'Crawler',
                    description = 'Crawl through a given url and export html elements',
                    epilog = 'Thank you')

#parser.add_argument('filename')           # positional argument
parser.add_argument('-u', '--url')      # option that takes a value
#parser.add_argument('-s', '--selector')
parser.add_argument('-e', '--export')
#parser.add_argument('-r', '--recursive',
#                    action='store_true')

args = parser.parse_args()
parsed_html = HTMLDecomposer.parseHTML(args.url)
htmlElements = parsed_html.body.select('.Search_Bar_Number .Search_Bar_a1');

file1 = open(args.export, 'w')

for element in htmlElements:
    file1.write(str(element) + '\n')

file1.close()

##print(htmlElements)