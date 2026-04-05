from ai_modules.llm_client import ask_llm
from unittest.mock import patch,MagicMock

@patch("ai_modules.llm_client.client.chat.completions.create")
def test_llm_cache(mock_create):
    # Mock API response
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content="4"))
    ]

    mock_create.return_value = mock_response


    r1 = ask_llm("You are helpful", "What is 2+2?", temperature=0)
    r2 = ask_llm("You are helpful", "What is 2+2?", temperature=0)

    assert r1 == r2
    # 🔥 Critical assertion
    assert mock_create.call_count == 1