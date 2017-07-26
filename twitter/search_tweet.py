from twitter import *


#auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
#                    CONSUMER_KEY, CONSUMER_SECRET)

t =Twitter(auth = OAuth("889439018282123264-ypvLZcI7Tt0nBA3yWvul6IfqvUMMdV0", 
            "SrH7ptZ0mIu99Cmg5LbFe2t0AFCMOglGz7peYFF539KgS",   
            "oiAlipRHReALc5EEGfxFzBl0I", 
            "iP18pav5D00ftGawVLsg9mORIKN9tgAcf16seby5IpbpDmVtZ2"))  


pythonTweets = t.search.tweets(q = "#JungTW_LEO")
print(pythonTweets)
