#resume urls
from django.urls import path
from . import views
app_name = 'resume'
urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio'),
    #path('education/', views.education, name='education')
    #path('resume.html', views.resume, name='resume'),
    #path('portfolio.html', views.portfolio, name='portfolio'),
    #path('contact.html', views.contact, name='contact'),

]
