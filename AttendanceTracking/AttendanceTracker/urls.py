from django.urls import path
from . import views

urlpatterns = [
path('', views.home, 
     name="home"),
path('Attendance/home', views.home, 
     name="home"),
path('Attendance/view', views.view_attendance_page, 
     name='view_attendance'),
path('Attendance/edit', views.edit_attendance_page, 
     name='edit_attendance'),
path('Attendance/mark', views.mark_attendance_page, 
     name='mark_attendance'),
path('Attendance/marked', views.attendance_marked, 
     name='attendance_marked'),
path('Attendance/view_table', views.view_table, 
     name='view_table'),
path('Attendance/notify', views.notification, 
     name='notification'),
path('Attendance/notified', views.notified, 
     name='notified'),
path('Attendance/students_to_notify', views.send_notification, 
     name='send_notification'),
path('Attendance/edit', views.edit_attendance_page, 
     name='edit_attendance'),
path('Attendance/edit_table',views.edit_table , name='edit_table'),
path('Attendance/return_edit_table',views.return_edit_table , name='return_edit_table'),
]

