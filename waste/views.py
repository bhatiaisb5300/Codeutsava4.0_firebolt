from django.shortcuts import render,redirect
from .models import ngo_list,Post
# Create your views here.
def index(request):
    return render(request,'waste_index.html')

def detail_view(request,pk):
    obj = Post.objects.get(pk=pk)
    return render(request,'detail_view.html',context={'details':obj})

def create_post(request):
    if request.method=='POST':
        if request.POST['waste_type'] and request.FILES['images'] and request.POST['amount']:
            obj = Post()
            obj.images = request.FILES['images']
            obj.waste_type = request.POST['waste_type']
            obj.amount = request.POST['amount']
            obj.save()
            return redirect('accounts:index')
    else:
        return render(request,'create_waste_post.html')
