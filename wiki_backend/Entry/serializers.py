import re

from Entry.models import Entry, Client, Tags

from .utils.tags import TagClass

from django.contrib.auth import authenticate

from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields= ['id','nickname']

class EntrySerializer(serializers.ModelSerializer):
    """
    Return id, client, title, create_date for searching
    """
    client = ClientSerializer()

    content_min = serializers.SerializerMethodField()

    def get_content_min(self, entry):
        content = entry.content
        # print(content)
        content = content[content.find("\n")+1:]
        content = content[:content.find("#")] 
        content = re.sub("\n+"," ", content)
        return content[:200]+"..."
        pass

    class Meta:
        model = Entry
        fields = ['id','client','title','create_date','content_min' ,'tag']

class DetailEntrySerializer(serializers.ModelSerializer):
    '''
    Return a content of an entry detailly 
    '''
    class Meta:
        model = Entry
        fields = ['id','client','title','create_date', 'tag', 'content']


# either create an entry or update an entry
class CreateEntrySerializer(serializers.Serializer):
    content = serializers.JSONField(
        label='content'
    )

    title = serializers.CharField(
        label='title'
    )

    tag = serializers.JSONField(
        label='tag'
    )

    def validate(self, attrs):
        content = attrs.get('content')
        title = attrs.get('title')
        tag = attrs.get('tag')

        if content is None or title is None:
            raise serializers.ValidationError("the content or title cannot be none", code="400")
        
        # create a post
        request = self.context.get('request')
        client = Client.objects.get(user = request.user)
        
        # Create a tag or update a current tag
        Tag = TagClass(tag=tag)
        
        # update an entry
        if (Entry.objects.filter(title=title).exists()):
            
            # update tag
            entry = Entry.objects.get(title=title)

            entry.tag = tag
            entry.content=content
            entry.save()

            Tag.modifyTag()
            
        # create a new entry
        else:
            entry = Entry.objects.create(client = client, content = content, tag = tag,title = title)
            Tag.addTag()

        attrs['id'] = entry.id
        return attrs 
    

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id','name','number','update_date']