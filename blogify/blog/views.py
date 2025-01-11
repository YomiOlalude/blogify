from blog.models import BlogPost
from blog.serializers import BlogPostSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class BlogListView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            try:
                blog_post = BlogPost.objects.get(pk=pk)
                serializer = self.serializer_class(blog_post)
                return Response(serializer.data)
            except BlogPost.DoesNotExist:
                return Response(
                    {"message": "Blog post not found."},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            blog_posts = BlogPost.objects.all()
            serializer = self.serializer_class(blog_posts, many=True)
            return Response(serializer.data)


class BlogCreateView(APIView):
    serializer_class = BlogPostSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogUpdateView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        try:
            blog_post = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response(
                {"message": "Blog post not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDeleteView(APIView):
    def delete(self, request, pk=None):
        try:
            blog_post = BlogPost.objects.get(pk=pk)
            blog_post.delete()
            return Response(
                {"message": "Blog post deleted successfully."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except BlogPost.DoesNotExist:
            return Response(
                {"message": "Blog post not found."},
                status=status.HTTP_404_NOT_FOUND
            )
