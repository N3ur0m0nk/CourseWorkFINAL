from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import *
from .forms import *
from .Filler import *


# Create your views here.

def index(request, id):
    ls = Form1.objects.get(name=id)
    keyword_dict['${Date}'] = ls.Date.strftime('%d.%m.%Y')
    keyword_dict['${FullFIO}'] = ls.FullFIO
    keyword_dict['${FIO}'] = ls.FIO
    keyword_dict['${Specialty}'] = ls.Specialty
    keyword_dict['${FullKafedra}'] = ls.FullKafedra
    keyword_dict['${Kafedra}'] = ls.Kafedra
    keyword_dict['${Birthday}'] = ls.Birthday.strftime('%d.%m.%Y')
    keyword_dict['${Passport_Number}'] = ls.Passport_Number
    keyword_dict['${Passport_Vidacha}'] = ls.Passport_Vidacha
    keyword_dict['${Passport_Date}'] = ls.Passport_Date.strftime('%d.%m.%Y')
    keyword_dict['${Registration_Address}'] = ls.Registration_Address
    replace_keywords_in_docx(input_file, keyword_dict, output_file)

    return render(request, "main/index.html", {"ls": ls})


def get_name(request):
    if request.method == "POST":
        form = Dogovor(request.POST)

        if form.is_valid():
            a = form.cleaned_data["name"]
            b = form.cleaned_data["FullFIO"]
            c = FIOSplit(b)
            d = form.cleaned_data["Specialty"]
            e = form.cleaned_data["FullKafedra"]
            f = form.cleaned_data["Kafedra"]
            g = form.cleaned_data["Birthday"]
            h = form.cleaned_data["Passport_Number"]
            i = form.cleaned_data["Passport_Vidacha"]
            j = form.cleaned_data["Passport_Date"]
            k = form.cleaned_data["Registration_Address"]
            l = datetime.date.today()
            t = Form1(name=a, Date=l, FullFIO=b, FIO=c, Specialty=d, FullKafedra=e, Kafedra=f, Birthday=g, Passport_Number=h, Passport_Vidacha=i, Passport_Date=j, Registration_Address=k)
            t.save()

            return HttpResponseRedirect("/%s" % t.name)

    else:
        form = Dogovor()

    return render(request, "main/create.html", {"form": form})


def home(request):
    return render(request, "main/home.html", {})


def view(request):
    l = Form.objects.all()
    return render(request, "main/view.html", {"lists": l})
