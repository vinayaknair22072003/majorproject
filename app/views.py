from django.shortcuts import render,redirect,get_object_or_404
from.forms import *
from.models import User,Login,Station
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index (request):
    data = Advertisement.objects.all()
   
    return render (request,'landing.html',{"data":data})

def userhome(request):
    return render(request,'userhome.html')

def adminhome(request):
    return render(request, 'adminhome.html')

def userreg(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        logform=LoginCheck(request.POST)
        if form.is_valid() and logform.is_valid():
            a=logform.save(commit=False)
            a.usertype='user'
            a.save()
            b=form.save(commit=False)
            b.login_id=a
            b.save()
            return redirect('login')
    else:
        form = UserForm()
        logform=LoginCheck()
    return render(request,'userform.html',{'form':form,'logform':logform})



def user_list_view(request):
    users = User.objects.all() 
    return render(request, 'usertable.html', {'users': users})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            try:
                user=Login.objects.get(email=email)
                if user.password==password:
                    if user.usertype=='user':
                        request.session['user_id']= user.id
                        return redirect('userhome')  
                    if user.usertype=='station':
                        request.session['station_id']=user.id
                        return redirect('chargestataionhome')             
                else:
                    messages.error(request,'Invalid password')
            except Login.DoesNotExist:
                messages.error(request,'user does not exist')
    else:
        form=LoginForm()


    return render(request, 'login.html', {'form': form})

def user_edit_view(request):
    id=request.session.get('user_id')
    users=get_object_or_404(User,login_id=id)
    email=get_object_or_404(Login,id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=users)
        logform=Logineditform(request.POST,instance=email)
        if form.is_valid() and logform.is_valid():
            form.save()
            logform.save()
            return redirect('userhome')  
    else:
         form = UserForm(instance=users)
         logform=Logineditform(instance=email)
    return render(request,'userprofile.html', {'form': form,'logform':logform})

def station_reg(request):
   
   
    if request.method == 'POST':
        form = StationForm(request.POST)
        logform=LoginCheck(request.POST)
        if form.is_valid() and logform.is_valid():
            a=logform.save()
            a.usertype='station'
            a.save()
            b=form.save(commit=False)
            b.login_id=a
            b.save()
            return redirect('login')
    else:
        form = StationForm()
        logform=LoginCheck()
    return render(request,'userform.html',{'form':form,'logform':logform})

def charging_station_admin_view(request):
    return render(request,'adminchargestationview.html')

def StationTable(request):
    forms=Station.objects.all()
    return render(request,'adminchargestationview.html',{'forms':forms})

def admuserview(request):
    forms=User.objects.all()
    return render(request,'adminuserview.html',{'forms':forms})

def stationsearch(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        stations = Station.objects.filter(
            Q(state__icontains=query) |
            Q(district__icontains=query) |
            Q(city__icontains=query) |
            Q(location__icontains=query)
        )
        
        # Check if no results were found
        if not stations:
            messages.error(request, 'No results found.')
        
        return render(request, 'userchargesearch.html', {'stations': stations})
    else:
        return render(request, 'userchargesearch.html')
    
def chargestationhome(request):
    s = request.session.get('station_id')
    data = get_object_or_404(Station,login_id=s)
    print(s)    
    a=Advertisement.objects.filter(station_id=data)
    print("data..",data)
    return render(request,'chargestationhome.html',{'a':a})

def stationprofile(request):
    id=request.session.get('station_id')
    users=get_object_or_404(Station,login_id=id)
    email=get_object_or_404(Login,id=id)
    if request.method == 'POST':
        form = StationForm(request.POST, instance=users)
        logform=Logineditform(request.POST,instance=email)
        if form.is_valid() and logform.is_valid():
            form.save()
            logform.save()
            return redirect('charginstationhome')  
    else:
         form = StationForm(instance=users)
         logform=Logineditform(instance=email)
    return render(request,'chargestationprofile.html', {'form': form,'logform':logform})

def advertisement(request):
    a=request.session.get('station_id')
    print("dataaa",a)
    b= get_object_or_404(Login,id=a)
    c=get_object_or_404(Station,login_id=b)
    print("dataaa....",c)
    if request.method == 'POST':
        form = AdvertisementForm(request.POST,request.FILES)
        if form.is_valid():
            d=form.save(commit=False)
            d.station_id=c
            d.save()
            return redirect('chargestataionhome')
    else:
        form = AdvertisementForm()
    return render(request,'advertisement.html',{'forms':form})

def advertisememnt_view_user(request):
    a=Advertisement.objects.all()
    return render(request,'advertisementviewtable.html',{'a':a})

def advertisememnt_view(request):
    a=Advertisement.objects.all()
    return render(request,'landing.html',{'a':a})

def adminstation_view(request):
    forms=Station.objects.all()
    return render(request,'adminstationview.html',{'forms':forms})

def advertisement_edit(request,id):
    a=get_object_or_404(Advertisement,id=id)

    if request.method == 'POST':
        form = AdvertisementForm(request.POST,request.FILES, instance=a)
        print("form",form)
        if form.is_valid():
            form.save()
            return redirect('advertisememnt_view_user')  
    else:
         form = AdvertisementForm(instance=a)
    return render(request,'advertisementremove.html', {'forms': form})

def advertisement_delete(request,id):
    a=get_object_or_404(Advertisement,id=id)
    a.delete()
    return redirect('advertisememnt_view_user')
























    