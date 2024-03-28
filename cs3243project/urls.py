"""cs3243project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin, auth
from kingOfTheHill.views import home_view, ranking_view, user_view, additional_upload_view, object_delete, final_tournament_view
urlpatterns = [
    url(r'^$', home_view, name='home'),
    url(r'^user/', user_view, name='user'),
    url(r'^finalTournament/', final_tournament_view, name='Final tournament'),
    url(r'^delete_upload/(?P<object_id>[0-9]+)$', object_delete, name='delete_object'),
    url(r'^upload/', additional_upload_view, name='upload'),
    url(r'^ranking/', ranking_view, name='ranking'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/profile', home_view, name='home')
]
