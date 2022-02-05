from django.urls import path
from .import views
from .views import AboutusView, HomePageView,FaqView

urlpatterns = [
 path('', HomePageView.as_view(), name='home'),
 path('about/', AboutusView.as_view(), name='about'),
 path('FAQ/', FaqView.as_view(), name='faq'),

]

