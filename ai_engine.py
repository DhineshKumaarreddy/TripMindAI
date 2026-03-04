import os
from dotenv import load_dotenv
from google import genai
from prompt_builder import build_prompt

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_itinerary(destination, days, budget, style, interests, start_city, traveler_type):
    prompt = build_prompt(destination, days, budget, style, interests, start_city,traveler_type)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text