import os
import django
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")
django.setup()

from quotesapp.models import Quote, Tag
from authorsapp.models import Author

uri = "mongodb+srv://admin:qwertyu@cluster0.upbkmny.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.authors

def seed_authors():
    authors = db.author.find()

    for author in authors:
        author_obj = Author(fullname=author["fullname"], born_date=author["born_date"],
                            born_location=author["born_location"], description=author["description"])
        author_obj.save()


seed_authors()


def seed_tags():
    quotes = db.quote.find()

    for quote in quotes:
        for tag in quote["tags"]:
            Tag.objects.get_or_create(name=tag)


seed_tags()


def seed_quotes():
    quotes = db.quote.find()

    for quote in quotes:
        tags = []
        print(quote["tags"])
        for tag in quote["tags"]:
            tags.append(Tag.objects.get(name=tag))

        quote_obj = Quote(quote=quote["quote"], tags=tags, author_id=quote["author"])
        quote_obj.save()


seed_quotes()
