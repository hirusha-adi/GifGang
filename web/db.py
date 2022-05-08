from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://135.181.82.175:27017/')
torrents = client['GifGang']['torrents']


class Torrents:

    def getAllTorrents():
        data = []

        # The second dict will show what info to get and what info to not get as in 1 and 0
        #   for i in result.find({}, {"title": 1, "size": 1, "link": 1, "se": 1, "le": 1, "page": 1}):
        # Not including it will return everything

        for i in torrents.find({}):
            data.append(i)
        return data

    def getTorrentsByFilter(_id=None, title=None, size=None, link=None, se=None, le=None, page=None):
        data = []

        query = {}

        if not(_id is None):
            query['_id'] = ObjectId(_id)

        if not(title is None):
            query['title'] = title

        if not(size is None):
            query['size'] = size

        if not(link is None):
            query['link'] = link

        if not(se is None):
            query['se'] = se

        if not(le is None):
            query['le'] = le

        if not(page is None):
            query['page'] = page

        for i in torrents.find(query):
            data.append(i)

        return data

    def updateTorrent(update, _id=None, title=None, size=None, link=None, se=None, le=None, page=None):
        query = {}

        if not(_id is None):
            query['_id'] = ObjectId(_id)

        if not(title is None):
            query['title'] = title

        if not(size is None):
            query['size'] = size

        if not(link is None):
            query['link'] = link

        if not(se is None):
            query['se'] = se

        if not(le is None):
            query['le'] = le

        if not(page is None):
            query['page'] = page

        torrents.find_one_and_update(
            {query},
            {"$set": update},
            upsert=True
        )

    def getTorrentByTitle(title):
        # https://stackoverflow.com/questions/10610131/checking-if-a-field-contains-a-string
        # https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362
        data = []
        for i in torrents.find({
            "title": {
                "$regex": f'.*{title}*.'
            }
        }):
            data.append(i)
        return data


x = Torrents.getTorrentByTitle(title="ABV")
print(x)