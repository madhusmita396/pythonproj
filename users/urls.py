
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignUpView,CustomLoginView


from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name='user'

urlpatterns = [
    
    path('signup/',SignUpView.as_view(),name='signup'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path("logout/", LogoutView.as_view(), name="logout")
]


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root =settings.STATIC_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()