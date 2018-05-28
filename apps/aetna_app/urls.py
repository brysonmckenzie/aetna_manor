from django.conf.urls import url

from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^accomplishments$', views.accomplishments),
    url(r'^events$', views.events),
    url(r'^gallery$', views.gallery),
    url(r'^remix$', views.remix),
    url(r'^members$', views.members),
    url(r'^volunteers$', views.volunteers),
    url(r'^documents$', views.documents),
    url(r'^member_registration$', views.registration),
]
