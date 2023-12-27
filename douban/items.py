# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item



class Movie(Item):
    title = Field()
    duration = Field()
    # douban_id = Field()
    type = Field()
    # cover = Field()
    # name = Field()
    # slug = Field()
    # year = Field()
    directors = Field()
    # writers = Field()
    actors = Field()
    # genres = Field()
    # official_site = Field()
    # regions = Field()
    # languages = Field()
    # release_date = Field()
    # mins = Field()
    # alias = Field()
    # imdb_id = Field()
    # douban_id = Field()
    douban_score = Field()
    # douban_votes = Field()
    # tags = Field()
    # storyline = Field()

class MovieHref(Item):
    href = Field()

class MovieComment(Item):
   
    content = Field()
    ip = Field()


