from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def admin_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        return redirect('student_dashboard')
    return wrapper

def student_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.role == 'student':
            return view_func(request, *args, **kwargs)
        return redirect('admin_dashboard')
    return wrapper
