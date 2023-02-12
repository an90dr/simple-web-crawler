from constants import NON_SECURE_PROTOCOL, SECURE_PROTOCOL


class DataManipulator:

    def resolveURL(args, href: str):
        if (args.domain_urls_only):
            if (args.domain in href):
                # Domain Urls Only and
                # Domain found in url
                return href
            elif (NON_SECURE_PROTOCOL not in href and
                  SECURE_PROTOCOL not in href):

                # Domain Urls Only
                # Domain found in url
                return args.domain + href
        elif (args.domain in href or
                NON_SECURE_PROTOCOL in href or
                SECURE_PROTOCOL in href):

            # Other Domains too
            # Domain found in url
            # Other Domains found
            return href
        else:
            # Other Domains too
            # Domain not in url
            # and no http or https found
            # so url is root-relative path
            return args.domain + href


    def elementsToHrefSet(args, urlList: list) -> set:
        hrefSet = set()
        for url in urlList:
            if url.has_key('href'):

                resolvedUrl = DataManipulator.resolveURL(args, url['href'])
                hrefSet.add(resolvedUrl)

        return hrefSet

        
    def addElementToSet(urls, targetSet):
        if isinstance(urls, set):
            for url in urls:
                targetSet.add(url)
        else:
            targetSet.add(urls)

                
    def addSetToIterationList(urlsSet, iterationList):
        if isinstance(urlsSet, set):
            for url in urlsSet:
                if (url not in iterationList):
                    iterationList.append(url)
        elif (isinstance(urlsSet, str)):
            iterationList.append(urlsSet)