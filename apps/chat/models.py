from django.db import models


class ChatbotMessage(models.Model):
    user_input = models.TextField()
    chatbot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_input} - {self.chatbot_response}"
