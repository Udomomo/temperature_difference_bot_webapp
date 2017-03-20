# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime
import tweepy
from decimal import *
from fetch_temperature import extract_temperature

#check if temperature data exists
data = extract_temperature()

if data == "No Daily data":
    sys.exit() 

print(data)

#set temperature difference baseline
difference_line = 3

#set tweet sentence
today_temperatureMax = Decimal(data[0]["temperatureMax"])
tomorrow_temperatureMax = Decimal(data[1]["temperatureMax"])
today_temperatureMin = Decimal(data[0]["temperatureMin"])        
tomorrow_temperatureMin = Decimal(data[1]["temperatureMin"])
temperatureMax_difference = tomorrow_temperatureMax - today_temperatureMax
temperatureMin_difference = tomorrow_temperatureMin - today_temperatureMin

def plus_mark(number):
    if number > 0:
        return "+"
    else:
        return ""

tweet = "・明日の最高気温：" + str(tomorrow_temperatureMax) + "℃\n" \
      + "　（前日比" + plus_mark(temperatureMax_difference) \
      + str(temperatureMax_difference) + "℃）\n" \
      + "・明日の最低気温：" + str(tomorrow_temperatureMin) + "℃\n" \
      + "　（前日比" + plus_mark(temperatureMin_difference) \
      + str(temperatureMin_difference) + "℃）\n" \
      + "寒暖差が大きいです。体調に気をつけましょう。"

print(tweet)

#set API key
consumer_key = os.environ["CONSUMER_KEY_TEMPBOT"]
consumer_secret = os.environ["CONSUMER_SECRET_TEMPBOT"]
access_token = os.environ["ACCESS_TOKEN_KEY_TEMPBOT"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_TEMPBOT"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler=auth)

#judge to tweet or not
def judge_difference():
    if abs(temperatureMax_difference) >= difference_line \
    or abs(temperatureMin_difference) >= difference_line:
        return True
    else:
        return False

print(judge_difference())

#execute tweet
def make_tweet():
    if judge_difference() == True:
        print(tweet)      
        api.update_status(tweet)        
    else:
        sys.exit()

make_tweet()

