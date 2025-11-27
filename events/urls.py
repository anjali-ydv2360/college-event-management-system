from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    # Admin URLs
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/add_event/', views.add_event, name='add_event'),
    path('admin/edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('admin/delete_event/<int:event_id>/', views.delete_event, name='delete_event'),

    # Student URLs
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/register_event/<int:event_id>/', views.register_event, name='register_event'),
]