from contextlib import redirect_stderr
from datetime import date
from multiprocessing import context
from urllib import request
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
import qrcode
# Create your views here.
# def pageNotFound(request):
#     return HttpResponseBadRequest
# conn = psycopg2.connect(
#     host="ec2-54-158-26-89.compute-1.amazonaws.com",
#     database="dhn6cqjl2l3g8",
#     user="oopdmvwlwappje",
#     password="eaf0cb1a8feaaf7048812b3ad852d919dc293a51ea1c8d7c2bb4ddac4cfa07bf")
# cursor = conn.cursor()


def page1(request):
    pk = 12
    redirect_link=(f"http://127.0.0.1:8000/document/{pk}")
    qr_image = qrcode.make(redirect_link)
    qr_image.save("/Users/maagauiya/Documents/kzspace_back/kazspace/app1/static/app1/qr_codes/12.png")
    image_name = "12.png"
    image_path = f"/static/app1/qr_codes/{image_name}"
    context = { 
        "qr_image" : image_path
    } 
    return render(request, 'app1/lichnyi_kab.html',context=context)


def page2(request):
    return render(request, 'app1/login.html')


def page3(request):
    if request.POST.get('submit'):
        return redirect('five/')
    return render(request, 'app1/profile.html')


def page4(request):
    return render(request, 'app1/profile2.html')


def page5(request):
    # if request.POST.get("button_reg"):
    #     li = request.POST.getlist("data")
    #     cursor.execute("insert into mestomogily(iin, last_name, first_name, middle_name, date_of_birth, cause_of_death, kladbishe_name, vera, morg_number, year_death, spravka_o_smerti, id_mogily, lat_coord_mogila, lng_coord_mogila) values ('"+li[0] + "','" +
    #                    li[1] + "','" + li[2] + "','" + li[3] + "','" + li[4] + "','" + li[5] + "','" + li[6] + "','" + li[7] + "','" + li[8] + "','" + li[9] + "','" + li[10] + "','" + li[11] + "','" + li[12] + "','" + li[13] + "')")
    #     conn.commit()

    return render(request, 'app1/reg_usopshi.html')


def page6(request):
    return render(request, 'app1/vybor_kladbisha.html')

def document(request,pk):
    return render(request, 'app1/document.html')
