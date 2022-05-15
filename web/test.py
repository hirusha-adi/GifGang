import itertools

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

all_items_list = list(itertools.chain(one, two))
final_list = []
for i in all_items_list:
    if not i in final_list:
        final_list.append(i)

print(len(final_list))
