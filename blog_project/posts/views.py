from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly


class PostList(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated, )  # agar ro'yxatdan otgan bo'lsa
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated, ) # agar ro'yxatdan otgan bo'lsa
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

