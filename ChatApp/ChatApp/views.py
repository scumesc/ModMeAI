import json
import openai
from settings import ai_token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

openai.api_key = ai_token

@csrf_exempt
@require_POST
def handle_request(request):
    data = request.body.decode('utf-8')
    json_data = json.loads(data)
    user_input = json_data.get("user_input")

    if user_input:
        assistant_response = funcgpt(user_input)
        return JsonResponse({"assistant_response": assistant_response})
    else:
        return JsonResponse({"error": "Invalid request"})

def funcgpt(user_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "ты ассистент-помощник"},
            {"role": "user", "content": user_prompt},
        ]
    )

    return response['choices'][0]['message']['content']
