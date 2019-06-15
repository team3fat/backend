from django.conf.urls import url
from diquecito.views import *

urlpatterns = [
    url(r'^Usuario/$', UsuarioList.as_view(), name="Usuario"),
    url(r'^Post/$', PostList.as_view(), name="Post"),
    url(r'^Reservation/$', ReservationList.as_view(), name="Reservation"),
    url(r'^Qualification/$', QualificationList.as_view(), name="Qualification")
]
