from cv.views import home, thankyou
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('thank-you', thankyou, name='thankyou'),
]