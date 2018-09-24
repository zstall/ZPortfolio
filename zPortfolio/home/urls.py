from django.conf.urls import url
from home import views
# from BetterBeerBlog import views

urlpatterns = [
    url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^thanks/$', views.ThanksView.as_view(), name='thanks'),
    # url(r'^home/$', views.get_contact, name='get_contact')
    # url(r'^BetterBeerBlog/$', views.PostListView.as_view(), name='post_list'),
]
