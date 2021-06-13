# Samir Mitha - (c) 2021
import StatusTTC as ttc
import StatusYRT as yrt

def ttc_tweet_short(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
	"""Shortens tweet informations and splits into categories

    Parameters
    ----------
    CONSUMER_KEY : str
    	tweepy API key
    CONSUMER_SECRET : str
    	tweepy API key
    ACCESS_TOKEN : str
    	tweepy API key
    ACCESS_TOKEN_SECRET : str
    	tweepy API key

    Returns
    -------
    tweets: list
        list of tweet objects
    """
	status = ttc.GetTTCStatus(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	j = 0
	for i in status:
		j = j + 1
		date = (i[0].split(', '))[0]
		time = (i[0].split(', '))[1]
		condition_full = i[1].split(': ')
		if len(condition_full) > 1:
			condition = (i[1].split(': '))[0]
			condition_time = int((i[1].split(': '))[1].replace(' minutes', ''))/60
		else:
			condition = (i[1].split(': '))[0]
			condition_time = None
		full_route =(i[2].split(' : '))
		route = full_route[0]
		if len(full_route) > 1:
			if " and " in full_route[1]:
				start = (full_route[1].split(' and '))[0]
				end = (full_route[1].split(' and '))[1]
			elif " to " in full_route[1]:
				start = (full_route[1].split(' to '))[0]
				end = (full_route[1].split(' to '))[1]
			else:
				start = full_route[1]
				end = None
		else:
			pass
		tweet = [j, date, time, condition, condition_time, route, start, end]
		# tweet object contains:
		# j -> tweet number
		# date -> tweet date
		# time -> tweet time
		# condition -> traffic status condition
		# condition_time -> estimated duration of condition (in minutes)
		# route -> TTC line number
		# start -> start location of transit condition
		# end -> end location of transit condition
		tweets[i] = tweet
	return(tweets)

def yrt_tweet_short(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
	"""Shortens tweet informations and splits into categories

    Parameters
    ----------
    CONSUMER_KEY : str
    	tweepy API key
    CONSUMER_SECRET : str
    	tweepy API key
    ACCESS_TOKEN : str
    	tweepy API key
    ACCESS_TOKEN_SECRET : str
    	tweepy API key

    Returns
    -------
    tweets: list
        list of tweet objects
    """
    status = yrt.GetTTCStatus(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    j = 0
    for i in status:
		j = j + 1
		date = (i[0].split(', '))[0]
		time = (i[0].split(', '))[1]
		condition_full = i[1].split(': ')
		if len(condition_full) > 1:
			condition = (i[1].split(': '))[0]
			condition_time = int((i[1].split(': '))[1].replace(' minutes', ''))/60
		else:
			condition = (i[1].split(': '))[0]
			condition_time = None
		full_route =(i[2].split(' : '))
		route = full_route[0]
		if len(full_route) > 1:
			if " and " in full_route[1]:
				start = (full_route[1].split(' and '))[0]
				end = (full_route[1].split(' and '))[1]
			elif " to " in full_route[1]:
				start = (full_route[1].split(' to '))[0]
				end = (full_route[1].split(' to '))[1]
			else:
				start = full_route[1]
				end = None
		else:
			start = None
			end = None
			pass
		tweet = [j, date, time, condition, condition_time, route, start, end]
		# tweet object contains:
		# j -> tweet number
		# date -> tweet date
		# time -> tweet time
		# condition -> traffic status condition
		# condition_time -> estimated duration of condition (in minutes)
		# route -> TTC line number
		# start -> start location of transit condition
		# end -> end location of transit condition
		tweets[i] = tweet
	return(tweets)