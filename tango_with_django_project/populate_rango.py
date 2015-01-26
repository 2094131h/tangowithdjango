import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
<<<<<<< HEAD

    python_cat = add_cat('Craig Hamill', 128, 64)

    add_page(cat=python_cat,
        title="My GitHub",
        url="https://github.com/2094131h",
        views=1)
    add_page(cat=python_cat,
        title="My Python Anywhere",
        url="https://www.pythonanywhere.com/user/2094131h/files/home/2094131h",
        views=1)

=======
>>>>>>> 12659ef... Chapter 4 - completed
    python_cat = add_cat('Python', 128, 64)


    add_page(cat=python_cat,
        title="Official Python Tutorial",
<<<<<<< HEAD
        url="http://docs.python.org/2/tutorial/",
        views=5)

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",
        views=20)

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",
        views=200)
=======
        url="http://docs.python.org/2/tutorial/")

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")
>>>>>>> 12659ef... Chapter 4 - completed

    django_cat = add_cat("Django", 64, 32)

    add_page(cat=django_cat,
        title="Official Django Tutorial",
<<<<<<< HEAD
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
        views=15)

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
        views=32)

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/",
        views=67)
=======
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")
>>>>>>> 12659ef... Chapter 4 - completed

    frame_cat = add_cat("Other Frameworks", 32, 16)

    add_page(cat=frame_cat,
        title="Bottle",
<<<<<<< HEAD
        url="http://bottlepy.org/docs/dev/",
        views=1000)

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org",
        views=290)
=======
        url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org")
>>>>>>> 12659ef... Chapter 4 - completed

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))


<<<<<<< HEAD
def add_page(cat, title, url, views):
=======
def add_page(cat, title, url, views=0):
>>>>>>> 12659ef... Chapter 4 - completed
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

<<<<<<< HEAD

=======
>>>>>>> 12659ef... Chapter 4 - completed
# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()

