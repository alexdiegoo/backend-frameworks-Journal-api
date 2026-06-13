from rest_framework import permissions


def is_editor(user):
    """True se o usuário pertence ao grupo 'Editor'."""
    return user.is_authenticated and user.groups.filter(name='Editor').exists()


class IsOwner(permissions.BasePermission):
    """Permite acesso só ao dono do objeto."""

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsOwnerOrEditorReadOnly(permissions.BasePermission):
    """
    Dono tem acesso total ao objeto.
    Membros do grupo 'Editor' podem apenas LER (somente leitura)
    entradas de qualquer usuário — nunca editar ou apagar.
    """

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        if request.method in permissions.SAFE_METHODS and is_editor(request.user):
            return True
        return False
