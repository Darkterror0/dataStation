from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import finance

def index(request):
    qiye = finance.objects.filter(name='江苏三森食品有限公司')[0]
    for i in qiye:
        print(qiye[i])

    return render(request,'data_index.html')

# class financeListView(ListView):