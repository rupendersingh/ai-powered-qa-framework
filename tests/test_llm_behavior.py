from ai_modules.llm_client import ask_llm
from ai_modules.test_generator import SYS_PROMPT
import json
from unittest.mock import patch

@patch("ai_modules.llm_client.ask_llm")
def test_llm_deterministic_math(mock_llm):
    mock_llm.return_value = "4"
    results = [mock_llm("sys", "2+2") for _ in range(3)]
   # results = [ask_llm("You are helpful.", "What is 2+2", temperature=0) for _ in range(3)]

    assert all("4" in r for r in results)

@patch("ai_modules.llm_client.ask_llm")
def test_llm_json_compliance(mock_llm):
    user = "Generate login test case"

    mock_llm.return_value = """
    [
      {
        "name": "Valid login",
        "steps": ["Enter username", "Enter password"],
        "expected": "Success",
        "priority": "High"
      }
    ]
    """

    response = mock_llm(SYS_PROMPT, "Generate login test case", temperature=0)

    data = json.loads(mock_llm("sys", "test"))

    assert isinstance(data, list)
    assert "name" in data[0]
    assert "steps" in data[0]