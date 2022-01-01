from django.urls import path
from .views.users import SignUp, SignIn, SignOut, GetUserName, GetId
from .views.posts import PostsView, PostView, AllView, UserPostsView, SingleView

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('get-user/<int:pk>/', GetUserName.as_view(), name='get-user'),
    path('get-id/<str:pk>/', GetId.as_view(), name='get-id'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('post/<int:pk>/', PostView.as_view(), name='post'),
    path('all/', AllView.as_view(), name='all'),
    path('user-posts/<int:pk>/', UserPostsView.as_view(), name='user-posts'),
    path('post/<int:user_pk>/<int:pk>/', SingleView.as_view(), name='post_public'),
]