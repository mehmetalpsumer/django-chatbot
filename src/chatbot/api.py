import json
import nltk
import numpy as np
import random
import string

from django.http import JsonResponse
from nltk.chat.util import Chat, reflections

from .models import UserMessage, BotMessage
from .pairs import pairs


def message(request):
    '''
    This endpoint receives message from user, processes it
    and returns the response of the chat bot.
    '''
    if request.method == 'POST':
        # Read and save user message
        incoming_data = json.loads(request.body)
        user_message = incoming_data['userMessage']
        user_message_obj = UserMessage.create(
            uid=incoming_data['uid'],
            message=user_message
        )
        user_message_obj.save()

        # Create bot message
        chat = Chat(pairs, reflections)
        user_message = user_message.lower()
        bot_message = chat.respond(user_message)

        # Create bot message object, save and send
        bot_message_obj = BotMessage.create(
            response_to=user_message_obj,
            message=bot_message
        )
        bot_message_obj.save()

        response = JsonResponse(bot_message, safe=False) 
        response.status_code = 201
        return response
    else:
        response = JsonResponse({'error': 'Invalid HTTP method.'})
        response.status_code = 404
        return response
