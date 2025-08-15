

To install and run a2a-inspector, refer to official [documentation](https://github.com/a2aproject/a2a-inspector).
On my laptop, I launched this commands:

```bash
 git clone https://github.com/a2aproject/a2a-inspector.git
 cd a2a-inspector
 curl -LsSf https://astral.sh/uv/install.sh | less
 curl -LsSf https://astral.sh/uv/install.sh | sh
 uv sync
 source $HOME/.local/bin/env
 uv sync
 cd frontend/
 npm install
 cd ..
 chmod +x run.sh
 ./run.sh
```

To run remote agent:
```bash
poetry run uvicorn remote_agent.agent:a2a_app --host localhost --port 8001
```
