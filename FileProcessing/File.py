class File:

    def appendContents(filepath, fileContent):
        try:
            file = open(filepath, 'a')
            file.write(str(fileContent) + '\n')
            file.close()
        except:
            print('Error while trying to write to file ' + filepath);