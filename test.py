import itertools

# http://rarbgenter.org/torrent/gl6uv19 - BEST

one = [
    "http://rarbgenter.org/torrent/tv85w3b",
    "http://rarbgenter.org/torrent/ctxnzeg",
    "http://rarbgenter.org/torrent/4wkbcm1",
    "http://rarbgenter.org/torrent/8nl3yfk",
    "http://rarbgenter.org/torrent/75eukng",
    "http://rarbgenter.org/torrent/qkf4u8c",
    "http://rarbgenter.org/torrent/cnvhorw",
    "http://rarbgenter.org/torrent/hg1l6bn",
    "http://rarbgenter.org/torrent/lvg83wh",
    "http://rarbgenter.org/torrent/rn4zqek"
]

two = [
    "http://rarbgenter.org/torrent/vfpdzcw",
    "http://rarbgenter.org/torrent/yv5rqsa",
    "http://rarbgenter.org/torrent/dm3hu48",
    "http://rarbgenter.org/torrent/t5giu9b",
    "http://rarbgenter.org/torrent/d4mtain",
    "http://rarbgenter.org/torrent/gdi8qmr",
    "http://rarbgenter.org/torrent/pne6uxr",
    "http://rarbgenter.org/torrent/vhfy9d4",
    "http://rarbgenter.org/torrent/2a54zxf",
    "http://rarbgenter.org/torrent/kolw485"
]

three = [
    "http://rarbgenter.org/torrent/dz64tbu",
    "http://rarbgenter.org/torrent/aznmut6",
    "http://rarbgenter.org/torrent/tkqj4pm",
    "http://rarbgenter.org/torrent/jg8avu3",
    "http://rarbgenter.org/torrent/iapv5sl"
]

all_items_list = list(itertools.chain(one, two, three))
final_list = []
for i in all_items_list:
    if not i in final_list:
        final_list.append(i)


print(len(final_list))
