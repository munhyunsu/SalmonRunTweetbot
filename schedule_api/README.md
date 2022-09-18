# Configuration

1. Create API key
```bash
python3 main_create_key.py
```

2. Setting `sqlite3` database path (db\_url in `config.py`)

# Run API server

## Simple run (development)

```bash
uvicorn main:app --reload --port 10009 --root-path '/splatoon'
```

- For url redirection [traefic](https://github.com/traefik/traefik/releases)

```bash
cd ./etc/traefik/
../../traefik_v2.8.4_linux_amd64/traefik --configFile ./traefik.toml
```

## Production mode (gunicorn)

```bash

```

## Downloads

1. Create root path venv and install requirements

(As a root)
```bash
/opt/Python310/bin/python3 -m venv /opt/splatoon_venv
/opt/splatoon_venv/bin/python3 -m pip install --upgrade -r [PATH2requirements.txt]
```

2. Copy and edit systemd, nginx conf file

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker --chdir [PATH] main:app --bind 0.0.0.0:8888
```

# Splatoon Service using `systemd`

```bash
sudo cp $HOME/.../run_splatoon /opt/splatoon/etc/systemd/run_splatoon
sudo cp $HOME/.../splatoon.service /opt/splatoon/etc/systemd/splatoon.service
sudo chmod +x /opt/splatoonl/etc/systemd/run_splatoon
```

```bash
sudo ln -s /opt/splatoon/etc/systemd/splatoon.service /etc/systemd/system/splatoon.service
sudo systemctl daemon-reload
sudo systemctl enable splatoon.service
sudo systemctl start splatoon.service
sudo systemctl status splatoon.service
```

