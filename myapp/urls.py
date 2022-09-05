
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='quotes'

urlpatterns = [
    
    path('',views.QuoteHomeView.as_view(),name='list'),
    path('tag/<slug:tag>',views.QuoteTagListView.as_view(),name='tag'),
    path('quotes/<int:pk>/',views.QuoteDetailView.as_view(),name='detail'),
    path('quotes/create/',views.QuoteCreateView.as_view(),name='create'),
    path('quotes/<int:pk>/update/',views.QuoteUpdateView.as_view(),name='update'),
    path('quotes/<int:pk>/delete/',views.QuoteDeleteView.as_view(),name='delete'),


    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root =settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()