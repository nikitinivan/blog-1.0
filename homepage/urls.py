from django.conf.urls import url
from homepage.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),

]
