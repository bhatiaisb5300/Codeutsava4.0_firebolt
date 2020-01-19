from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.urls import reverse
from .models import User,farmerPost,Warehouse,contact
from .forms import SignUpForm,SellerForm
from django.contrib.auth import authenticate,login,logout

# from django.contrib.auth import set_password
# Create your views here.
# @csrf_exempt
# def signup(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = SignUpForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             user = User()
#             user.first_name = form.cleaned_data['first_name']
#             user.last_name  = form.cleaned_data['last_name']
#             user.username   = form.cleaned_data['username']
#             user.email      = form.cleaned_data['email']
#             user.password1  = form.cleaned_data['password1']
#             user.phone = form.cleaned_data['phone']
#             # user.password2  = form.cleaned_data['password2']
#             completed = request.POST.get('cat')
#             if completed == 'True':
#                 user.user_type = 'True'
#                 user.save()
#                 pk = user.pk
#                 return HttpResponseRedirect(reverse('seller', kwargs={'pk':pk}))
#             else:
#                 user.save()
#                 return HttpResponseRedirect('/')
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = SignUpForm()
#
#     return render(request, 'signup.html', {'form': form})
def signup(request):
    if request.method=='POST':
        if request.POST['name'] and request.POST['email'] and request.POST['phone'] and request.POST['password'] and request.POST['register'] and request.POST['first'] and request.POST['last']:
            user_obj = User()
            user_obj.first_name = request.POST['first']
            user_obj.last_name = request.POST['last']
            user_obj.email = request.POST['email']
            user_obj.username = request.POST['name']
            user_obj.phone = request.POST['phone']
            user_obj.user_type = request.POST['register']
            # user = user_obj.save()
            user_obj.set_password(request.POST['password'])
            user_obj.save()
            if user_obj.user_type=='True':
                return redirect('accounts:farmerform')
            else:
                return redirect('accounts:index')
    else:
        return render(request,'signup.html')

def farmerform(request):
    if request.method=='POST':
        if request.POST['crop'] and request.POST['user'] and request.POST['address'] and request.POST['state'] and request.POST['reg_no'] and request.POST['land_area'] and request.POST['warehouse']:
            user_obj = Farmer()
            user_obj.crop = request.POST['crop']
            user_obj.user = request.POST['user']
            user_obj.address = request.POST['address']
            user_obj.state = request.POST['state']
            user_obj.reg_no = request.POST['reg_no']
            user_obj.land_area = request.POST['land_area']
            user_obj.warehouse = request.POST['warehouse']
            # user = user_obj.save()
            user_obj.save()
            return redirect('accounts:index')

    else:
        return render(request,'farmerform.html')

def detail_view(request,pk):
    var = farmerPost.objects.get(pk=pk)
    return render(request,'detail_view.html',context={'var':var})

def postform(request):
    if request.method=='POST':
        if request.FILES['images'] and request.POST['desc'] and request.POST['warehouse'] and request.POST['crop'] and request.POST['qty'] and request.POST['price_kg'] and request.POST['extra']:
            user_obj = farmerPost()
            user_obj.images = request.FILES['images']
            user_obj.desc = request.POST['desc']
            user_obj.warehouse = request.POST['warehouse']
            user_obj.crop = request.POST['crop']
            user_obj.qty = request.POST['qty']
            user_obj.price_kg = request.POST['price_kg']
            user_obj.extra = request.POST['extra']
            # user = user_obj.save()
            if request.POST['warehouse'] != '':
                if user_obj.qty <= user_obj.warehouse.avaiable:
                    user_obj.warehouse.avaiable -= user_obj.qty
                    user_obj.warehouse.avaiable.save()
                    print(user_obj.warehouse.avaiable)
                else:
                    return HttpResponse('space not available')
            user_obj.save()
            return redirect('accounts:farmerform')

    else:
        return render(request,'farmerform.html')

# def callback(request):


def get_seller(request,pk):
    user = User.objects.get(pk = pk)
    form = SellerForm()
    if user.user_type == 'True':
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = SellerForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                user.sell = form.cleaned_data['sell']
                user.save(commit=False)
                # pk = user.pk
                return HttpResponseRedirect('/')
        # if a GET (or any other method) we'll create a blank form
        else:
            form = form


    return render(request, 'seller.html',{'form':form})

def index(request):
    farmerpost = farmerPost.objects.all()
    return render(request,'index.html',context={'var':farmerpost})

def login_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            # return redirect('index')
            return redirect('accounts:index')
        else:
            return render(request,'about.html')
    else:
        return render(request,'login.html')
def about(request):
    return render(request,'about.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:index')

@csrf_exempt
def contacts(request):
    if request.method=='POST':
        obj = contact()
        obj.name = request.POST.get('name')
        obj.phone = request.POST.get('telephone')
        obj.email = request.POST.get('email')
        obj.subject = request.POST.get('subject')
        obj.message = request.POST.get('message')
        obj.save()
        return redirect('accounts:index')

    else:
        return render(request,'contact.html')

def details(request):
    return render(request,'cropfilter.html')

# def buy_crop(request,pk):
#     user = Warehoouse.objects.get(pk = pk)
#     user.available = user.avaiable +
