from django.urls import path

from qlomb_dashboard.restricted.views import (
    RestrictedView,
)

app_name = "restricted"
urlpatterns = [
    path("restricted-area/", view=RestrictedView.as_view(), name="restricted_area"),
]
