from django.urls import re_path
from .views import login, launch, get_jwks, configure, score, scoreboard

urlpatterns = [
    re_path(r'^login/$', login, name='game-login'),
    re_path(r'^launch/$', launch, name='game-launch'),
    re_path(r'^jwks/$', get_jwks, name='game-jwks'),
    re_path(r'^configure/(?P<launch_id>[\w-]+)/(?P<difficulty>[\w-]+)/$', configure, name='game-configure'),
    re_path(r'^api/score/(?P<launch_id>[\w-]+)/(?P<earned_score>[\w-]+)/(?P<time_spent>[\w-]+)/$', score,
            name='game-api-score'),
    re_path(r'^api/scoreboard/(?P<launch_id>[\w-]+)/$', scoreboard, name='game-api-scoreboard'),
]
