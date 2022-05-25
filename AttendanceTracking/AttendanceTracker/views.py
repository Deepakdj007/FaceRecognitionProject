from django.shortcuts import render
from django.shortcuts import HttpResponse
from matplotlib.style import context
import pandas as pd
from . import view_attendance, face_rec_take_attendance, smtp_email, low_attendance_list, whatsapp, edit_attendance
from django.contrib.auth.decorators import login_required
import json
from django.template.loader import render_to_string

def home(request):
    return render(request,'home.html',{})
@login_required
def view_table(request):
    
    if request.method == "GET":
        class_date = request.GET.get('class_date')
        class_name = request.GET.get('class')
    df = view_attendance.view_att(class_date, class_name)
    json_records2 = df.reset_index().to_json(orient ='records')
    data2 = []
    data2 = json.loads(json_records2)
    context2 = {'d2': data2}  
    return render(request, 'view_table.html',context2)

@login_required
def view_attendance_page(request):
    return render(request, 'view_attendance.html',{})
@login_required
def edit_attendance_page(request):
    return render(request, 'edit_attendance.html',{})
@login_required
def mark_attendance_page(request):
    
    return render(request, 'mark_attendance.html',{})
@login_required    
def attendance_marked(request):
    
    if request.method == "GET":
        class_name = request.GET['class']
        period = request.GET['hour']
        face_rec_take_attendance.main(class_name, int(period))
        
    return render(request, 'attendance_marked.html',{})

@login_required
def send_notification(request):
    if request.method == "POST":
        class_name = request.POST['class']
        request.session['Class_name'] = class_name
        
    a,b,df2 = low_attendance_list.low_attendance(class_name)
    json_records = df2.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}  
    return render(request, 'send_notification.html',context)

@login_required
def notified(request):
    if request.method == 'POST' and 'run_mail' in request.POST:
        smtp_email.notify_people(request.session.get('Class_name'))
    if request.method == 'POST' and 'run_whatsapp' in request.POST:
        whatsapp.whatsapp_message(request.session.get('Class_name'))
    
    return render(request, 'notified.html',{})
    
@login_required
def notification(request):
        return render(request, 'notification.html')

@login_required 
def edit_table(request):
    if request.method == "GET":
        class_date = request.GET.get('class_date')
        class_name = request.GET.get('class')
    df = edit_attendance.view_today_att(class_date, class_name)
    json_records3 = df.reset_index().to_json(orient ='records')
    data3 = []
    data3 = json.loads(json_records3)
    context3 = {'d3': data3}  
    return render(request, 'edit_table.html',context3)

@login_required 
def return_edit_table(request):
    if request.method == 'POST':
        data = request.POST.getlist('data1[]')
        edit_attendance.update_table(data)
        return HttpResponse("Success!") # Sending an success response

    

    
    