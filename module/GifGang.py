"""
Basic Usage Demonstration for the GifGang python module
"""

# Importing
# -----------------------------------------------------

# Import SFW classes
from gifgang import sfw

# Import NSFW Classes
from gifgang import nsfw


# SFW Classes Usage Demonstration
# -----------------------------------------------------

# Giphy
obj = sfw.Giphy()
x = obj.random(limit=5)
x = obj.trending(limit=5, offset=5)
x = obj.search(query="cats", limit=5, offset=5)

# Picsum
obj = sfw.Picsum()
x = obj.images(limit=5, height=500, width=200)

# Tenor
obj = sfw.Tenor()
x = obj.random(limit=5, locale="en_US", ar_range="all", contentfilter="off")
x = obj.search(query="random", limit=5, locale="en_US",
               ar_range="all", contentfilter="off")
