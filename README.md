# Python MCP Servers

A collection of four small, runnable [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers built with Python and the official MCP Python SDK.

## Included servers

| Server | Tools | Purpose |
|---|---|---|
| Calculator | `add`, `subtract`, `multiply`, `divide` | Safe basic arithmetic |
| Text Tools | `word_count`, `reverse_text`, `slugify` | Small text transformations |
| Time Tools | `current_utc_time`, `timestamp_to_iso` | UTC time and timestamp conversion |
| Notes | `save_note`, `list_notes`, `get_note` | In-memory notes for one server session |

Each server can be run independently over MCP's stdio transport.

## Requirements

- Python 3.10+
- MCP Python SDK

## Setup

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run a server

```bash
python servers/calculator/server.py
python servers/text_tools/server.py
python servers/time_tools/server.py
python servers/notes/server.py
```

These processes speak MCP over standard input/output, so use an MCP-compatible client to connect to them. Do not type commands directly into the terminal after starting a server; the client sends the protocol messages.

## Run tests

```bash
pytest -q
```

## Project layout

```text
servers/
├── calculator/server.py
├── text_tools/server.py
├── time_tools/server.py
└── notes/server.py
tests/test_servers.py
```

## Security notes

- The examples do not access the network or the local filesystem.
- The Notes server stores data only in memory and loses it when the process exits.
- Review tools before connecting them to an AI client, and never commit credentials or secrets.

## Author

**Aniruddha Salve**  
[GitHub](https://github.com/aniruddhasalve)
