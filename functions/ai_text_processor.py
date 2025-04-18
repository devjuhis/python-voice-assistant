from groq import Groq
from functions.read_config import read_config

def process_voice_prompt(raw_text):
    """
    Handles speech recognition text using Groq AI.
    Returns the AI response as a string and speaks it aloud.
    """

    groq_api_key = read_config()
    client = Groq(api_key=groq_api_key)

    prompt = f'"{raw_text}"'

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a speech prompt processor. Your job is to clean up user speech input by removing disfluencies "
                        "such as 'um', 'uh', and repeated or filler words, while preserving the intended meaning. "
                        "Return only the cleaned-up version of the prompt as a single string.\n\n"
                        "You must also recognize and preserve specific **commands** exactly as they are spoken. "
                        "Do not clean, rephrase, or change commands in any way.\n\n"
                        "### Commands include (but are not limited to):\n"
                        "- command mode\n"
                        "- AI mode\n"
                        "- text mode\n"
                        "- delete all\n"
                        "- erase\n"
                        "- delete word\n"
                        "- enter\n\n"
                        "You must be able to clearly **distinguish between normal user text input and commands**. "
                        "If the input is a command, return only the command exactly as spoken. "
                        "If the input is normal text, return the cleaned-up version."
                    )

                },
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
        print("AI processed text:", response)
        return response

    except Exception as e:
        error_msg = f"Error in text prosessing: {str(e)}"
        print(error_msg)
        return error_msg
