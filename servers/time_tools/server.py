from datetime import datetime, timezone

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Time Tools Server")


@mcp.tool()
def current_utc_time() -> str:
    """Return the current UTC time in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


@mcp.tool()
def timestamp_to_iso(timestamp: float) -> str:
    """Convert Unix seconds to a UTC ISO 8601 timestamp."""
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()


if __name__ == "__main__":
    mcp.run()
