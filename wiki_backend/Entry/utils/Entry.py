## including entry methods
from ..models import client_entry_updated

def record(client,entry,content_new):
    '''
    save the record into client_entry_updated field
    '''
    client_entry_updated.objects.create(
        client = client,
        entry = entry,
        content_new = content_new
    )

    return 
