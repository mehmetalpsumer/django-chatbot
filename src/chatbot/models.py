from django.db import models


class UserMessage(models.Model):
    uid = models.CharField(max_length=12)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    @classmethod
    def create(cls, uid, message):
        user_message = cls(uid=uid, message=message)
        return user_message

    def __str__(self):
        return '{}: {}'.format(self.uid, self.message)


class BotMessage(models.Model):
    response_to = models.ForeignKey(UserMessage, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    @classmethod
    def create(cls, response_to, message):
        bot_message = cls(response_to=response_to, message=message)
        return bot_message

    def __str__(self):
        return '{}: {}'.format(self.response_to, self.message)
