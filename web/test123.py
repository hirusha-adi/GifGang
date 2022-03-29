from utils import Important
from imgurpython import ImgurClient

client_id = Important.imgur_client_id
client_secret = Important.imgur_clinet_secret

client = ImgurClient(client_id, client_secret)

# Example request
items = client.gallery()
list1 = [item.link for item in items]
