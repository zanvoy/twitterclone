from django.shortcuts import render, reverse, HttpResponseRedirect 
from tweet.models import Tweet
from twitteruser.models import SomeUser
from tweet.forms import TweetAddForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

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
        'feed': feed,
    }
    return render(request, 'index.html',data)

def profile(request, username):
    username = SomeUser.objects.get(username=username)
    # tweet_total = len(Tweet.objects.filter(author= username))
    data = {
        'username': username,
        'tweet_total': len(Tweet.objects.filter(author= username)),
        'following': len(username.following.all()),
        'feed': list(Tweet.objects.filter(author= username))
    }
    return render(request, 'profile.html', {'data':data})

def tweet_detail(request, id):
    tweet = Tweet.objects.filter(id=id)
    return render(request, 'recipe.html', {'tweet': tweet})



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
            return HttpResponseRedirect('/')

    form = TweetAddForm()
    return render(request, html, {'form': form})
