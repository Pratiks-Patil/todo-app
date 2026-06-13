# 📝 ToDo DevOps App

A simple **Flask-based ToDo application** built to demonstrate a complete **DevOps workflow** using Docker, Jenkins, and Kubernetes.

This project serves as a hands-on example for learning Continuous Integration (CI), Continuous Deployment (CD), containerization, and orchestration.

---

## 🚀 Features

- ✅ Add new tasks
- ✅ View all tasks
- ✅ Simple and clean user interface
- ✅ Lightweight Flask backend
- ✅ Dockerized application
- ✅ Jenkins pipeline support
- ✅ Kubernetes deployment ready

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Programming |
| Flask | Web Framework |
| HTML/CSS | Frontend |
| Docker | Containerization |
| Jenkins | CI/CD Pipeline |
| Kubernetes | Container Orchestration |

---

## 📂 Project Structure

```
todo-app/
│
├── templates/              # HTML templates
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── Jenkinsfile             # Jenkins pipeline
├── k8s-deployment.yaml     # Kubernetes Deployment
├── k8s-service.yaml        # Kubernetes Service
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/todo-app.git
cd todo-app
```

### 2️⃣ Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://localhost:5000
```

---

# 🐳 Running with Docker

## Build the image

```bash
docker build -t todo-app .
```

## Run the container

```bash
docker run -p 5000:5000 todo-app
```

The application will be available at:

```
http://localhost:5000
```

---

# 🔄 Jenkins CI/CD

The repository includes a `Jenkinsfile` that can be used to automate:

- Source code checkout
- Dependency installation
- Application build
- Docker image creation
- Automated deployment steps

---

# ☸️ Kubernetes Deployment

Deploy the application using:

```bash
kubectl apply -f k8s-deployment.yaml
kubectl apply -f k8s-service.yaml
```

Verify resources:

```bash
kubectl get deployments
kubectl get services
kubectl get pods
```

---

## 🎯 Learning Objectives

This project demonstrates:

- Flask web application development
- Docker containerization
- Jenkins CI/CD pipelines
- Kubernetes deployments
- DevOps best practices

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## 👨‍💻 Author

**Pratik Patil**


---

⭐ If you found this project helpful, consider giving it a **star** on GitHub!
