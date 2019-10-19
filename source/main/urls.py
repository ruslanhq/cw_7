"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, ChoiceCreate
from webapp.views.choice_views import ChoiceCreatePoll, ChoiceUpdate
from webapp.views.poll_views import PollView, PollCreate, PollUpdate, PollDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll_view'),
    path('poll/create/', PollCreate.as_view(), name='poll_create'),
    path('poll/update/<int:pk>/', PollUpdate.as_view(), name='poll_update'),
    path('poll/delete/<int:pk>/', PollDelete.as_view(), name='poll_delete'),
    path('choice/create/', ChoiceCreate.as_view(), name='choice_create'),
    path('choice/create/<int:pk>/', ChoiceCreatePoll.as_view(), name='choice_create_poll'),
    path('choice/update/<int:pk>/', ChoiceUpdate.as_view(), name='choice_update')
]
