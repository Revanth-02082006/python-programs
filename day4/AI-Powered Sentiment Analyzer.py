from textblob import TextBlob

text = input("Enter a sentence: ")
sentiment = TextBlob(text).sentiment.polarity

if sentiment > 0:
    print("Positive sentiment 😊")
elif sentiment < 0:
    print("Negative sentiment 😞")
else:
    print("Neutral sentiment 😐")
