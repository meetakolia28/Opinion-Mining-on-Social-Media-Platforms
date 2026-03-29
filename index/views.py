from django.shortcuts import render, HttpResponse
import tweepy
from InstagramAPI import InstagramAPI
import p_textclean
import p_naivebayes
import matplotlib.pyplot as plt

username = "de_social"
InstagramAPI = InstagramAPI(username, "0987654321_de")

consumer_key = 'x6K0CMdvaS6LCmJaGFznUZg93'
consumer_secret = 'cN2FtBvLcv4ql71yPnc9C1gVlN5Megm1EX3KcfsWm02BIMXJp0'
access_token = '1105492645579644933-owmnarWVOCY8TBx5OgoPoXDPAFBrlP'
access_token_secret = 'jwkNryMyDbkO5009uFwHcbP0zPPvLRXxIfZ8Ee522K2S3'


def get_api(request):
    # set up and return a twitter api object
    oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(oauth)
    return api


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def twitter(request):
    return render(request, 'twitter.html')


def analyze_twitter(request):
    p = 0
    n = 0
    hashtag = str(request.POST.get('hashtag'))
    num = request.POST.get('num')
    submitbutton = request.POST.get('Submit')
    api = get_api(request)
    tweets = tweepy.Cursor(api.search, tweet_mode='extended', lang='en', q=hashtag).items(int(num))
    sentiment = []
    confidence = []
    tweet_only = []
    for tweet in tweets:
        tweet_only.append(tweet.full_text)
        sentiment.append(p_naivebayes.analyze(p_textclean.clean(tweet.full_text)))
        # confidence.append(p_naivebayes.confidence(p_textclean.clean(tweet.full_text)))
    for s in sentiment:
        if s == '0':
            n = n + 1
        else:
            p = p + 1
    final = dict(zip(tweet_only, sentiment))
    plot(int(p), int(n), int(num), hashtag)
    context = {'submitbutton': submitbutton, 'final': final}
    return render(request, 'twitter.html', context)


def graph(request):
    return render(request, 'graph.html')


def instagram(request):
    InstagramAPI.login()
    has_more_posts = True
    max_id = ""
    myposts = []

    while has_more_posts:
        InstagramAPI.getSelfUserFeed(maxid=max_id)
        if InstagramAPI.LastJson['more_available'] is not True:
            has_more_posts = False

        max_id = InstagramAPI.LastJson.get('next_max_id', '')
        myposts.extend(InstagramAPI.LastJson['items'])
    iter = 0
    urls = []
    ids = []
    comcntlst = []
    likelist = []
    cid = '_11545205672'
    for i in reversed(InstagramAPI.LastJson['items']):
        for c in i['image_versions2']['candidates']:
            if iter % 2 != 0:
                urls.append(c['url'])
            iter = iter + 1
        id = i['id']
        id = id.replace(cid, '')
        ids.append(id)
        InstagramAPI.getMediaComments(id)
        comcnt = 0
        for c in (InstagramAPI.LastJson['comments']):
            comcnt += 1
        comcntlst.append(comcnt)
        like = i['like_count']
        likelist.append(like)

    final = dict(zip(urls, ids))
    meta = dict(zip(comcntlst, likelist))
    context = {'final' : final, 'meta': meta}
    return render(request, 'instagram.html', context)


def analyze_instagram(request):
    p = 0
    n = 0
    cid = '_11545205672'
    media_id = str(request.POST.get('postid'))
    media_id = media_id + cid
    InstagramAPI.login()
    has_more_posts = True
    max_id = ""
    myposts = []
    sentiment = []
    comments = []
    while has_more_posts:
        InstagramAPI.getSelfUserFeed(maxid=max_id)
        if InstagramAPI.LastJson['more_available'] is not True:
            has_more_posts = False

        max_id = InstagramAPI.LastJson.get('next_max_id', '')
        myposts.extend(InstagramAPI.LastJson['items'])

    for i in reversed(InstagramAPI.LastJson['items']):
        InstagramAPI.getMediaComments(media_id)
        cc = 0
        for c in (InstagramAPI.LastJson['comments']):
            sentiment.append(p_naivebayes.analyze(p_textclean.clean(c['text'])))
            comments.append(c['text'])
            cc += 1
    for s in sentiment:
        if s == '0':
            n = n + 1
        else:
            p = p + 1
    plot(int(p), int(n), int(cc), media_id)
    final = dict(zip(comments, sentiment))
    context = {'final' : final}
     return render(request, 'instagram_analyze.html', context)


def facebook(request):
    return render(request, 'facebook.html')


def percentage(part, whole):
    return 100 * float(part) / float(whole)


def plot(p, n, num, hashtag):
    positive = percentage(p, num)
    negative = percentage(n, num)
    labels = ['Positive[' + str(positive) + '%]'], ['Negative[' + str(negative) + '%]']
    sizes = [positive, negative]
    colors = ['green', 'red']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title("Reacting on " + hashtag + ".For " + str(p) + " pos & " + str(n) + " neg out of " + str(num) + " tweets." )
    plt.axis('equal')
    plt.savefig("E:/Python/omosmp/static/pie")

