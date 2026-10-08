from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Notes Server")
_notes: dict[str, str] = {}


@mcp.tool()
def save_note(title: str, content: str) -> str:
    """Save or replace an in-memory note and return its title."""
    clean_title = title.strip()
    if not clean_title:
        raise ValueError("Note title cannot be empty")
    _notes[clean_title] = content
    return clean_title


@mcp.tool()
def list_notes() -> list[str]:
    """Return saved note titles in alphabetical order."""
    return sorted(_notes)


@mcp.tool()
def get_note(title: str) -> str:
    """Return a note's content, or an explanatory message if missing."""
    return _notes.get(title, "Note not found")


if __name__ == "__main__":
    mcp.run()
