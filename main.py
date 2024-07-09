"""hastag = "programming"
medias = cl.hashtag_medias_recent(hastag, 20)

for i, media in enumerate(medias):
    cl.media_like(media.id)
    print(f"Likes post number {i+1} of hashtag")
"""
from instagrapi import Client
import time
def check_followers():
    cl = Client()
    cl.login("", "")
    list_id_base = []
    #david = cl.user_info_by_username_v1('davids.exe').dict()

    dic_followers = cl.user_followers("4262787278")
    for i, j in dic_followers.items():
        list_id_base.append(i)
    return list_id_base


def difference(dic_base):
    nouveau_dic = check_followers()
    nouveau_followers = []
    followers_perdu = []
    if len(nouveau_dic) != dic_base:
        for i in range(len(dic_base)):
            for j in range(len(nouveau_dic)):
                if dic_base[i] != nouveau_dic[j]:
                    nouveau_followers.append(nouveau_dic[j])
            if not dic_base[i] in nouveau_dic:
                followers_perdu.append(dic_base[i])
    return nouveau_followers, followers_perdu

list_base = check_followers()

while True:
    difference(list_base)
    time.sleep(3600)
