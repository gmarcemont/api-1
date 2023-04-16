import keys
import tweepy


client = tweepy.Client(bearer_token=keys.bearer_token)

response = client.get_user(username='elonmusk')

response = client.get_users_followers(44196397)

query = 'ADHD at my job -is:retweet -has:media'

response = client.search_recent_tweets(query=query, max_results=100)

print(response)

# a, b, c, d = response
# print(a)

# prints the client's usernames
# for x in a:
#   print(x)
