import re

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Text Tools Server")


@mcp.tool()
def word_count(text: str) -> int:
    """Count whitespace-separated words in text."""
    return len(text.split())


@mcp.tool()
def reverse_text(text: str) -> str:
    """Return text in reverse character order."""
    return text[::-1]


@mcp.tool()
def slugify(text: str) -> str:
    """Convert text into a lowercase URL-friendly slug."""
    normalized = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    return normalized.strip("-")


if __name__ == "__main__":
    mcp.run()
