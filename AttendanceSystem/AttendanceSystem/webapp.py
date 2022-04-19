from django.shortcuts import render
from . import face_recognize_testing as ft

def button(request):

    return render(request,'AttendnanceTracker.html')

def output(request):
    
    output_data = ft.main()

    
    return render(request,"AttendnanceTracker.html",{"output_data":output_data})
    