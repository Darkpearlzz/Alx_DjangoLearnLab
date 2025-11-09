from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view

app_name = 'relationship_app'

urlpatterns = [
    # Existing routes
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # 🔐 Authentication routes
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]

urlpatterns += [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]