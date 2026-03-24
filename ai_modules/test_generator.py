from openai import OpenAI
import os
import json

def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set")
    return OpenAI(api_key=api_key)

#client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYS_PROMPT = """You are a QA engineer.

Return ONLY a JSON array of test cases.

Each test case:
{
  "name": "string",
  "steps": ["step1", "step2"],
  "expected": "string",
  "priority": "High|Medium|Low"
}

No explanation. Only JSON.
"""

def generate(page_desc: str, rules: list, retries=2) -> list:
    
    # 🔹 MOCK MODE (fallback when no API or quota)
    if not os.getenv("OPENAI_API_KEY") or os.getenv("MOCK_AI") == "true":
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
        ]

    client = get_client()

    for attempt in range(retries):
        try:
            user_prompt = f"Page: {page_desc}\nRules:\n" + "\n".join(f"- {r}" for r in rules)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                temperature=0,
                messages=[
                    {"role": "system", "content": SYS_PROMPT},
                    {"role": "user", "content": user_prompt}
                ]
            )

            raw = response.choices[0].message.content.strip()
            return json.loads(raw)

        except Exception as e:
            if attempt == retries - 1:
                raise e