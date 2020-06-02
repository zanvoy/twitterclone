from django.shortcuts import render, reverse, HttpResponseRedirect 
from tweet.models import Tweet
from twitteruser.models import SomeUser
# from tweet.forms import TweetAddForm
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
    
        
    # .filter(author__in=[request.user].extend(request.user.following.all()))
    data = {
        'username': username,
        'tweet_total': len(Tweet.objects.filter(author= request.user)),
        'following': len(following),
        'feed': feed,
    }
    return render(request, 'index.html',data)

def profile(request, id):
    person = Author.objects.get(id=id)
    recipe = Recipe.objects.filter(author=person)
    return render(request, 'author.html', {'person': person, 'recipe': recipe})

def tweet_detail(request, id):
    tweet = Tweet.objects.filter(id=id)
    return render(request, 'recipe.html', {'tweet': tweet})



# @login_required
# def recipeadd(request):
#     html = 'addform.html'

#     if request.method == 'POST':
#         form = RecipeAddForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Recipe.objects.create(
#                 title = data['title'],
#                 description = data['description'],
#                 req_time = data['req_time'],
#                 instructions = data['instructions'],
#                 author = data['author']
#             )
#             return HttpResponseRedirect('/')

#     form = RecipeAddForm()
#     return render(request, html, {'form': form})
