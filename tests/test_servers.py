from servers.calculator.server import add, divide, multiply, subtract
from servers.notes.server import get_note, list_notes, save_note
from servers.text_tools.server import reverse_text, slugify, word_count
from servers.time_tools.server import timestamp_to_iso


def test_calculator_tools():
    assert add(2, 3) == 5
    assert subtract(5, 3) == 2
    assert multiply(4, 3) == 12
    assert divide(8, 2) == 4


def test_calculator_rejects_zero_division():
    try:
        divide(1, 0)
    except ValueError as exc:
        assert "zero" in str(exc).lower()
    else:
        raise AssertionError("divide should reject zero")


def test_text_tools():
    assert word_count("one two three") == 3
    assert reverse_text("MCP") == "PCM"
    assert slugify("Hello, MCP Server!") == "hello-mcp-server"


def test_time_tools():
    assert timestamp_to_iso(0) == "1970-01-01T00:00:00+00:00"


def test_notes_tools():
    title = "test-note"
    assert save_note(title, "hello") == title
    assert title in list_notes()
    assert get_note(title) == "hello"
