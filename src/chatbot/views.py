import uuid
from django.shortcuts import render


def index(request):
    context = {
        'uid': uuid.uuid4().hex[:12].upper()
    }
    return render(request, 'chatbot/index.html', context=context)
