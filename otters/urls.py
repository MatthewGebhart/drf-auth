from django.urls import path
from .views import OtterList, OtterDetail


urlpatterns = [
    path('', OtterList.as_view(), name='otter_list'),
    path('<int:pk>/', OtterDetail.as_view(), name="otter_detail"),
]

