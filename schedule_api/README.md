# Simple run (development)

```bash
uvicorn main:app --reload --port 8888
```

## Production mode (gunicorn)

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker --chdir [PATH] main:app --bind 0.0.0.0:8888
```

