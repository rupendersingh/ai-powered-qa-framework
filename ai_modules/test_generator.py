from openai import OpenAI
from ai_modules.llm_client import ask_llm
import os
import json

def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set")
    return OpenAI(api_key=api_key)

#client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYS_PROMPT = """
You are a senior QA engineer.

Generate test cases in STRICT JSON format.

Example:

[
  {
    "name": "Valid login",
    "steps": ["Enter valid username", "Enter valid password", "Click login"],
    "expected": "User lands on dashboard",
    "priority": "High"
  }
]

Rules:
- Output ONLY JSON array
- No explanation
- No markdown
- Follow exact schema
"""

def generate(page_desc: str, rules: list, retries=2) -> list:
    
    # 🔹 MOCK MODE (fallback when no API or quota)
    """ if not os.getenv("OPENAI_API_KEY") or os.getenv("MOCK_AI") == "true":
        return [
            {
                "name": "Valid login",
                "steps": ["Enter valid username", "Enter valid password", "Click login"],
                "expected": "User redirected to dashboard",
                "priority": "High"
            },
            {
                "name": "Invalid password",
                "steps": ["Enter valid username", "Enter wrong password", "Click login"],
                "expected": "Error message displayed",
                "priority": "High"
            }
        ]"""

    client = get_client()

#for attempt in range(retries):
    user_prompt = f"Page: {page_desc}\nRules:\n" + "\n".join(f"- {r}" for r in rules)

    raw = ask_llm(SYS_PROMPT, user_prompt,temperature=0)
    return json.loads(raw)