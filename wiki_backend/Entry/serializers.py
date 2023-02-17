from Entry.models import Entry, Client

from django.contrib.auth import authenticate

from rest_framework import serializers

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id','client','title','create_date']

class CreateEntrySerializer(serializers.Serializer):
    content = serializers.JSONField(
        label='content'
    )

    title = serializers.CharField(
        label='title'
    )

    def validate(self, attrs):
        content = attrs.get('content')
        title = attrs.get('title')

        if content is None or title is None:
            raise serializers.ValidationError("the content or title cannot be none", code="400")
        
        # create a post
        request =self.context.get('request')
        client = Client.objects.get(user = request.user)
        
        entry = Entry.objects.create(client = client, content = content, tag ='',title=title)
        attrs['id'] = entry.id
        return attrs 