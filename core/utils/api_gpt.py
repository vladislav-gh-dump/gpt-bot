import openai

from core.config import CONFIG

openai.api_key = CONFIG['OPENAI_API_KEY']


def get_content(messages: list[dict]):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages
        )

        return response['choices'][0]['message']['content']
    except Exception:
        return 'Упс... не удалось выполнить запрос'
