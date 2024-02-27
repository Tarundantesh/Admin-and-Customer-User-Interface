from django.shortcuts import render
from Account.models import AccountHolder
from Account.forms import AccountForm
# Create your views here.
def f1(request):
    form=AccountForm
    acc={"form":form}
    if request.method=='POST':
        form=AccountForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'sample.html',acc)
