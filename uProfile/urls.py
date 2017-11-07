from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


app_name = 'uProfile'

urlpatterns = [
    # /music/
    url(r'^login/$',auth_views.login,{'template_name': 'uProfile/login.html'},name="login"),
    url(r'^logout/$',auth_views.logout,{'template_name': 'uProfile/logout.html'},name="logout"),
    url(r'^$', views.Headings.as_view(), name='index'),  # default section
    url(r'^register/$',views.UserFormView.as_view(),name='register'), #registration
    # /music/id eg: /uProfile/12
    url(r'^test/$',views.index,name='test'),
    url(r'^(?P<pk>[-]*[0-9]+)/$', views.Quesinfo.as_view(), name='details'),
    url(r'^Qtn/(?P<c_id>[0-9]+)/$',views.test,name='Qtn'),
    url(r'^help/$',views.help,name='help'),
    url(r'^no/$',views.no,name = 'no'),
    url(r'^uProfile/add/$',views.QuestionAdd.as_view(),name='QandA_add'),
]
