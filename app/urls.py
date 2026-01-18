from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.HomeView,name="home"),
    path('success/', views.success_page, name='success'),
    path('search/', views.search_student, name='result'),
    path('payment/', views.payment_view, name='payment'),
    path('verify-payment/', views.verify_payment, name='verify_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('apply/', views.tutor_application, name='tutor_application'),  # URL to display the tutor application form
    path('thank-you/', views.thank_you, name='thank_you'), 
    path('privacy/', views.privacy_view, name='privacy'), 
    path('terms/', views.Term_view, name='terms'),  
    path('base/', views.base_view, name='base'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)