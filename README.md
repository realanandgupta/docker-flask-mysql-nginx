# 🚀 Dockerized Flask App with MySQL and Nginx (CI/CD Enabled)

## 📌 Project Overview

This project demonstrates a fully containerized **multi-tier web application** using:

* 🐍 Flask (Backend API)
* 🛢️ MySQL (Database)
* 🌐 Nginx (Reverse Proxy)
* 🐳 Docker & Docker Compose
* ⚙️ GitHub Actions (CI/CD Pipeline)
* ☁️ AWS EC2 (Deployment)

The application is automatically deployed to an EC2 instance using a CI/CD pipeline.

---

## 🏗️ Architecture

```
User → Nginx → Flask App → MySQL
```

* Nginx handles incoming traffic
* Flask processes requests
* MySQL stores data

---

## ⚙️ Tech Stack

* Python (Flask)
* MySQL
* Nginx
* Docker & Docker Compose
* GitHub Actions
* AWS EC2

---

## 🚀 Features

* Full containerization using Docker
* Multi-service orchestration using Docker Compose
* Reverse proxy setup using Nginx
* Persistent database using Docker volumes
* Automated deployment using CI/CD
* Debugged real-world issues (port conflicts, service dependencies)

---

## 📂 Project Structure

```
.
├── app.py
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── requirements.txt
└── .github/workflows/deploy.yml
```

---

## 🔧 Setup Instructions (Local)

```bash
git clone https://github.com/your-username/docker-flask-mysql-nginx.git
cd docker-flask-mysql-nginx

docker compose up --build
```

Access app:

```
http://localhost
```

---

## ☁️ Deployment (AWS EC2)

* EC2 instance (Ubuntu)
* Docker & Docker Compose installed
* Port 80 open in security group

Run:

```bash
docker compose up -d
```

---

## 🔄 CI/CD Pipeline

GitHub Actions is used to:

* SSH into EC2
* Pull latest code
* Stop old containers
* Rebuild and deploy new containers

### Workflow Steps:

1. Code pushed to GitHub
2. GitHub Actions triggered
3. SSH into EC2
4. Run:

   ```bash
   docker compose down
   docker compose up --build -d
   ```

---

## ⚠️ Challenges Faced

* ❌ Port 80 already in use (system nginx conflict)
* ❌ Container networking issues
* ❌ MySQL authentication errors
* ❌ CI/CD SSH authentication issues

### ✅ Solutions

* Disabled system nginx service
* Proper container dependency setup
* Added required Python packages
* Configured GitHub secrets correctly

---

## 📸 Output

```
{"message": "CI/CD working 🔥"}
```

---

## 👨‍💻 Author

**Anand Kumar**

* GitHub: https://github.com/realanandgupta

---

## ⭐ Future Improvements

* HTTPS with SSL (Certbot)
* Kubernetes deployment
* Load balancing
* Monitoring (Prometheus + Grafana)
* Blue-Green Deployment

---

## 📢 Conclusion

This project demonstrates real-world DevOps practices including:

* Containerization
* Reverse proxy setup
* CI/CD automation
* Cloud deployment

It also highlights debugging skills and problem-solving in production-like environments.

---

