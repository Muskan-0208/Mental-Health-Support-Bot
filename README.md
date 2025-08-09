
# 🧠 Mental Health Support Bot

> *"Your mental health is just as important as your physical health."*  

The **Mental Health Support Bot** is an AI-powered companion built during my internship at **IIT Jammu**.  
It provides users with **empathetic responses** and **personalized self-care suggestions** based on their emotional state.  

---

## 🌐 Demo  
🔗 [**Live Demo on Gradio**](https://www.linkedin.com/posts/muskan-sharma2208_aiforgood-mentalhealthmatters-crewai-activity-7359974250339794944-I8Sw?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFoJALEBmuYl7p_GVlFFzgVh4v3dJL4x9ak)  

---

## 📌 About the Project  
This project aims to create a safe, supportive, and AI-driven mental wellness tool.  
By understanding a user's mood, it responds with warmth and care, followed by a simple self-care activity suggestion.  

Built using:  
- **CrewAI** – For multi-agent orchestration.  
- **Gemini LLM** – For natural language understanding and generation.  
- **Gradio** – For creating an easy-to-use web interface.  

---

## ⚙️ How It Works  
1. **User inputs** their current feelings in a text box.  
2. **Mood Analyzer Agent** classifies the emotional state (Sad, Anxious, Angry, Happy, Neutral).  
3. **Companion Agent** generates an empathetic response.  
4. **Self-Care Recommender Agent** suggests a mental wellness activity.  
5. Responses are **combined into one friendly and supportive message**.  

---

## 🚀 Getting Started  

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/mental-health-support-bot.git
cd mental-health-support-bot
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set up environment variables

Create a `.env` file in the project root and add your **Gemini API Key**:

```env
GEMINI_API_KEY=your_api_key_here
```

### 4️⃣ Run the bot

```bash
python crew.py
```

Your Gradio interface will open in the browser.

---

## 📂 Project Structure

```
.
├── crew.py          # Main script to run the bot
├── Agents.py        # All AI agent definitions
├── tasks.py         # Task definitions for CrewAI
├── requirements.txt # Python dependencies
└── .env             # API keys (not included in repo)
```

---

## 💡 Example Interaction

**User:** *"I’ve been feeling stressed and overwhelmed lately."*
**Bot:**
*"I hear you. It sounds like you’ve been carrying a lot, and it’s okay to feel this way.
You might find it helpful to take a short walk in nature today to clear your mind and refresh your energy."*

---

## 🙏 Acknowledgments

* **IIT Jammu** – Internship opportunity
* **Parmveer Nandal Sir** – Guidance and mentorship
* **CrewAI**, **Gemini LLM**, and **Gradio** teams for the amazing tools

---



