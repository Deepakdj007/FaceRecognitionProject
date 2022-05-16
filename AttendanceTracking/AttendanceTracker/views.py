from django.shortcuts import render
from django.shortcuts import HttpResponse
import pandas as pd
from . import view_attendance, face_rec_take_attendance

def home(request):
    return render(request,'home.html',{})

def Table(request):
    
    if request.method == "GET":
        class_date = request.GET.get('class_date')
        class_name = request.GET.get('class')
    df = view_attendance.view_att(class_date, class_name)
    attendance_table = df.to_html(classes='table table-stripped')
  
    return HttpResponse(attendance_table)

def view_attendance_page(request):
    return render(request, 'view_attendance.html',{})

def edit_attendance_page(request):
    return render(request, 'edit_attendance.html',{})

def mark_attendance_page(request):
    
    return render(request, 'mark_attendance.html',{})
    
def attendance_marked(request):
    
    if request.method == "GET":
        class_name = request.GET['class']
        period = request.GET['hour']
        face_rec_take_attendance.main(class_name, int(period))
        
    return render(request, 'attendance_marked.html',{})