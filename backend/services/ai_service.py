import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def analyze_symptoms(symptoms: str):

    try:
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            return "Error: GROQ_API_KEY not found"

        client = Groq(api_key=api_key)

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": f"My symptoms are {symptoms}. Suggest possible illness and precautions."}
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"AI Error: {str(e)}"