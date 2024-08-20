import tweepy
#####%%%%%%%%%%%%%%%% Auhenticate %%%%%%%%%%%%%%%%%
# auth = tweepy.OAuth2BearerHandler("Bearer Token here")
# client = tweepy.Client("Bearer Token here")
auth = tweepy.OAuth1UserHandler(consumer_key='', consumer_secret='', access_token='', access_token_secret='')
api = tweepy.API(auth)
print(api)

#%%%%%%%%%%%%%%%% Search %%%%%%%%%%
api.search_tweets(q='Python', geocode='')
trend_tweet = api.closest_trends(lat='', long='')
api.available_trends()
api.get_place_trends(id='woeid number')


################# for myself
api.retweet(id=' tweet id to retweet')
api.unretweet(id= 'ID of the retweet to unretweet')

api.create_friendship(screen_name='', user_id='')
api.destroy_friendship(screen_name='', user_id='')
api.update_friendship(screen_name='',user_id='',device=False)

api.get_settings()
api.get_saved_searches()
api.remove_profile_banner()
api.update_profile(name='Python Hero',
                 url='', 
                 location='Pakistan', 
                 description='Python Develope',
                 profile_link_color='FOO', 
                 include_entities=True, 
                 skip_status=False)
api.update_profile_banner(filename='', file, 
                          width='in px', height='in px',
                          offset_left='', offset_top='')
api.create_saved_search(query='')
api.destroy_saved_search(id='search id')

api.create_block(screen_name='', user_id='')
api.destroy_block(screen_name='', user_id='')
api.get_blocked_ids()
api.create_block()
api.get_blocks()
api.perform_block(screen_name='', user_id='',perform_block =True)

api.send_direct_message(recipient_id='', text='',
                     attachment_type='Can be media or location.', 
                     attachment_media_id='')

api.media_upload(filename='',file, chunked, media_category)
API.simple_upload(filename='', file, media_category, additional_owners )
######## Search users and users ids %%%%%%%%%%%%%%%%%55
api.get_profile_banner(user_id='',screen_name='')
api.get_retweeter_ids(id=' tweet id ')


api.search_users(q='Python Developer]')
api.get_user(user_id='',screen_name='')

api.get_followers(user_id='',screen_name='')
api.get_follower_ids(user_id='', screen_name='')
api.get_friends(id='',screen_name='')
api.get_friend_ids(id='',screen_name='')

api.get_friendship( source_id='', source_screen_name='', target_id='', target_screen_name='')



user = api.get_user(screen_name="Twitter")
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)