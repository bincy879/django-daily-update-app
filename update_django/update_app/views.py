from django.shortcuts import render,redirect
from update_app.models import update_db

# Create your views here.
def form_fn(request):
    return render(request,"update.html")

def save_data(request):
    if request.method=="POST":
        us=request.POST.get('user')
        da=request.POST.get('date')
        wf=request.POST.get('wfh')
        up=request.POST.get('update')
        co=request.POST.get('comment')
        im=request.FILES['img']
        obj=update_db(Name=us,Date=da,Workfh=wf,Updates=up,Comments=co,Images=im)
        obj.save()
        return redirect(form_fn)

def table_fn(request):
    data=update_db.objects.all()
    return render(request,"view-table.html",{'data':data})