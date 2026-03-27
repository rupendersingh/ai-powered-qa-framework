import openai
import json
import os

SYS = """You are a QA test failure analyst.

Return ONLY JSON:
{"error_type":"string","likely_cause":"string","suggested_fix":"string","confidence":"High|Med|Low"}
"""


def analyze(screenshot_path, log_text, page_title):
    client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    prompt = f"""
    Page Title: {page_title}

    Failure Log:
    {log_text[-2000:]}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "system", "content": SYS},
            {"role": "user", "content": prompt}
        ]
    )

    return json.loads(response.choices[0].message.content.strip())