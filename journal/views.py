from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import JournalEntry
from .serializers import JournalEntrySerializer
from .permissions import IsOwner


class JournalEntryViewSet(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return JournalEntry.objects.filter(
            author=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
