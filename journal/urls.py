from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import JournalEntryViewSet, PublicJournalEntryListView

router = DefaultRouter()
router.register(r'entries', JournalEntryViewSet, basename='entry')

urlpatterns = [
    path('journal/public/', PublicJournalEntryListView.as_view(), name='public-entries'),
]

urlpatterns += router.urls
