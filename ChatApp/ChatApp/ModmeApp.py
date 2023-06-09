import openai
from settings import ai_token

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

openai.api_key = ai_token

@csrf_exempt
def handle_request(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")

        assistant_response = funcgpt(user_input)  # Вызов функции funcgpt, реализованной в вашем коде

        return JsonResponse({"assistant_response": assistant_response})

def funcgpt(user_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "ты ассистент-помощник"},
            {"role": "user", "content": user_prompt},
        ]
    )

    return response['choices'][0]['message']['content']
