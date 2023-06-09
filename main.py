






# import openai
# from settings import ai_token
#
# openai.api_key = ai_token
#
# def funcgpt(user_prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "ты ассистент-помощник"},
#             {"role": "user", "content": user_prompt},
#         ]
#     )
#
#     print(response['choices'][0]['message']['content'])
#
#
# user_input = input("Введите текст: ")
#
# while user_input != "exit":
#     funcgpt(user_input)
#     user_input = input("Введите текст: ")
