from Entry.models import Entry
from django.db.models import Q


def getEntry(tags:list,search:str):
    """
    get the entry based on tags and search 
    problem with current sqlite database, json contain seems not to be supported, it is case insensitive now.
    """
    if search == None and tags==['']:
        return Entry.objects.all()
    
    elif search !=None and tags==['']:
        return Entry.objects.filter(title__contains=search)
    
    elif search == None and tags!=['']:
        q = Q(tag__icontains=tags[0])

        for i in range(1,len(tags)):
            q = q & Q(tag__icontains=i)

        return Entry.objects.filter(q)
    
    elif search !=None and tags!=['']:
        
        q= Q(title__contains=search)
        for i in tags:
            q = q & Q(tag__icontains=i)
        return Entry.objects.filter(q)
