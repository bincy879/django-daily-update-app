from django.urls import path
from update_app import views

urlpatterns=[
    path("form_fn/",views.form_fn,name="form_fn"),
    path("save_data/",views.save_data,name="save_data"),
    path("table_fn/",views.table_fn,name="table_fn")
]