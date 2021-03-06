from django.shortcuts import render, reverse, HttpResponseRedirect 
from tweet.models import Tweet
from twitteruser.models import SomeUser
from tweet.forms import TweetAddForm
from notification.models import Notification
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import re

@login_required
def index(request):
    username = request.user.username
    feed = []
    feed.extend(list(Tweet.objects.filter(author= request.user)))
    following = request.user.following.all()
    for item in following:
        feed.extend(Tweet.objects.filter(author= item))
    feed.sort(key=lambda r: r.date, reverse=True)


    data = {
        'username': username,
        'tweet_total': len(Tweet.objects.filter(author= request.user)),
        'following': len(following),
        'feed': feed
    }
    return render(request, 'index.html',data)

def profile(request, username):
    username = SomeUser.objects.get(username=username)
    if request.user.is_authenticated:
        isFollowing = username in list(request.user.following.all())
    else:
        isFollowing = None
    data = {
        'username': username,
        'tweet_total': len(Tweet.objects.filter(author= username)),
        'following': len(username.following.all()),
        'feed': list(Tweet.objects.filter(author= username)),
        'isFollowing' : isFollowing
    }
    return render(request, 'profile.html', {'data':data})


def tweet_detail(request, id):
    tweet = Tweet.objects.get(id=id)
    return render(request, 'tweet_detail.html', {'tweet': tweet})



@login_required
def tweetadd(request):
    html = 'tweetadd.html'

    if request.method == 'POST':
        form = TweetAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                body = data['body'],
                author = request.user
            )
            txt = data['body']
            notify = re.findall(r'\@\w*',txt)
            for item in notify:
                try:
                    notifyee = SomeUser.objects.get(username=item[1:])
                except SomeModel.DoesNotExist:
                    notifyee = None
                if notifyee != None:
                    Notification.objects.create(
                        notifyee = notifyee,
                        tweet = Tweet.objects.last()
                    )
            return HttpResponseRedirect('/')

    form = TweetAddForm()
    return render(request, html, {'form': form})

def follow(request, friend):
    following = list(request.user.following.all())
    friendObj = SomeUser.objects.get(username=friend)
    if friendObj in following:
        request.user.following.remove(friendObj)
        request.user.save()
    else:
        request.user.following.add(friendObj)
        request.user.save()
    return HttpResponseRedirect('/'+friend)

@login_required
def notification(request):
    username = request.user.username
    feed = []
    feed.extend(list(Notification.objects.filter(notifyee = request.user)))
    feed.sort(key=lambda r: r.tweet.date, reverse=True)
    following = request.user.following.all()


    data = {
        'username': username,
        'tweet_total': len(Tweet.objects.filter(author= request.user)),
        'following': len(following),
        'feed': feed,
    }
    Notification.objects.filter(notifyee = request.user).delete()
    return render(request, 'notification.html',data)

