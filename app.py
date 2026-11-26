import re
from textblob import TextBlob
from flask import Flask, render_template, request, jsonify
import nltk

nltk.download('stopwords', quiet=True)

app = Flask(__name__)
app.static_folder = 'static'


def clean_text(text):
    return ' '.join(
        re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split()
    )


def analyze_sentiment(text):
    blob = TextBlob(clean_text(text))
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity == 0:
        return "neutral"
    else:
        return "negative"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict1', methods=['POST'])
def predict_text():
    text = request.form.get('txt', '').strip()
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    sentiment = analyze_sentiment(text)
    return jsonify({'result': sentiment, 'text': text})


if __name__ == '__main__':
    app.run(debug=True)
