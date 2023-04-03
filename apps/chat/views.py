import openai
from django.shortcuts import render
from .models import ChatbotMessage
openai.api_key = "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" #GPT-3 API key


def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        # Generate chatbot response using GPT-3
        response = generate_response(user_input)
        # Save the user input and chatbot response to the database
        chatbot_message = ChatbotMessage(user_input=user_input, chatbot_response=response)
        chatbot_message.save()
    else:
        response = ""
    # Get the last 10 chatbot messages from the database
    chatbot_messages = ChatbotMessage.objects.order_by('-timestamp')[:10]
    context = {'response': response, 'chatbot_messages': chatbot_messages}
    return render(request, 'chatbot/chatbot.html', context)


def generate_response(user_input):
    prompt = f"User: {user_input}\nChatbot:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["User:"]
    )
    return response.choices[0].text.strip()


# Define function to generate chatbot response
# def generate_response(user_input, chat_history=None):
#     prompt = f"You:{user_input}\nDoctorAI:"
#
#     if chat_history:
#         prompt = f"{chat_history}\n{prompt}"
#
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         temperature=0.5,
#         max_tokens=1024,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0,
#         stop=["User:"]
#     )
#
#     chat_history = f"{prompt}{response.choices[0].text.strip()}"
#
#     return response.choices[0].text.strip(), chat_history