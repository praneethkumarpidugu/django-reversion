from django.http import HttpResponse
from reversion.models import Version
from django.contrib.admin.models import LogEntry
import json

def history_list(request):
    history_list = Version.objects.all().order_by('-revision__date_created')

    data = []

    for i in history_list:
        data.append({
            'date_time': str(i.revision.date_created),
            'user': str(i.revision.user),
            'object': i.object_repr,
            'type': i.content_type.name,
            'comment': i.revision.comment
        })

    data_ser = json.dumps(data)
    return HttpResponse(data_ser, content_type="application/json")