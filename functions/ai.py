from groq import Groq
from functions.read_config import read_config
from functions.speak import speak

def get_ai_response(prompt):

    groq_api_key = read_config()
    client = Groq(api_key=groq_api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "you are a helpful assistant. Your answers are short and concise."},
            {"role": "user", "content": prompt},
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.5,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )

    response = chat_completion.choices[0].message.content
    print(response)
    speak(response)
