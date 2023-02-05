from Entry.models import *
from Entry import serializers



from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

# show all the posts or the post that is related to search result
class index(APIView):

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = (permissions.AllowAny,)

    def get(self,request):
        search = request.query_params.get('search')
        if search == None:
            entries = Entry.objects.all()
        else:
            entries = Entry.objects.filter(title__contains=search)
        serializer = serializers.EntrySerializer(entries,many=True)
        response = Response(serializer.data)

        return response

    pass

# show the detail of each post
class detail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self,request,id):
        entry = Entry.objects.get(id=id)
        return Response({'entry':entry.content})

class CreateEntry(APIView):
    """
    Create an entry
    """
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self,request):
        pass