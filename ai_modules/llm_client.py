import os
import openai
import time
from openai import RateLimitError
from utils.llm_cache import get_cached, set_cache

CACHE_FILE = "utils/llm_cache.json"
client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
def ask_llm(system:str, user : str, temperature : float = 0, retries: int =3) -> str:
    """
    Central LLM wrapper with retry + control
    """
    # ✅ Step 1: Check cache
    cached = get_cached(system,user,temperature)
    if cached:
        print("CACHE HIT")
        return cached

     # ❌ Step 2: Call API if not cached
    for attempt in range(retries +1):
        try:
            response = client.chat.completions.create(
                model= "gpt-3.5-turbo",
                temperature= temperature,
                messages=[
                    {"role": "system", "content":system},
                    {"role": "user", "content":user}
                ]
            )
            output = response.choices[0].message.content.strip()

            # ✅ Step 3: Save to cache
            set_cache(system, user, temperature,output)
            return output
        
        except Exception as e:
            if attempt == retries:
                raise e
