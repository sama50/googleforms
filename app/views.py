from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
from app.models import UserForms ,SubmissionForm , QueationForImage , Queation_Text_ans
import uuid
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request=request,username=username,password=password)
        print(user)
        if user is not None:
            login(request=request,user=user)
            return redirect('home')
        print(username+" "+password)

    return render(request,'login.html')

def home(request):

    form_all = UserForms.objects.all()

     
    return render(request,'home.html',{'form_all':form_all})

def add_form(request):
    if request.method == 'POST':
        uuid_id = uuid.uuid4()
        form_name = request.POST.get('form_name')
        data = UserForms(user=request.user,form_name=form_name,form_id=uuid_id)
        data.save()
        

        return redirect('/add-form/'+str(uuid_id))
    else:
        return redirect('./')
def add_form_id(request,id):
    user_obj = UserForms.objects.get(form_id=id)
    if request.method == 'POST':
        queation = request.POST.get('queation')
        
        SubmissionForm(formid=user_obj,quetion=queation).save()

        return redirect('./')
    all_qps = SubmissionForm.objects.filter(formid=user_obj)
    all_img_qps = QueationForImage.objects.filter(formid=user_obj)
    return render(request,'addform.html',{'all_qps':all_qps,'myid':id,'all_img_qps':all_img_qps})

def add_image_fields(request,id):
    user_obj = UserForms.objects.get(form_id=id)
    if request.method == 'POST':
        queation = request.POST.get('image_qps')
        
        QueationForImage(formid=user_obj,quetion=queation).save()

        return redirect('/add-form/'+id)
    return redirect('/add-form/'+id)

def share_form(request,id):
    user_obj = UserForms.objects.get(form_id=id)
    get_all_qps = SubmissionForm.objects.filter(formid=user_obj)
    print(get_all_qps[1])
    if request.method == 'POST':
        email = request.POST.get('email')
        print(request.POST)
        for i in range(0,len(get_all_qps)):
            qps_ans = request.POST.get(str(i))
            Queation_Text_ans(email=email,form_id=user_obj,que=get_all_qps[i],ans=qps_ans).save()
        return render(request,'success.html')
    return render(request,'shareform.html',{'get_all_qps':get_all_qps,'user_obj':user_obj})

 
def see_all_details(request,id):
    user_obj = UserForms.objects.get(form_id=id)
    que_ans_list = Queation_Text_ans.objects.filter(form_id=user_obj)
    return render(request,'seedetails.html',{'que_ans_list':que_ans_list})
def logout_user(request):
    logout(request)
    return redirect('login')