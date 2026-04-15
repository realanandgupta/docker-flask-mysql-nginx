# 🚀 Dockerized Flask App with MySQL and Nginx (Docker Compose)

## 📌 Project Overview

This project demonstrates a fully containerized multi-tier application using:

* Flask (Backend API)
* MySQL (Database)
* Nginx (Reverse Proxy)
* Docker & Docker Compose

The application is deployed on AWS EC2 and follows a production-like architecture.

---

## 🏗️ Architecture

User → Nginx → Flask → MySQL

* Nginx acts as a reverse proxy and handles incoming requests
* Flask processes API requests
* MySQL stores application data
* Docker Compose manages all services

---

## ⚙️ Tech Stack

* Python (Flask)
* MySQL
* Nginx
* Docker
* Docker Compose
* AWS EC2

---

## 📁 Project Structure

```
project-compose/
│── app.py
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── nginx.conf
│── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd project-compose
```

### 2. Start the application

```bash
docker compose up --build -d
```

### 3. Access the application

```
http://<EC2-IP>
```

---

## 🔥 Features

* Multi-container setup using Docker Compose
* Reverse proxy using Nginx
* Flask API integrated with MySQL
* Persistent database using Docker volumes
* Internal container communication via Docker network

---

## 📌 API Endpoints

### Home

```
GET /
```

### Database Check

```
GET /db
```

---

## 🧠 Key Learnings

* Containerization of applications
* Multi-container orchestration
* Reverse proxy setup with Nginx
* Service-to-service communication using Docker networking
* Debugging container and networking issues

---

## 💡 Future Improvements

* Add CI/CD pipeline
* Use environment variables (.env)
* Use production server (Gunicorn)
* Add frontend (React)

---

## 👨‍💻 Author

Anand Kumar

