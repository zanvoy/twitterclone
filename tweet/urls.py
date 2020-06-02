from django.urls import path
from tweet import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('/tweet/<int:id>/', views.tweet_detail, name='tweet'),  
    path('/profile/<int:id>', views.profile)
    # path('tweetadd/', views.tweetadd, name='tweetadd'),
    # path('profile/<int:id>', views.profile, name='profile'),
]