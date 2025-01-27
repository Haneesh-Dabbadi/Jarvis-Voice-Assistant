# 🧠 Jarvis - Personal AI Assistant

Jarvis is a Python-based, voice-controlled virtual assistant 🧐 that can automate various tasks on your computer. It leverages speech recognition, natural language processing, and APIs to execute commands such as opening apps, controlling media, sending messages, generating essays, and more.

---

## ✨ Features

- 🎤 **Voice Commands:** Use natural speech to control Jarvis.
- 🚀 **App Automation:** Open applications like WhatsApp, Spotify, Google Chrome, etc.
- 🎵 **Media Control:** Increase/decrease volume, play music via YouTube or Spotify.
- 📞 **Communication:** Send messages or make calls on WhatsApp.
- 🔄 **Content Generation:** Generate essays using AI-based APIs.
- 🌐 **Multilingual Support:** Supports commands in multiple languages with translation.
- 🔍 **Screen OCR:** Capture and read WhatsApp messages using OCR (Optical Character Recognition).
- 📰 **News Fetching:** Retrieve the latest news using the NewsAPI.

---

## 📊 Prerequisites

Before using Jarvis, you need to install the following libraries:

- `speech_recognition`
- `pyttsx3`
- `requests`
- `pywhatkit`
- `pyautogui`
- `pytesseract`
- `pillow`
- `win32com.client` (for MS Word integration)
- `platform` (for OS-related functionality)

Install dependencies using `pip`:

```bash
pip install speech_recognition pyttsx3 requests pywhatkit pyautogui pytesseract pillow pywin32
```

Additionally, you need to install **Tesseract-OCR**:

1. 🔗 Download Tesseract-OCR from [here](https://github.com/tesseract-ocr/tesseract).
2. 🔧 During installation, note the installation directory (default: `C:\Program Files\Tesseract-OCR`).
3. 🗒 Add the path in the script:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## 🔧 Setup

### Step 1: 🔧 Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/jarvis-assistant.git
cd jarvis-assistant
```

### Step 2: ⚙️ Add API Keys

Jarvis uses APIs for various tasks like news fetching and essay generation. Add your keys in the script:

- **NewsAPI:** Get your API key from [NewsAPI](https://newsapi.org/).
- **AI21 API:** Get your API key from [AI21 Studio](https://www.ai21.com/).

Update the placeholders in the script:

```python
NEWS_API_KEY = 'your_news_api_key'
AI21_API_KEY = 'your_ai21_api_key'
```

### Step 3: 📞 Define Contacts

Add your contacts in the `contacts` dictionary in the script. Example:

```python
contacts = {
    "John": "+1234567890",
    "Doe": "+0987654321"
}
```

### Step 4: 🔍 Specify WhatsApp Path

Ensure your WhatsApp application path is correctly set in the script. Example:

```python
whatsapp_path = r"C:\Users\YourUserName\AppData\Local\WhatsApp\WhatsApp.exe"
```

---

## 💻 Usage

Run the script:

```bash
python jarvis_assistant.py
```

Once running, say **"Jarvis"** to activate it and give your commands. Example commands:

- "open WhatsApp"
- "send message to John Hi there!"
- "play the song Shape of You"
- "news"
- "generate an essay on climate change"

Jarvis will process and execute your commands.

---

## 🤖 How It Works

1. **Activation:** Jarvis listens for the keyword "Jarvis" to activate itself.
2. **Speech Recognition:** Converts spoken commands to text using the `speech_recognition` library.
3. **Command Mapping:** The text command is mapped to a specific functionality (e.g., sending a WhatsApp message or opening an app).
4. **Execution:** The mapped function is executed via Python libraries and APIs.

---

## 🔍 Example Workflow

### Sending a WhatsApp Message:

1. User says: "send message to John Hey, how are you?"
2. Jarvis extracts the name "John" and the message "Hey, how are you?".
3. It uses the `contacts` dictionary to fetch John's number.
4. The `pywhatkit` library is used to send the WhatsApp message.

---

## ✨ Example Commands

### Open Apps:

- "open WhatsApp"
- "open Spotify"

### Control Media:

- "play the song Believer"
- "increase volume"

### Send Messages:

- "send message to John Good morning!"

### Fetch News:

- "news"

### AI-Generated Content:

- "generate an essay on artificial intelligence"

### OCR WhatsApp Messages:

- "read my WhatsApp messages"

---

## 🙏 Contributions

Contributions are always welcome! If you'd like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/<your-feature-name>
```

3. Commit your changes:

```bash
git commit -m "Added <feature-name>"
```

4. Push to the branch:

```bash
git push origin feature/<your-feature-name>
```

5. Open a pull request.

---

## ❤️ License

This project is licensed under the MIT License. See the LICENSE file for details.
