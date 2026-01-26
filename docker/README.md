# Docker Deployment Guide

## Local Development

```bash
# From repository root
docker build -f docker/Dockerfile -t maths-python-app .
docker run -p 8501:8501 maths-python-app
```

Access at: http://localhost:8501

## AWS EC2 Deployment

The maths-python app runs on **port 8505** on the shared EC2 instance to avoid conflicts with other apps.

### Port Mapping Explained

All Streamlit apps run on port 8501 **inside** their containers. Docker maps each to a unique **external** port:

```
EC2 Host Port    Container Port    App
─────────────    ──────────────    ─────────────────────
8501        ──►  8501              quant-finance
8502        ──►  8501              options
8503        ──►  8501              fixed-income
8504        ──►  8501              portfolio-management
8505        ──►  8501              maths-python
```

The `-p` flag syntax: `-p <host-port>:<container-port>`

```bash
docker run -p 8505:8501 maths-python-app
#             │     │
#             │     └── Port inside container (always 8501 for Streamlit)
#             └──────── Port on EC2 (must be unique per app)
```

### Adding New Apps

To deploy another Streamlit app, choose the next available port:

```bash
# Example: new app on port 8506
docker run -d -p 8506:8501 --name new-app --restart unless-stopped new-app-image
```

Remember to add the port to the EC2 security group.

### Deploy Commands

```bash
# SSH into EC2 (via Instance Connect)

# Clone and build
cd ~
git clone https://github.com/koysor/maths-python.git
cd maths-python
sudo docker build -f docker/Dockerfile -t maths-python-app .

# Run on port 8505
sudo docker run -d -p 8505:8501 --name maths-python --restart unless-stopped maths-python-app
```

### Update Deployment

```bash
cd ~/maths-python
git pull
sudo docker stop maths-python
sudo docker rm maths-python
sudo docker build -f docker/Dockerfile -t maths-python-app .
sudo docker run -d -p 8505:8501 --name maths-python --restart unless-stopped maths-python-app
```

## Live URL

http://13.50.72.89:8505

## All Apps on EC2

| App | Port | Repository |
|-----|------|------------|
| Quant Finance | 8501 | quant-finance |
| Options | 8502 | quant-finance |
| Fixed Income | 8503 | quant-finance |
| Portfolio Management | 8504 | quant-finance |
| Maths Python | 8505 | maths-python |
