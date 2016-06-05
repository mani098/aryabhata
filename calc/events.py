from django_socketio import events
from models import CalcLog, User
from django.conf import settings
import json


@events.on_message(channel="calc_channel")
def message(request, socket, context, message):
    """
    Event handler for a room receiving a message. First validates a
    joining user's name and sends them the list of users.
    """

    qs = CalcLog.objects.all().order_by('-added_at')
    log_count = qs.count()

    if log_count >= settings.QUEUE_SIZE:
        qs.last().delete()

    request_user = User.objects.get(id=message.get('user_id'))

    CalcLog.objects.create(user=request_user,
                           equation=message.get('calculation'))
    # import pdb; pdb.set_trace()
    log_data = list(qs.values_list('equation', flat=True))

    socket.send_and_broadcast_channel(log_data)
