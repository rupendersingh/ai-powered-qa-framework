import json
from test_generator import generate

PAGE_DESC = "Login page with username, password fields and submit button"

RULES = [
    "Username and password are mandatory",
    "Invalid login shows error message",
    "Valid login redirects to dashboard"
]

def main():
    test_cases = generate(PAGE_DESC,RULES)
    with open("tests/generated/login_tests.json", "w") as f:
        json.dump(test_cases, f, indent=2)
    print(f"Generated {len(test_cases)} test cases")

if __name__ == "__main__":
    main()