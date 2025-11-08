# 🌍 Real-Time Language Translator Bot 🎙

A simple and powerful Python app that listens to your voice 🎧, translates it instantly 🌐, and speaks it back 🔊 — breaking language barriers in real time!

---

## ✨ What It Does

- 🎤 *Listens* to your voice through the microphone  
- 🌎 *Translates* it instantly into another language  
- 🔊 *Speaks* the translated text out loud  
- 🖥 *Displays* everything clearly in a beautiful Streamlit app  

---

## 🧠 How It Works

🎙 Speak → 🧩 Recognize Speech → 🌍 Translate → 🔊 Speak Output

- Uses *SpeechRecognition* to convert your voice to text  
- Uses *Google Translate API* to translate text  
- Uses *gTTS (Google Text-to-Speech)* and *Pygame* to play the audio  

---

## ⚙ Requirements

Make sure you have *Python 3.8 or higher* installed.
Install these libraries (already listed in requirements.txt):
streamlit gtts pygame googletrans==4.0.0-rc1 SpeechRecognition pyaudio
💡 Tip: If PyAudio doesn’t install, use the prebuilt version from  
👉 [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

---

## 🚀 Quick Start

```bash
# 1️⃣ Clone the repo
git clone https://github.com/jeevzzz1024/Real-Time-language-translator-bot.git
cd Real-Time-language-translator-bot

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the app
streamlit run source/main.py

Then open the Streamlit link that appears in your terminal.


---

🎮 How to Use

1. Choose Source Language (the language you speak).
2. Choose Target Language (the language you want to translate to).
3. Click Start and begin speaking!
4. The app will:
Show what you said 💬
Translate it instantly 🌍
Speak it back in the target language 🔊
5. Click Stop to end translation.
---

🌐 Supported Languages

All Google Translate languages are supported — including:

Code	Language

en	English
ta	Tamil
hi	Hindi
ml	Malayalam
fr	French
es	Spanish
de	German
zh-cn	Chinese
ja	Japanese



---

🧩 Project Structure

Real-Time-language-translator-bot/
│
├── source/
│   └── main.py
│
├── requirements.txt
└── README.md


---

##🔮 Future Ideas ##
🎧 Add offline voice translation (using Whisper / Vosk)
💬 Add chat-based multilingual mode
🎛 Build mobile app version
🧠 Use AI voices for natural output



---

👨‍💻 Developed By
Jeeva & Team
💡 Powered by Python, Streamlit, and Google APIs
📅 2025
⭐ “Speak any language, understand every word.”
---
❤ Support

If you like this project: ⭐ Star it on GitHub 📢 Share it with friends
🧠 Keep building cool Python apps!

