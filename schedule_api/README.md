# Simple run (development)

```bash
uvicorn main:app --reload --port 8888
```

# Production mode (gunicorn)

1. Create root path venv and install requirements

(As a root)
```bash
/opt/Python310/bin/python3 -m venv /opt/splatoon_venv
/opt/splatoon_venv/bin/python3 -m pip install --upgrade -r [PATH2requirements.txt]
```



```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker --chdir [PATH] main:app --bind 0.0.0.0:8888
```

