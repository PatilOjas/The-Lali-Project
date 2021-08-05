from textblob import TextBlob
sentence=input("Type your sentence")
edu=TextBlob(sentence)
x=edu.sentiment.polarity

if x<0:
    print('negative')
elif x==0:
    print('Neutral')
elif x>0 and x<=1:
    print('positive')