from textblob import TextBlob

text = [
 "i love NLP ! It works great and I'm very satisfied ",
 "This is my first experience on doing sentiment analysis, I am little bit dissapointed",
 "The NLP sentiment analysis is quite intresting it is neither good or bad",

]

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity>0:
        sentiment= "positive"
    elif polarity<0:
        sentiment="negative"
    else:
        sentiment="neutral"
        return sentiment
for text in text:
    sentiment = analyze_sentiment(text)
    print(f"text:{text}")
    print(f"Sentiment:{sentiment}\n")


