from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import InputForm

def index(request):
    print('Request for index page received')
    context ={}
    context['form']= InputForm()
    return render(request, "hello_azure/index.html", context)

@csrf_exempt
def hello(request):
    gen_map = {0: 'F', 1: 'M'}
    region_map = {5: 'North Western Region',
        0: 'East Anglian Region',
        8: 'South Region',
        11: 'West Midlands Region',
        7: 'South East Region',
        9: 'South West Region',
        4: 'North Region',
        1: 'East Midlands Region',
        3: 'London Region',
        12: 'Yorkshire Region',
        10: 'Wales',
        6: 'Scotland',
        2: 'Ireland'}
    ed_map = {0: 'A Level or Equivalent',
        2: 'Lower Than A Level',
        1: 'HE Qualification',
        4: 'Post Graduate Qualification',
        3: 'No Formal quals'}
    imd_map = {3: '30-40%',
        7: '70-80%',
        1: '10-20',
        8: '80-90%',
        5: '50-60%',
        2: '20-30%',
        9: '90-100%',
        6: '60-70%',
        4: '40-50%',
        0: '0-10%'}
    age_map = {1: '35-55', 0: '0-35', 2: '55<='}
    dis_map = {1: True, 0: False}
    if request.method == 'POST':
        gender = request.POST.get('gender')
        gender_enc = gen_map[int(gender)]

        region = request.POST.get('region')
        region_enc = region_map[int(region)]

        education = request.POST.get('education')
        education_enc = ed_map[int(education)]

        age = request.POST.get('age')
        age_enc = age_map[int(age)]

        disability = request.POST.get('disability')
        disability_enc = dis_map[int(disability)] 

        imd = request.POST.get('imd')
        imd_enc = imd_map[int(imd)]

        studied_credits = request.POST.get('studied_credits')


        
        context = {'gender': gender,
            'gender_enc': gender_enc,
            'region': region,
            'region_enc': region_enc,
            'education': education,
            'education_enc': education_enc,
            'age': age,
            'age_enc': age_enc,
            'disability': disability,
            'disability_enc': disability_enc,
            'imd': imd,
            'imd_enc': imd_enc,
            'studied_credits': studied_credits,
            'credits_enc': studied_credits}
        return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')

 