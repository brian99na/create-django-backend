from ..serializers.user import UserSerializer
from django.contrib.auth import authenticate, login, logout

from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from ..models.user import User

class SignUp(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        created_user = UserSerializer(data=request.data['user'])
        if created_user.is_valid():
            created_user.save()
            return Response({'user': created_user.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(created_user.errors, status=status.HTTP_400_BAD_REQUEST)

class SignIn(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        data = request.data['user']
        user = authenticate(request, email=data['email'], password=data['password'])

        if user is not None:
            login(request, user)

            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            user.token = token.key
            user.save()

            return Response({
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'user_name': user.user_name,
                    'token': token.key
                }
            })
        else:
            return Response({'msg': 'Username/Password is invalid'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


# class ChangePassword(generics.UpdateAPIView):
#     def patch(self, request):
#         user = request.user
#         old_pw = request.data['passwords']['old']
#         new_pw = request.data['passwords']['new']
#         # This is included with the Django base user model
#         # https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User.check_password
#         if not user.check_password(old_pw):
#             return Response({ 'msg': 'Wrong password' }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#         # set_password will also hash the password
#         # https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User.set_password
#         user.set_password(new_pw)
#         user.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class SignOut(generics.CreateAPIView):
    def delete(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        user.token = None
        user.save()
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetUserName(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        user_data = UserSerializer(user).data
        return Response(user_data)
        print(user)

class GetId(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, pk):
        user = User.objects.get(user_name=pk)
        user_data = UserSerializer(user).data
        return Response(user_data)
        print(user)