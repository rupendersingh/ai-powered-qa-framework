import openai, json, os
SYS = """You are a QA test failure analyst.

Return ONLY JSON:
{"error_type":"string","likely_cause":"string","suggested_fix":"string","confidence":"High|Med|Low"}

No explanation. No markdown. Only JSON."""

def analyze(log_text: str, page_title: str)-> dict:
    client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    prompt = f"""Page Title: {page_title}
        Failure Log:
        {log_text[-2000:]}
        """
    
    response = client.chat.completions.create(
        model= "gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "system", "content": SYS},
            {"role": "user", "content": prompt}
        ]
    )

    return json.loads(response.choices[0].message.content.strip())