#!/bin/sh
# database population
# add listings to database for testing purpose
#python3 manage.py shell


import random
from home.models import Listing
from django.utils import timezone
from django.conf import settings


Listing.objects.all().delete()
street_name = ["Hydraulic Road","Hydraulic Road","Idlewood Drive","Ilex Court","Incarnation Drive","Independence Way","India Road","Indian Laurel Road","Indian Spring Road","Ingle Court","Inglecress Drive","Ingleridge Farm","Ingleside Drive","Ingleside Farm Lane","Ingleside Lane","Inglewood Court","Inglewood Drive","Inn Drive","Innovation Drive","Insurance Lane","Interstate 64","Interstate 64","Ipswich Place","Ironwood Lane","Isolina Lane","Ivy Cmns","Ivy Creek Drive","Ivy Creek Farm Road","Ivy Depot Road","Ivy Drive","Ivy Farm Drive","Ivy Hill Lane","Ivy Lane","Ivy Ridge Road","Ivy Road","Ivy Road","Ivy Rose Lane","Ivy Springs Lane","Ivy Vista Drive","Ivywest Lane","Ivywood Lane","James Lane","James Monroe Parkway","Jamestown Drive","Jasmine Terrace","Jeanette Lancaster Way - University Of Virginia","Jeffers Drive","Jefferson Court","Jefferson Lake Drive","Jefferson Park Avenue","Jefferson Park Avenue","Jefferson Park Circle","Jefferson Street","Jessies Lane","Jester Lane","John Street","Jones Street","Jordan Lane","Journeys End Lane","Judge Lane","Jumpers Run","Juniper Lane","Jurlando Lane","Kearsarge Circle","Keelona Farm","Keiser Ridge Road","Keith Valley Road","Kellogg Drive","Kelly Avenue","Kelsey Court","Kelsey Drive","Kemper Lane","Kendalwood Lane","Kenridge Court","Kensington Avenue","Kent Road","Kent Terrace","Kenwood Circle","Kenwood Lane","Kenwood Lane","Kernwood Place","Kerry Lane","Key West Drive","Keystone Place","Kimbrough Circle","King George Circle","King George Circle","King Mountain Road","King Street","King William Drive","Kingston Road","Knightsbridge Court","Knoll Ridge Drive","Knoll Street","Labrador Lane","Lafayette Lane","Lafayette Street","Lake Albemarle Road","Lake Club Court","Lake Forest Drive","Lake Forest Lane","Lake Road","Lakeside Drive","Lakeview Drive","Lambeth Lane","Lambeth Lane","Lambs Lane","Lambs Road","Lamkin Way","Lanark Farm","Lancaster Court","Landin Circle","Landmark Drive","Landonia Circle"]
random_words = ["patterner","ambroise","hiatuses","unscanned","pow","mickies","cherryvale","holforging","translucid","kiang","enful","topside","oillessness","radiantly","brooksville","araatuba","hyperfastidious","preknowing","befoul","reoccupied","liberality","repelling","metrology","antifeudalism","guilelessly","hastefully","perkasie","hypothetically","welkom","amarna","abasement","badge","eduardo","perishableness","chorioid","harambee","feb","germanophile","sniffish","woesome","cauterization","ferriage","burble","confining","touse","bacilliform","roughdry","greasiness","banning","blackness","misclaim","epitheliomas","rostrated","battlefront","semidefinite","antitaxation","epistler","vetting","collotyped","menses","ethiopic","unnihilistic","exclusioner","baseman","asparagus","horses","unputridity","seashell","imbibed","harim","deluge","obscurant","eerier","alluvion","overboot","mercilessly","compassable","benzylidene","nephralgic","burnisher","sublegislature","genucius","toward","sheefish","overmarch","experientially","unsiding","dodecaphony","softa","chirpy","untwining","pigface","spill","uhrichsville","hatboro","unshunnable","locomotion","prestandardizing","annville","dropwort"]
for iteration in range(0,15):
    add = street_name[random.randint(0, len(street_name)-1)] + " "+str(random.randint(0,9999))
    realtor = street_name[random.randint(0, len(street_name)-1)] + " Property"
    site = "_".join(street_name[random.randint(0, len(street_name)-1)].split()) + ".com"
    number = str(random.randint(100,999)) + "-" + str(random.randint(100,999)) + "-" +str(random.randint(1000,9999))
    random.shuffle(random_words)
    features_l = []
    for i in range(0,10):
        if random.randint(0,2) == 1:
            features_l.append(i)
    des = " ".join(random_words)
    q = Listing(pub_date = timezone.now(),
                    address = add,
                    realtor_agent = realtor,
                    realtor_site = site,
                    phone_number = number,
                    description = des,
                    beds = random.randint(1,6),
                    baths = random.randint(1,6),
                    price = random.randint(1,5000),
                    ratings = random.randint(1,6),
                    number_of_ratings = random.randint(1,100),
                    reviews = "[]")
    q.set_features(features_l)
    q.save()
print("Success")