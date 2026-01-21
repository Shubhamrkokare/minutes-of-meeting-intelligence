import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required resources (safe if already present)
nltk.download("vader_lexicon")

# Initialize analyzer
sia = SentimentIntensityAnalyzer()


def analyze_sentiment(text: str) -> str:
    """
    Perform basic sentiment analysis:
    Positive / Negative / Neutral
    """

    scores = sia.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    result = (
        f"Overall Sentiment: {sentiment}\n\n"
        f"Detailed Scores:\n"
        f"Positive: {scores['pos']}\n"
        f"Neutral: {scores['neu']}\n"
        f"Negative: {scores['neg']}\n"
        f"Compound Score: {scores['compound']}"
    )

    return result

