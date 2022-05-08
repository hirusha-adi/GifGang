from pymongo import MongoClient
from bson import ObjectId

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://135.181.82.175:27017/')

db = client['GifGang']

torrents = db['torrents']
admin = db['admin']

# The second dict will show what info to get and what info to not get as in 1 and 0
#   for i in result.find({}, {"title": 1, "size": 1, "link": 1, "se": 1, "le": 1, "page": 1}):
# Not including it will return everything

for i in torrents.find({}):
    print(i)

# Find one by ID and update
torrents.find_one_and_update(
    {"_id": ObjectId("6277d5c4ddec3b4a82b7f2cb")},
    {"$set": {
        "testing": "sex"
    }
    },
    upsert=True
)

print("="*50)
for i in torrents.find({}):
    print(i)
