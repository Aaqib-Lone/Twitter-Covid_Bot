from requests import api
import tweepy
from tweepy import OAuthHandler
import datetime
import time
import apikey2
import requests

while True:
    try:
        headers={
        'x-rapidapi-host': 'covid-19-data.p.rapidapi.com',
        'x-rapidapi-key': apikey2.key,
        # 'Accept':'application/json'
        }
        params= {'code': 'in', format: 'json'}
        url='https://covid-19-data.p.rapidapi.com/country/code'
        json=requests.get(url, params=params, headers=headers).json()

        coins=json[0]
        obj1="Country:  "+coins['country']
        obj2="Confirmed cases:  "+str("{:}".format(coins["confirmed"]))
        obj3="Recovered:  "+str("{:}".format(coins["recovered"]))
        obj4="Critical:  "+str("{:}".format(coins["critical"]))
        obj5="Deaths:  "+str("{:}".format(coins["deaths"]))

        full_m="Covid-19 Cases in "+obj1+"\n"+obj2+"\n"+obj3+"\n"+obj4+"\n"+obj5+"\n"+"Wear masks, maintain social distancing and follow Covid protocol"+"\n"

        print(full_m)

        api_key=apikey2.API_KEY
        api_key_secret=apikey2.API_KEY_SECRET
        access_token=apikey2.ACCESS_TOKEN
        access_token_secret=apikey2.ACCESS_TOKEN_SECRET

        auth= tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)

        api=tweepy.API(auth)

        api.update_status(full_m  +"\n"+ str(datetime.datetime.now()))
        print("Tweet Sent...")

    except:
        print("Something went wrong!!!")
    
    time.sleep(1600)