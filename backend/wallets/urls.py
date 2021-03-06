from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'wallets', views.WalletViewSet)
wallet_history = views.WalletViewSet.as_view({'get': 'history'})
# router.register(r'operations', views.OperationsViewSet)

operation_list = views.OperationsViewSet.as_view({'get': 'list', 'post': 'create'})
operation_delete = views.OperationsViewSet.as_view({'delete': 'destroy'})
# router.register(r'wallets/<id>/operations', operation_list, basename='operation')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('phrases/', views.PhraseView.as_view()),
    path(r'wallets/<pk>/history', wallet_history, name='List Wallet History'),
    path(r'wallets/<pk>/operations', operation_list, name='List Operations'),
    path(r'wallets/<pk_wallet>/operations/<pk_op>', operation_delete, name='Delete Operations'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
