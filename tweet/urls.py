from django.urls import path
from tweet import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('tweet/<int:id>/', views.tweet_detail, name='tweet'),  
    path('<username>', views.profile, name='profile'),
    path('tweetadd/', views.tweetadd),
    path('follow/<friend>', views.follow, name='follow')
]