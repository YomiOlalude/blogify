from account.models import User
from account.serializers import UserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class UserListView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            try:
                user = User.objects.get(pk=pk)
                serializer = self.serializer_class(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response(
                    {"message": "User not found."},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            users = User.objects.all()
            serializer = self.serializer_class(users, many=True)
            return Response(serializer.data)


class UserCreateView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {"message": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(
                {"message": "User deleted successfully."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except User.DoesNotExist:
            return Response(
                {"message": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )
