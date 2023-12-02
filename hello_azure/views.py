from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import InputForm
from django.templatetags.static import static
import pickle
import os
from django.conf import settings
from  azure.storage.blob  import  BlobServiceClient, BlobClient, ContainerClient

def index(request):
    print('Request for index page received')
    context ={}
    context['form']= InputForm()
    return render(request, "hello_azure/index.html", context)

@csrf_exempt
def recommendations(request):

    def get_weights_blob(blob_name):
        connection_string = "DefaultEndpointsProtocol=https;AccountName=busadm742;AccountKey=c+P3idmYNO2f0qLHKzO6O4mTDOeztMCPOr2klmWkffQ+nSgP9CmF76uDG3LXxBup2f+F6pjZmMCv+AStxvGMFw==;EndpointSuffix=core.windows.net"
        blob_client = BlobClient.from_connection_string(connection_string, 'models', blob_name)
        downloader = blob_client.download_blob(0)

        # Load to pickle
        b = downloader.readall()
        weights = pickle.loads(b)

        return weights


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

    classes = {0: 'AAA', 1: 'BBB', 2: 'CCC', 3: 'DDD', 4: 'EEE', 5: 'FFF', 6: 'GGG'}
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

        model_avoid = get_weights_blob(blob_name = 'model_avoid.pkl')

        model_rec = get_weights_blob(blob_name = 'model_rec.pkl')

        test_arr = [[int(gender), int(region), int(education), int(imd), int(age), int(studied_credits), int(disability)]]

        recommended_class = model_rec.predict(test_arr)[0]
        avoid_class = model_avoid.predict(test_arr)[0]

        rec = classes[recommended_class]
        avo = classes[avoid_class]

        if rec == avo:
            avo = '--'

        print(rec)
        print(avo)
        
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
            'credits_enc': studied_credits,
            'rec': rec,
            'avo': avo}
        return render(request, 'hello_azure/recommendations.html', context)
    else:
        return redirect('index')

 