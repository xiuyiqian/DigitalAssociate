import os, sys, signal, json, requests
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

request_url = "http://localhost:8011/A2F/A2E/SetEmotion"
player = "/World/audio2face/PlayerStreaming"
fullface_core = "/World/audio2face/CoreRegular"

# Opening JSON file
f = open('./sentimentModel/a2f_emotion.json')
# returns JSON object as # a dictionary
emotionLib = json.load(f)
sentiment = SentimentIntensityAnalyzer()

def setEmo(text):
    
    sent_t = sentiment.polarity_scores(text)
    del sent_t["compound"]
    emotion = max(sent_t, key=sent_t.get)
    
    emotion = emotion.capitalize()
    
    if emotion == "Neg":
        emotion = "Sadness"
    elif emotion == "Pos":
        emotion = "Joy"
    else:
        emotion = "Neutral"
    
    """
    if emotion == "Surprise":
        emotion = "Amazement"
    if emotion == "Love":
        emotion = "Neutral"
    """
    print(emotion)
        
    emotionVec = emotionLib["Emotions"][0][emotion]
    print(emotionVec)
    
    headers = {
    'Content-Type': 'application/json',
    'accept': 'application/json'
    }
    
    dataPost =   {
    "a2f_instance": "/World/audio2face/CoreFullface",
    "emotion": emotionVec
    }
    req = requests.post(request_url, headers=headers, data=json.dumps(dataPost))

setEmo("The pizza tastes terrible.")