# Dumitru Cotorobai - (c) 2021
import sys
from datetime import datetime
import tweepy
import pandas as pd
import re
from array import *

def GetLocationEndPoint(TweetString, start):
    #Common delimeters in the specific location substring
    end = TweetString.find(' while ')
    if(end == -1):
        end = TweetString.find(' due ')
        if(end  == -1):
            end = TweetString.find('.')
            if(end < start):
                end = len(TweetString)
    
    return end

def GetTTCTweetLocation(TweetString):
    
    #Set Initial Location
    location = ''

    #Remove TTC Update substring
    if((TweetString.find('UPDATE:') > -1) or (TweetString.find('Update:') > -1)):
        TweetString = TweetString[8:-1]
    
    #Start at String Index 0
    start = 0
    end = 0
    
    #Remove Additional Spaces of Substring
    for i in range(0, len(TweetString)):
        if(TweetString[i] != ' '):
            TweetString = TweetString[i:]
            break

    
    #Look for Keyword in Tweet
    keywords = [' at ', ' between ', ' near ', ' via ', ' from ']

    for keyword in keywords:
        
        match = TweetString.find(keyword)
        if(match > -1):
            if keyword == ' between ':
                start = TweetString.find(' between ') + 9
                end = GetLocationEndPoint(TweetString = TweetString, start = start)
                break
            
            if keyword == ' at ':
                start = TweetString.find(' at ') + 4
                end = GetLocationEndPoint(TweetString = TweetString, start = start)
                break

            if keyword == ' near ':
                start = TweetString.find(' near ') + 6
                end = GetLocationEndPoint(TweetString = TweetString, start = start)
                break

            if keyword == ' via ':
                start = TweetString.find(' via ') + 5
                end = GetLocationEndPoint(TweetString = TweetString, start = start)
                break
            
            if keyword == ' from ':
                start = TweetString.find(' from ') + 6
                end = GetLocationEndPoint(TweetString = TweetString, start = start)
                break
    
    #Check if a specific location is found
    if(start < end):
        SpecificLocation = TweetString[start : end]
    else:
        SpecificLocation = ''

    #Get Main Route Path
    keywords = [r'continues to', r':']
    for keyword in keywords:
        end = TweetString.find(keyword)
        if(end > -1):
            if keyword == keywords[1]:
                location = TweetString[0 : end]
            else:
                location = TweetString[0 : end - 1] 
            break



    #Did not find an exact location thus return route
    if SpecificLocation == '':
        return location            
    return location + ' : ' + SpecificLocation



def GetTTCTweetStatus(TweetString):
    keywords = ['Delay', 'Resume', 'No Service', 'Detour', 'Collision']

    #Look for Keywords in Tweet
    for keyword in keywords:
        match = re.search(keyword, TweetString, re.IGNORECASE)
        if match:
            match = re.search(r'\d\d minutes', TweetString, re.IGNORECASE)
            if match:
                return (keyword + ': ' + match.group())
            else:
                return keyword
    
    return ''

def GetTTCStatus(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    
    #Connect to API
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    #User Information
    username = r'TTCnotices'
    count = 50
    page = 1

    #GetTweets 
    i = 1
    j = 1
    tweets_index = []
    tweets_delay = []
    tweets_delaytime = []
    tweets_location = []
    tweets_date = []
    tweets_text = []

    while True:
        if(i <= page):

            tweets = api.user_timeline(id = username, count = count, page = page, tweet_mode = 'extended')
            for tweet in tweets:
                #Print to console Index, Time, and Tweet
                #print(str(j) + '. \t{' + str(tweet.created_at) + ' }\t' + tweet.full_text)
                tweets_index.append(j)

                
                #Get Time Zone Right
                time = tweet.created_at.strftime('%H')
                time = int(time)
                time = (time - 5)%24
                time = str(time)
                #tweets_date.append(tweet.created_at.strftime(time + ':%M:%S'))
                tweets_date.append(tweet.created_at.strftime('%m/%d/%Y, '+ time + ':%M:%S'))

                tweets_delay.append(GetTTCTweetStatus(tweet.full_text))
                if(tweets_delay[-1] == ''):
                    tweets_location.append('')
                else:
                    tweets_location.append(GetTTCTweetLocation(tweet.full_text))
                tweets_text.append(tweet.full_text)

                #Increment Tweet Index
                j += 1
            
            #Increment Page Index
            i += 1
        else:
            break

    #Store Info to Excel Spreadsheet
    #d = {'Index' : tweets_index, 'Date' : tweets_date, 'Status' : tweets_delay, 'Location': tweets_location, 'Text' : tweets_text}
    #df = pd.DataFrame(data = d, columns = ['Index', 'Date', 'Status', 'Location', 'Text'])
    #df.to_excel('Book1.xlsx')

    #Object to return to main
    ReturnObject = []

    #Return time, status flag, and location
    for i in range(0, len(tweets_delay) - 1):
        if tweets_delay[i] != '':
            ReturnObject.append([tweets_date[i], tweets_delay[i], tweets_location[i]])
    
    return ReturnObject

