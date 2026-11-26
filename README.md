# Claude-Style Sentiment Analysis Web App

A clean, minimalist web application for real-time text sentiment analysis featuring a **Claude-inspired dark chat interface**. Built with Python, Flask, and TextBlob/NLTK.

---

## 📸 Overview

The interface mimics Claude's conversational experience:
- **Claude aesthetic**: Sleek dark theme, subtle terracotta accents, and smooth typography.
- **Conversational workflow**: Type or paste any sentence, tweet, or review to receive instant inline sentiment feedback.
- **Real-time feedback**: Animated typing indicator with color-coded classification (Positive, Negative, or Neutral) and descriptive sentiment insights.
- **Interactive quick suggestions**: One-click prompt chips on the welcome screen.
- **Keyboard shortcuts**: Press `Enter` to analyze and `Shift + Enter` for multi-line input.

---

## 🛠️ Tech Stack

- **Backend**: Python 3, [Flask](https://flask.palletsprojects.com/)
- **NLP Engine**: [TextBlob](https://textblob.readthedocs.io/), [NLTK](https://www.nltk.org/)
- **Frontend**: HTML5, Vanilla JavaScript, CSS3 (CSS Variables, Flexbox, responsive design)

---

## 📂 Project Structure

```text
Sentiment_Analysis/
├── app.py                  # Flask backend with text sentiment analysis routes
├── requirements.txt        # Python package dependencies
├── templates/
│   └── index.html          # Claude-inspired chat UI
├── static/                 # Static assets (styles, icons, images)
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8 or higher installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/yourusername/Sentiment_Analysis.git
cd Sentiment_Analysis
```

### 3. Create & Activate a Virtual Environment

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies & Corpora
```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

### 5. Run the Application
```bash
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## 💡 How It Works

1. **Input Preprocessing**: User text is cleaned of URLs, user handles, and special symbols.
2. **Polarity Calculation**: TextBlob calculates the sentiment polarity score between `-1.0` (extremely negative) and `+1.0` (extremely positive).
3. **Sentiment Mapping**:
   - **Positive** (`polarity > 0`): Highlights praise, satisfaction, and optimism.
   - **Neutral** (`polarity == 0`): Objective statements or balanced tones.
   - **Negative** (`polarity < 0`): Criticism, frustration, or sadness.
4. **Instant Response**: Results are returned asynchronously via JSON and displayed inline without page reloads.

---

## 🔌 API Reference

### Text Sentiment Analysis
- **Endpoint**: `/predict1`
- **Method**: `POST`
- **Payload**: `form-data` with key `txt` containing the text string.
- **Response**:
  ```json
  {
    "result": "positive",
    "text": "I absolutely love this new update!"
  }
  ```

---

## 🤝 Contributing

Contributions and feedback are always welcome!
1. Fork this repository.
2. Create a feature branch (`git checkout -b feature/cool-feature`).
3. Commit your changes (`git commit -m "Add cool feature"`).
4. Push to the branch (`git push origin feature/cool-feature`).
5. Open a Pull Request.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
