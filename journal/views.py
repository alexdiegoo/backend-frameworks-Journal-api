from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import JournalEntry
from .serializers import (
    JournalEntrySerializer,
    PublicJournalEntrySerializer,
)
from .permissions import IsOwnerOrEditorReadOnly, is_editor


class JournalEntryViewSet(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrEditorReadOnly]

    def get_queryset(self):
        # Editores enxergam as entradas de todos (somente leitura);
        # usuários comuns enxergam apenas as próprias.
        if is_editor(self.request.user):
            return JournalEntry.objects.all()
        return JournalEntry.objects.filter(
            author=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PublicJournalEntryListView(generics.ListAPIView):
    """Feed público: entradas marcadas como is_public, sem precisar de login."""
    queryset = JournalEntry.objects.filter(is_public=True)
    serializer_class = PublicJournalEntrySerializer
    permission_classes = [AllowAny]
