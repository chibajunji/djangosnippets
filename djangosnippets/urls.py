from django.contrib import admin
from django.urls import path, include

from snippets.views import top

urlpatterns = [
    path('', top, name='top'),
    path('snippets/', include('snippets.urls')),  # snippets/urls.pyの読込
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
