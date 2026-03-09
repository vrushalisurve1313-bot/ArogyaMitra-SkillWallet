# 🏥 ArogyaMitra

ArogyaMitra is an AI-powered healthcare assistance platform designed to provide basic health guidance based on user symptoms. The system uses **React (frontend)** and **FastAPI (backend)** to analyze symptoms entered by the user and generate AI-based health suggestions.

## 🚀 Feature

### Symptom Analysis

Users can enter symptoms such as *fever, cough, headache*, and the system provides possible health insights and suggestions.

## 🛠 Tech Stack

* **Frontend:** React.js
* **Backend:** FastAPI (Python)
* **Database:** SQLite
* **AI Model:** Groq LLaMA 3.3

## 📂 Project Structure

```
ArogyaMitra
│
├── arogya-frontend   # React frontend
├── backend           # FastAPI backend
└── README.md
```

## ⚙️ How to Run

### Backend

```
cd backend
python -m uvicorn main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

### Frontend

```
cd arogya-frontend
npm install
npm start
```

Frontend runs on:

```
http://localhost:3000
```

## 👥 Team

* Devraj Jadhav
* Nivas Maragale
* Prathamesh Wategaonkar
* Vrushali Surve (Team Lead)

## ⚠️ Note

This project is developed for **educational purposes** and should not replace professional medical advice.
