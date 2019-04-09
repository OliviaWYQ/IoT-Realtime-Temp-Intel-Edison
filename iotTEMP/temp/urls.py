#  Name:    Maoxin Hou,  Xiren Zhou, Yiqian Wang
#  UNI:   mh3895,  xz2754,  yw3225
#  Group Code: MOHAfrom django.conf.urls import url



from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]