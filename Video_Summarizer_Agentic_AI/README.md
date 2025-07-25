# 📽️ Video Summarizer Agent

This application allows users to upload video files and ask questions about their content. It uses AI (Gemini model) to analyze videos and generate detailed insights.  

---

## ✨ Features
- Upload video files (MP4, MOV, AVI).
- Ask questions about the video content.
- AI summarizes and provides contextual answers.
- Powered by Google Gemini and Phi Agent.

---

## 🖥️ User Interface

### 📤 Upload Video
![Upload Screen](screenshots/upload_screen.png)

### 📝 Ask Questions
![Ask Questions](screenshots/question_screen.png)

---

## 📚 Libraries Used

### 🖥️ **Frontend and UI**
- **`streamlit`**  
  Creates the interactive web interface for uploading videos and displaying AI responses.

### 🤖 **AI Models and Tools**
- **`phi.agent.Agent`**  
  Defines the intelligent agent for video summarization.  
- **`phi.model.google.Gemini`**  
  Connects to Google Gemini models for analyzing video and generating insights.  
- **`phi.tools.duckduckgo.DuckDuckGo`**  
  Allows the agent to perform supplementary web searches.

### 🎥 **Google Generative AI**
- **`google.generativeai.upload_file` & `google.generativeai.get_file`**  
  Uploads video files and retrieves processed files for analysis.  
- **`google.generativeai`**  
  Configures API access to Gemini services.

### 🔐 **Environment Management**
- **`dotenv.load_dotenv`**  
  Loads API keys from a `.env` file securely.  
- **`os.getenv`**  
  Fetches environment variables like `GOOGLE_API_KEY`.

### 📂 **File Management**
- **`pathlib.Path`**  
  Manages temporary video file paths and cleanup.  
- **`tempfile.NamedTemporaryFile`**  
  Creates a temporary file for uploaded videos.

### 🕒 **Utilities**
- **`time.sleep`**  
  Waits during asynchronous video processing.  

