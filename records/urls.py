from django.urls import path
from .views import index, get_records, record_detail, csrf_token

urlpatterns = [
    path('', index, name='index'),
    path('api/records/', get_records, name='get_records'),
    path('api/records/<int:id>/', record_detail, name='record_detail'),
    path('api/csrf/', csrf_token, name='csrf_token'),  # CSRF token endpoint
]
