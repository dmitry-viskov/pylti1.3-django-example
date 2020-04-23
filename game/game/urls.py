from django.conf import settings
from django.conf.urls import url
from django.urls import include, path
from .views import login, launch, get_jwks, configure, score, scoreboard

urlpatterns = [
    url(r'^login/$', login, name='game-login'),
    url(r'^launch/$', launch, name='game-launch'),
    url(r'^jwks/$', get_jwks, name='game-jwks'),
    url(r'^configure/(?P<launch_id>[\w-]+)/(?P<difficulty>[\w-]+)/$', configure, name='game-configure'),
    url(r'^api/score/(?P<launch_id>[\w-]+)/(?P<earned_score>[\w-]+)/(?P<time_spent>[\w-]+)/$', score,
        name='game-api-score'),
    url(r'^api/scoreboard/(?P<launch_id>[\w-]+)/$', scoreboard, name='game-api-scoreboard'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
