from .views import *

from django.urls import path,include
urlpatterns = [
    path('signup/', SingupView_instutition.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', RefreshView.as_view(), name='refresh'),

]