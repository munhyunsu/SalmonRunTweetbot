# Configuration

1. Create API key
```bash
python3 main_create_key.py
```

2. Setting `sqlite3` database path (db\_url in `config.py`)

# Simple run (development)

```bash
uvicorn main:app --reload --port 10009 --root-path '/splatoon'
```

- For url redirection [traefic](https://github.com/traefik/traefik/releases)

```bash
cd ./etc/traefik/
../../traefik_v2.8.4_linux_amd64/traefik --configFile ./traefik.toml
```

# Production mode (gunicorn)

## Downloads

1. Create root path venv and install requirements

(As a root)
```bash
/opt/Python310/bin/python3 -m venv /opt/splatoon_venv
/opt/splatoon_venv/bin/python3 -m pip install --upgrade -r [PATH2requirements.txt]
```

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker --chdir [PATH] main:app --bind 0.0.0.0:8888
```

