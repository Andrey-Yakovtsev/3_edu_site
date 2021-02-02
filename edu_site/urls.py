from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('courses.urls', namespace='courses')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('graphql/', GraphQLView.as_view(graphiql=True), name='graphql-api'),
    # JWT urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
