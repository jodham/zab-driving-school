from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_roles=None):
    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('you are not authorised to view this page')

        return wrapper_func

    return decorator


def admin_only(view_func):
    def wrapper_func(self, request, *args, **kwargs):
        group = None
        if self.request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('home')
        if group == 'admin':
            return self.view_func(request, *args, **kwargs)
    return wrapper_func
