from Entry.models import *
from Entry import serializers

from .utils.helper import getEntry


from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

# show all the posts or the post that is related to search result
class PostList(APIView):

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = (permissions.AllowAny,)

    def get(self,request):
        tags = request.query_params.get("tags").split(",") # array of tags
        print(tags)
        search = request.query_params.get('search')
        entries = getEntry(tags=tags, search=search)
        serializer = serializers.EntrySerializer(entries,many=True)
        response = Response(serializer.data)

        return response

    pass

# show the detail of each post
class detail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self,request,id):
        entry = Entry.objects.get(id=id)
        serializer = serializers.DetailEntrySerializer(entry)
        return Response(serializer.data)

class CreateEntry(APIView):
    """
    Create an entry
    """
    # authentication_classes = [authentication.SessionAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self,request):
        serializer = serializers.CreateEntrySerializer(data=request.data, context={'request':self.request})
        serializer.is_valid(raise_exception=True)
        print(request.data)
        return Response({'id':serializer.validated_data.get('id')})

        pass

class TagList(APIView):

    permission_classes=(permissions.AllowAny,)

    def get(self, request):
        tags = Tags.objects.all()
        serializer = serializers.TagSerializer(tags,many=True)
        return Response(serializer.data)

    