from rest_framework import generics, permissions
from projects_app.models import Project
from contact_app.models import ContactMessage
from .serializers import ProjectSerializer, ContactSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by('-created_date')
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]

class ContactCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
