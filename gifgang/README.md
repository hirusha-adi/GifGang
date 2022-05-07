Basic Usage Demonstration for the GifGang python module

```python
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

# Cats
obj = sfw.Cats()
x = obj.theCatAPI(limit=5, size="med", mime_types="jpg,gif,png",
                  order="RANDOM", has_breeds=0)
x = obj.CatsAsAService.image(text=None, size="med", color=None, type=None,
                             filter=None, width=None, height=None)
x = obj.CatsAsAService.gif(text=None, size="med", color=None, type=None,
                           filter=None, width=None, height=None)

# Dogs
obj = sfw.Dogs()
x = obj.images(limit=5)


# NSFW Classes Usage Demonstration
# -----------------------------------------------------

# Eporner
obj = nsfw.Eporner()
x = obj.random(limit=5, thumbsize="big", order="top-weekly", format="json")
x = obj.search(query="hardcore", limit=5, thumbsize="big",
               order="top-weekly", format="json")

# RedTube
obj = nsfw.RedTube()
x = obj.random(size="big", output="json")
x = obj.search(query="hardcore", size="big", output="json")
x = obj.stars(page="1", output="json")
```
