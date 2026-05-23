# 🏋️‍♂️ AI-Powered Real-Time Fitness Coach

An AI-powered real-time gym coaching platform that uses **Computer Vision**, **Pose Estimation**, **LLM-based AI feedback**, and **Voice Coaching** to analyze exercises, count repetitions, detect posture mistakes, and provide intelligent workout guidance in real time.

---

# 🚀 Features

- ✅ Real-time pose estimation using MediaPipe
- ✅ Live exercise tracking and rep counting
- ✅ AI-powered workout coaching using Groq Llama 3
- ✅ Real-time voice feedback with gTTS
- ✅ Posture correction and form validation
- ✅ Multi-exercise support
- ✅ Live webcam streaming using WebRTC
- ✅ Workout history tracking
- ✅ Modular and scalable architecture
- ✅ Real-time skeletal overlays and metrics

---

# 🧠 Supported Exercises

- Push-ups
- Squats
- Lunges
- Shoulder Press
- Biceps Curls

---

# 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Python | Core Programming |
| Streamlit | Frontend Web App |
| streamlit-webrtc | Real-time Webcam Streaming |
| MediaPipe | Pose Estimation |
| OpenCV | Image Processing |
| Groq API (Llama 3) | AI Coaching |
| gTTS | Voice Feedback |
| SQLite | Workout History Storage |
| Pandas | Data Handling |

---

# 📂 Project Structure

```bash
REAL-TIME-AI-GYM-COACH/
│
├── core/
│   └── base_exercise.py
│
├── detectors/
│   ├── pushup.py
│   ├── squat.py
│   ├── lunges.py
│   ├── shoulder_press.py
│   └── biceps_curl.py
│
├── ml_models/
│   └── pose_landmarker_full.task
│
├── services/
│   ├── auth/
│   ├── coaching/
│   │   ├── llm.py
│   │   ├── tts.py
│   │   └── voice_pipeline.py
│   │
│   ├── config/
│   ├── persistence/
│   ├── state/
│   ├── tracking/
│   ├── ui/
│   └── vision/
│       └── exercise_video_processor.py
│
├── static/
│   ├── style.css
│   └── AdobeClean.otf
│
├── data.db
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚡ How It Works

## 1️⃣ Pose Detection
The webcam feed is processed using **MediaPipe Pose Landmarker** to extract body landmarks in real time.

## 2️⃣ Exercise Analysis
Custom exercise detectors calculate:
- Joint angles
- Body alignment
- Movement stages
- Posture quality
- Rep counts

## 3️⃣ AI Coaching
Detected posture issues are sent to the **Groq Llama 3 LLM**, which generates intelligent workout feedback.

## 4️⃣ Voice Feedback
The AI response is converted into audio using **gTTS** and played back to the user in real time.

---

# 📸 Real-Time Metrics

The system tracks:
- Total repetitions
- Sets completed
- Knee angle
- Elbow angle
- Body alignment
- Hip position
- Balance status
- Back posture

---

# 🧮 Core Computer Vision Concepts Used

- Pose Estimation
- Human Landmark Detection
- Joint-Angle Calculation
- Biomechanical Analysis
- Motion Tracking
- Landmark Visibility Filtering
- Real-time Video Processing

---

# 🔥 AI Features

- Context-aware AI coaching
- Real-time form correction
- Dynamic motivational feedback
- Intelligent workout guidance
- Voice-based AI assistant

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-GYM-COACH.git
cd AI-GYM-COACH
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

## 3️⃣ Activate Environment

### Windows
```bash
.venv\Scripts\activate
```

### Mac/Linux
```bash
source .venv/bin/activate
```

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

# ▶️ Run Project

```bash
streamlit run main.py
```

---

# 📋 Requirements

```txt
streamlit==1.54.0
streamlit-webrtc==0.64.5
mediapipe==0.10.14
opencv-python-headless==4.10.0.84
pandas==2.2.3
groq>=0.12.0
gtts==2.5.3
python-dotenv==1.2.2
```

---

# 🎯 Future Improvements

- AI workout recommendations
- Personalized training plans
- Calorie estimation
- Multi-person tracking
- Exercise leaderboard
- Mobile app deployment
- Cloud-based analytics

---

# 📚 Learning Outcomes

This project helped in understanding:
- Computer Vision
- Human Pose Estimation
- Real-time AI systems
- LLM integration
- Voice AI pipelines
- Streamlit deployment
- Modular software architecture

---

# 👨‍💻 Author

Shweta Bairagi

---

# ⭐ If you like this project, consider giving it a star!
