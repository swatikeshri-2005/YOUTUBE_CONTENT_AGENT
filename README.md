# 🎬 YouTube Content Creation Agent

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge\&logo=streamlit)
![AI](https://img.shields.io/badge/AI-Powered-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 🚀 Overview

**YouTube Content Creation Agent** is an AI-powered application that helps creators quickly research topics and generate engaging **YouTube Shorts scripts**.

The system combines:

* 🔎 Real-time web research
* 🧠 Large Language Models (LLMs)
* 🎨 Streamlit interactive UI

Users simply enter a **YouTube topic**, and the AI generates a **short-form video script ready for recording**.

---

## ✨ Features

✔ AI-generated **YouTube Shorts scripts**
✔ Real-time **topic research**
✔ Clean **Streamlit dashboard**
✔ Fast script generation
✔ Beginner-friendly architecture

---

## 🧠 How It Works

```
User Topic
   │
   ▼
Research Agent
   │
   ▼
LLM Script Generator
   │
   ▼
Formatted YouTube Script
```

1️⃣ User enters a topic
2️⃣ Research agent gathers information
3️⃣ AI processes and summarizes content
4️⃣ Script generator produces a short video script

---

## 🏗 Project Architecture

```
youtube_content_agent
│
├── app
│   ├── main.py
│   ├── research_agent.py
│   ├── script_writer.py
│   └── utils.py
│
├── config
│   ├── __init__.py
│   └── config.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/swatikeshri-2005/YOUTUBE_CONTENT_AGENT.git
cd YOUTUBE_CONTENT_AGENT
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Create environment variables

Create `.env` file:

```
GEMINI_API_KEY=your_api_key_here
SERPER_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the application

```
streamlit run app/main.py
```

The app will open at:

```
http://localhost:8501
```

---

## 🎥 Example Output

**Input Topic**

```
Future of Artificial Intelligence
```

**Generated Script**

```
🎬 Hook
Did you know AI might transform almost every job in the next decade?

📌 Main Points
Artificial Intelligence is already powering healthcare,
self-driving cars, and personalized education.

🚀 Call To Action
Follow for more quick AI insights!
```

---

## 🛠 Tech Stack

* **Python**
* **Streamlit**
* **LLM API (Gemini / other)**
* **Web Search API**
* **Environment Variables**

---

## 📈 Future Improvements

* Viral title generator
* YouTube SEO tag generator
* Thumbnail text generator
* Trending topic detection
* Multi-agent architecture

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repo
2. Create a feature branch
3. Submit a pull request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you like this project, consider **starring the repository**!

---

<p align="center">

Made with ❤️ by **Swati Keshri**

</p>
