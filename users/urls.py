from django.urls import path
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    # path('', UsersListView.as_view(), name='home'),

]
