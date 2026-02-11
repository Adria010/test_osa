## Setup

This project uses `uv` for dependency management and virtual environments.

1. Install uv (if you do not have it):
	- macOS/Linux: https://docs.astral.sh/uv/
	- Windows: https://docs.astral.sh/uv/

2. Create the virtual environment and install dependencies:

```bash
uv venv
uv sync
```

3. Activate the environment (optional if you use `uv run`):

```bash
source .venv/bin/activate
```

## Run

```bash
uv run python main.py
```
