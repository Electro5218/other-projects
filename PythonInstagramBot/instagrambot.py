from time import sleep
from instabot import Bot

instagrambot = Bot()

#logowanie
instagrambot.login(username="", password="")
#follow user
instagrambot.follow("")
#message user
instagrambot.send_message("")
#comment
user_id = instagrambot.get_user_id_from_username("")
media_id = instagrambot.get_last_user_medias(user_id)
instagrambot.comment(media_id,"")

#list of followers of victim
followers_list = instagrambot.get_user_followers("")
following_list = instagrambot.get_user_following("")

for count, each_follower in enumerate(followers_list):
    if count > 4:
        continue
    sleep(5)
    print(instagrambot.get_username_from_user_id(each_follower))
for count1, each_following in enumerate(following_list):
    if count1 > 4:
        continue
    sleep(5)
    print(instagrambot.get_username_from_user_id(each_following))

instagrambot.logout()
