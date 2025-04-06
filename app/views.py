from django.shortcuts import render,redirect,get_object_or_404
from.forms import *
from.models import *
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

def slotbookings(request, login_id):
    user = request.session.get('user_id') 
    login = get_object_or_404(Login, id=user)
    
    station = get_object_or_404(Station, login_id__id=login_id)  
    
    if request.method == 'POST':
        form = slotbook(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            
            existing_booking = slotbooking.objects.filter(
                login_id=station.login_id,
                date=date,
                time=time
            ).exists()  
            
            if existing_booking:
                form.add_error(None, "This slot is already booked by another user.")
            else:
                a = form.save(commit=False)
                a.user_id = login  
                a.login_id = station.login_id 
                a.save() 
                return redirect('payment',a.id)  
    else:
        form = slotbook()

    return render(request, 'slotbooking.html', {'form': form})


def slotbookingview(request):
    a=slotbooking.objects.all()
    return render(request,'userslotview.html',{'a':a})

def slotedit(request,id):
    user = request.session['user_id'] 
    login = get_object_or_404(Login, id=user)
    a=get_object_or_404(slotbooking,id=id)
    stationid=a.user_id.id
    station = get_object_or_404(Station, id=stationid)  
    if request.method == 'POST':
        form = slotbook(request.POST, instance=a)
        if form.is_valid():
            b = form.save(commit=False)
            b.user_id = station
            b.login_id = station.login_id 
            b.save() 
            return redirect('slotbookingview')  
    else:
         form = slotbook(instance=a)
    return render(request,'slotbooking.html', {'form': form})

def slot_cancel(request,id):
    a=get_object_or_404(slotbooking,id=id)
    a.cancel_status=1
    a.save()
    return redirect('slotbookingview')
def slot_delete(request,id):
    a=get_object_or_404(slotbooking,id=id)
    a.delete()
    return redirect('slotbookingview')


def slotstationview(request):
    station_id = request.session.get('station_id')
    station_login = Login.objects.get(id=station_id)
    booked_slots = slotbooking.objects.filter(login_id=station_login)
    slots_with_user_info = []
    for slot in booked_slots:
        user_info = User.objects.get(login_id=slot.user_id)
        slots_with_user_info.append({
            'date': slot.date,
            'time': slot.time,
            'user_name': user_info.name,
            'user_contact': user_info.contact,
            'cancel_status': slot.cancel_status
        })
    context = {
        'booked_slots': slots_with_user_info,
    }
    
    return render(request, 'slotstationview.html', context)

def feedbacks(request,id):
    if request.method == 'POST':
        form = feedbackform(request.POST)
        if form.is_valid():
            a=form.save(commit= False)
            user=get_object_or_404(Login,id=request.session['user_id'])
            stationlogin = get_object_or_404(Login,id = id)
            station = get_object_or_404(Station,login_id = stationlogin)
            a.login_id = user   
            a.station_id = station
            a.save()
            return redirect('stationsearch')
    else:
          form = feedbackform()
    return render(request,'feedback.html',{'form': form})
        

def view_feedback(request,id):
    a=get_object_or_404(Login,id=id)
    station=get_object_or_404(Station,login_id=a)
    form=feedback.objects.filter(station_id=station.id)
    return render(request,'view_feedback.html',{'form': form})

def user_feedback(request):
    # Retrieve the logged-in user's session ID
    user_id = request.session.get('user_id')
    a=get_object_or_404(Login,id=user_id)
    # Get the user's feedback entries
    feedback_entries = feedback.objects.filter(login_id=a)
    return render(request, 'user_feedback.html', {'feedback_entries': feedback_entries})

def edit_feedback(request,id):
    feedback_instance = get_object_or_404(feedback, id=id, login_id=request.session.get('user_id'))
    if request.method == 'POST':
        form = feedbackform(request.POST, instance=feedback_instance)
        if form.is_valid():   
            form.save()
            return redirect('user_feedback') 
    else:
        form = feedbackform(instance=feedback_instance)
    return render(request, 'edit_feedback.html', {'form': form})

def delete_feedback(request,id):
    a=get_object_or_404(feedback,id=id)
    a.delete()
    return redirect('user_feedback')

def complaint_add(request):
    userid=request.session.get('user_id')
    log=get_object_or_404(Login,id=userid)
    if request.method == 'POST':
        form = complaintform(request.POST)
        if form.is_valid():
            a=form.save(commit= False)
            a.user_logid=log
            a.save() 
            return redirect('userhome')
    else:
          form = complaintform()
    return render(request,'complaints.html',{'form': form})

def view_complaints(request):
    complaint = complaints.objects.all()  # Fetch all complaints
    return render(request, 'admin_complaints.html', {'complaints': complaint})

def user_viewcomplaints(request):
    complaint = complaints.objects.all()  # Fetch all complaints
    return render(request, 'user_complaintview.html', {'complaints': complaint})

def edit_complaint(request,id):
    cmt=get_object_or_404(complaints,id=id)
    if request.method == 'POST':
        form = complaintform(request.POST, instance=cmt)
        if form.is_valid():   
            form.save()
            return redirect('user_viewcomplaints') 
    else:
        form = complaintform(instance=cmt)
    return render(request, 'Edit_complaints.html', {'form': form})

def delete_complaint(request,id):
    cmt=get_object_or_404(complaints,id=id)
    cmt.delete()
    return redirect('user_viewcomplaints')

def complaint_reply(request,id):
    cmt=get_object_or_404(complaints,id=id)
    if request.method=='POST':
        form=replyform(request.POST)
        if form.is_valid():
            cmt.reply=form.cleaned_data['reply']
            cmt.save()
            return redirect('adminhome')
    else:
        form=replyform(initial={'reply':cmt.reply})
    return render(request,'admin_complaintreply.html',{'form':form,'cmt':cmt})
    

def payment(request,id):
    slotid=get_object_or_404(slotbooking,id=id)
    log=request.session.get('user_id')
    logid=get_object_or_404(User,login_id=log)
    if request.method=='POST':
        form=paymentform(request.POST)
        if form.is_valid():
            a = form.save(commit = false)
            a.login_id = logid
            a.bookingid = slotid
            a.save()
            return redirect('payment')
    else:
        form=paymentform()
    return render(request,'payments.html',{'form':form})
    








