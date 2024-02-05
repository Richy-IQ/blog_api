from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.views.decorators.csrf import csrf_exempt


from .views import PostersList, PostersDetail, CommentListCreateView, CommentDetailView, UserList, UserDetail


urlpatterns = [
    path('api-token-auth/', csrf_exempt(obtain_auth_token), name='api_token_auth'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path("<int:pk>/", PostersDetail.as_view(), name="post_detail"),
    path("", PostersList.as_view(), name="post_list"),
    path("comments/", CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    
]