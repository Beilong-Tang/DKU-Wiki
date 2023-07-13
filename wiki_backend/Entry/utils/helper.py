from Entry.models import Entry
from django.db.models import Q
import os
import math

page_number = int(os.environ.get('page_number'))

def getEntry(tags:list,search:str,page:str):
    """
    get the entry based on tags and search 
    problem with current sqlite database, json contain seems not to be supported, it is case insensitive now.
    """
    page = int(page)
    if search == None and tags==['']:
        e =  Entry.objects.all().order_by("-create_date")
        return e[page_number*page:page_number*(page+1)], int(math.ceil(e.count()/page_number))
    
    elif search !=None and tags==['']:
        e = Entry.objects.filter(title__icontains=search).order_by("-create_date")
        return e[page_number*page:page_number*(page+1)], int(math.ceil(e.count()/page_number))
    
    elif search == None and tags!=['']:
        q = Q(tag__icontains=tags[0])

        for i in range(1,len(tags)):
            q = q & Q(tag__icontains=i)
        e = Entry.objects.filter(q).order_by("-create_date")
        return e[page_number*page:page_number*(page+1)], int(math.ceil(e.count()/page_number))
    
    elif search !=None and tags!=['']:
        
        q= Q(title__contains=search)
        for i in tags:
            q = q & Q(tag__icontains=i)

        e = Entry.objects.filter(q).order_by("-create_date")
        return e[page_number*page:page_number*(page+1)], int(math.ceil(e.count()/page_number))
