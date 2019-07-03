from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('sell/', views.ListingCreateView, name='sell'),
    path('buy', views.ListingListFilter.as_view(), name='buy'),
    path('search', views.search, name='search'),
    path('individual/<int:listing_id>', views.individual, name='individual'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
