from pymongo import MongoClient

from constants import DB_COLLECTION_PAGE_URL_NAME, DB_COLLECTION_URL_NAME, DB_COLLECTION_EMAIL_NAME, DB_CONNECTION_STRING

def get_database():
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(DB_CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['company_emails']
  

def insertEmail(document):

    dbname = get_database()
    #collection_name = dbname[DB_COLLECTION_EMAIL_NAME]
    
    #find = collection_name.count_documents(document)

    #if find != None & find.__len__() == 0 :
    #    collection_name.insert_one(document)

def insertURL(document):

    dbname = get_database()
    collection_name = dbname[DB_COLLECTION_URL_NAME]
    
    if collection_name.count_documents(document) == 0 :
        collection_name.insert_one(document)
        return 1;
    return 0; 

def insertPageURL(document):

    dbname = get_database()
    collection_name = dbname[DB_COLLECTION_PAGE_URL_NAME]
    
    if collection_name.count_documents(document) == 0 :
        collection_name.insert_one(document)
        return 1;
    return 0; 


def getSourceURLs():
    dbname = get_database()
    collection_name = dbname[DB_COLLECTION_URL_NAME]

    return collection_name.find()


def updateURLType(urlObject):
    dbname = get_database()
    collection_name = dbname[DB_COLLECTION_URL_NAME]

    collection_name.update_one({
        '_id': urlObject['_id']
        },
        {"$set":{"type": "CATEGORY"}}, 
    upsert=False)


    return;


