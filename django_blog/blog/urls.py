from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # ----- Blog post views -----
    path("", views.index, name="index"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),

    # ----- Post CRUD views -----
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("posts/new/", views.PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),

    # ----- Authentication views -----
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
]
