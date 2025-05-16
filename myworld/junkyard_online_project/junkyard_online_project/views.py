from django.shortcuts import redirect

def to_main(request):
    return redirect('main/')