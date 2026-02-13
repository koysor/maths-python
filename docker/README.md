# Docker Deployment Guide

## Architecture

The maths-python app is deployed on a shared EC2 instance alongside the quant-finance apps. Caddy (managed by the quant-finance repository) provides automatic HTTPS via Let's Encrypt and routes `/maths/*` traffic to this container.

```
Internet (HTTPS :443)
    │
    ▼
Caddy Reverse Proxy (managed by quant-finance)
    │
    ├─► quant-finance:8501  (/)
    ├─► options:8501        (/options/)
    ├─► fixed-income:8501   (/fixed-income/)
    ├─► portfolio:8501      (/portfolio/)
    │
    └─► host:8505           (/maths/)
            │
            ▼
        maths-python container (internal port 8501)
```

## Local Development

### Using Docker Compose (recommended)

```bash
cd docker
docker-compose up --build
```

Access at: http://localhost:8505/maths/

### Using Docker directly

```bash
docker build -f docker/Dockerfile -t maths-python .
docker run -p 8505:8501 maths-python
```

Access at: http://localhost:8505/maths/

## Production Deployment (EC2)

### How it works

1. GitHub Actions builds the Docker image and pushes to GHCR
2. The deploy job SSHs into EC2, pulls the image, and starts the container via docker-compose
3. The container publishes port 8505 on the host
4. Caddy (from quant-finance) routes `https://koysor.duckdns.org/maths/*` to `host.docker.internal:8505`

### Docker Compose files

| File | Purpose |
|------|---------|
| `docker-compose.yml` | Local development (builds from local Dockerfile) |
| `docker-compose.prod.yml` | Production (uses pre-built GHCR image) |

### Manual deployment

```bash
# SSH into EC2
cd ~/maths-python/docker

# Pull latest image and start
docker-compose -f docker-compose.prod.yml pull
docker-compose -f docker-compose.prod.yml up -d
```

### Updating

```bash
cd ~/maths-python
git pull
cd docker
docker-compose -f docker-compose.prod.yml pull
docker-compose -f docker-compose.prod.yml up -d
```

## Port Allocation on Shared EC2

```
Host Port    Container Port    App                  Repository
─────────    ──────────────    ─────────────────    ──────────────
8501         8501              quant-finance        quant-finance
8502         8501              options              quant-finance
8503         8501              fixed-income         quant-finance
8504         8501              portfolio-management quant-finance
8505         8501              maths-python         maths-python
```

## HTTPS

HTTPS is provided by Caddy in the quant-finance deployment. The Caddyfile entry:

```
handle /maths/* {
    reverse_proxy host.docker.internal:8505
}
```

This means:
- The maths-python container publishes port 8505 on the EC2 host
- Caddy terminates TLS and proxies HTTPS traffic to the container
- The `--server.baseUrlPath=maths` Streamlit option ensures the app works correctly at `/maths/`
- Automatic Let's Encrypt certificate renewal is handled by Caddy

## Live URL

https://koysor.duckdns.org/maths/
