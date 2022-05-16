from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name="Home"),
path('Attendance/view', views.view_attendance_page, 
     name='view_attendance'),
path('Attendance/edit', views.edit_attendance_page, 
     name='edit_attendance'),
path('Attendance/mark', views.mark_attendance_page, 
     name='mark_attendance'),
path('Attendance/marked', views.attendance_marked, 
     name='attendance_marked'),
path('Attendance/attendance_table', views.Table, 
     name='Table'),
]

