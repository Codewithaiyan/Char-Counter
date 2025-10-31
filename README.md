🧮 Character Counter Application

A full-stack web application that counts the number of characters in a user’s input text.
The app is built using Flask (Python) for the backend and HTML/CSS/JavaScript for the frontend.
It is fully containerized with Docker and deployable to Kubernetes for scalability and production readiness.

📘 Table of Contents

Overview

Architecture

Project Structure

Tech Stack

Backend API Details

Frontend Overview

Docker Setup

Kubernetes Deployment

Testing the Application

Future Enhancements

Author

📖 Overview

This project demonstrates a simple but production-style microservice setup:

The backend handles requests and performs logic (counting characters, validation, response formatting).

The frontend is a clean, interactive UI where the user enters their text.

Both are Dockerized and deployed as independent services on Kubernetes — communicating via internal service names.

This design mimics real-world DevOps workflows, focusing on containerization, deployment automation, and scalability.

🏗️ Architecture

┌─────────────────────────┐
│       Frontend          │
│  (HTML + CSS + JS)      │
│  Sends POST → /api      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       Backend (Flask)   │
│  /count endpoint         │
│  Returns JSON response   │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Docker Networking      │
│  Kubernetes Cluster      │
│  Frontend & Backend Pods │
│  NodePort Service        │
└─────────────────────────┘


📂 Project Structure
char-counter/
│
├── backend/
│   ├── app.py                 # Flask backend logic
│   ├── Dockerfile.backend     # Docker config for backend
│
├── frontend/
│   ├── index.html             # Main frontend interface
│   ├── Dockerfile.frontend    # Docker config for frontend
│
├── k8s/
│   ├── backend-deployment.yaml   # Backend Deployment & Service
│   ├── frontend-deployment.yaml  # Frontend Deployment & Service
│
├── .gitignore
└── README.md

⚙️ Tech Stack
Component	Technology Used
Frontend	HTML, CSS, JavaScript
Backend	Python (Flask)
Containerization	Docker
Orchestration	Kubernetes
Testing	curl / browser
Version Control	Git & GitHub
