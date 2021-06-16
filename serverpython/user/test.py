# import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
result = sia.polarity_scores("i hate you")
print(result["compound"])

if result["compound"] > 0:
    print("sentimen positif")
else :
    print("sentimen negatif")