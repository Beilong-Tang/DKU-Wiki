from Entry.models import Entry

from django.contrib.auth import authenticate

from rest_framework import serializers

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id','client','title','create_date']

