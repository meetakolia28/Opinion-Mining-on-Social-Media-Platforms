from django.conf.urls import url
from . import views

app_name = 'index'

urlpatterns = [
    # /index/
    # url('^$', views.index, name='index'),

    # /home/
    url('^$', views.home, name='home'),

    # /home/about/
    url('^about/$', views.about, name='about'),

    # /home/twitter/
    url('^twitter/$', views.twitter, name='twitter'),

    # /home/twitter/analyze_twitter
    url('^twitter/show$', views.analyze_twitter, name='analyze_twitter'),

    # /home/graph
    url('graph/$',views.graph, name='graph'),

    # /home/instagram
    url('^instagram/$', views.instagram, name='instagram'),

    # /home/instagram/analyze_instagram
    url('instagram/analyze_instagram$', views.analyze_instagram, name='analyze_instagram'),

    # /home/facebook
    url('^facebook/$', views.facebook, name='facebook'),
    # /index/values
    # url('^values$', views.values, name='values'),

    # url('^twitter/test2/$', views.test2, name='test2'),
]

