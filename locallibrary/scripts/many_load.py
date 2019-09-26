import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, States, Region, Iso, Site

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()
    # Format
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(category1=row[7])
        s, created = States.objects.get_or_create(states1=row[8])
        r, created = Region.objects.get_or_create(region1=row[9])
        i, created = Iso.objects.get_or_create(iso1=row[10])

        try:
            y = int(row[3])
        except:
            y = None
        site = Site(name=row[0], description=row[1], justification=row[2], year=y, longitude=row[4], latitude=row[5], area_hectares=row[6], category=c, states=s, region=r, iso=i)
        site.save()







