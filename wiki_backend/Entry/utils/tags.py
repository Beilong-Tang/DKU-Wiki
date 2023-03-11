from Entry.models import Tags

class TagClass:

    def __init__(self, tag:list):
        self.tag = tag
        self.addTag()
        
    def addTag(self):
        '''
        Create a tag if it is not there, or, update the tags
        '''
        # tag = Tags.objects.create(name=)
        for _item in self.tag:

            if Tags.objects.filter(name=_item).exists():
                tag = Tags.objects.get(name=_item)
                tag.number = tag.number + 1
                tag.save()
            else:
                tag = Tags.objects.create(name=_item, number = 1)
    
    
        
