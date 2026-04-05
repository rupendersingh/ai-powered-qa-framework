from ai_modules.llm_client import ask_llm

SYSTEM = "You are a QA engineer. Return JSON only."
USER = "Generate 2 login test cases."

for t in [0, 0.5, 1.0]:
    print(f"\n---Temperature : {t} ---")
    print(ask_llm(SYSTEM, USER, temperature=t))

