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
x = sfw.Giphy.random(limit=5)
x = sfw.Giphy.trending(limit=5, offset=5)
x = sfw.Giphy.search(query="cats", limit=5, offset=5)

# Picsum
x = sfw.Picsum.images(limit=5, height=500, width=200)


