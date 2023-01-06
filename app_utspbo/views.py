from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from app_utspbo.forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect("/index")
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    lagus = lagu.objects.all()
    petas = peta.objects.all()
    data = {
        'Title': "Halaman Utama",
        'Heading': "Peta Pendugaan klorofil-A di PPN Karangantu",
        'lagus' : lagus,
        'petas' : petas,
    }
    return render(request, 'index.html', data)

@login_required(login_url='login')
def about(request, id):
    aboutlagus = lagu.objects.get(pk=id)
    data = {
        'Title': "Halaman Detail Informasi",
        'Heading': "Menampilkan detail Informasi dari halaman 1",
        'lagus' : aboutlagus,
    }
    return render(request, 'about.html', data)

@login_required(login_url='login')
def index2(request):
    lagus = lagu.objects.all()
    data = {
        'Title': "Halaman Utama",
        'Heading': "CRUD Data Tangkapan Ikan",
        'lagus' : lagus,
    }
    return render(request, 'index2.html', data)

@login_required(login_url='login')
def crudpeta(request):
    petas = peta.objects.all()
    data = {
        'Title': "Halaman Utama",
        'Heading': "Peta Pendugaan klorofil-A di PPN Karangantu",
        'petas' : petas,
    }
    return render(request, 'crudpeta.html', data)


def tambah(request):
    if request.POST:
        form = Formlagu(request.POST)
        if form.is_valid():
            form.save()
            form = Formlagu()
            pesan = "Data Berhasil Ditambahkan!"
            data = {
                'Title': "Halaman Tambah Data",
                'Heading': "Menambahkan Data Tangkapan Ikan",
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambah.html', data)
    else:
        form = Formlagu()
        data = {
            'Title': "Halaman Tambah Data",
            'Heading': "Menambahkan Data Tangkapan Ikan",
            'form' : form,
        }
    return render(request, 'tambah.html', data)

def genre(request):
    genres = alattangkap.objects.all()
    data = {
        'Title': "Halaman Genre",
        'Heading': "Menampilkan Keterangan Alat Tangkap Ikan",
        'genres' : genres,
    }
    return render(request, 'genre.html', data)

def tambahpeta(request):
    if request.POST:
        form = Formpeta(request.POST)
        if form.is_valid():
            form.save()
            form = Formpeta()
            pesan = "Data Berhasil Ditambahkan!"
            data = {
                'Title': "Halaman Tambah Data",
                'Heading': "Menambahkan Data Peta",
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambahpeta.html', data)
    else:
        form = Formpeta()
        data = {
            'Title': "Halaman Tambah Data",
            'Heading': "Menambahkan Data Peta",
            'form' : form,
        }
    return render(request, 'tambahpeta.html', data)

def update(request, id):
    lagus = lagu.objects.get(id=id)
    template = 'update.html'
    
    if request.POST:
        form = Formlagu(request.POST, instance=lagus)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diubah!"
            data = {
            'Title': "Halaman Update",
            'Heading': "Mengubah Data Tangkapan Ikan dalam Database",
            'form' : form,
            'pesan' : pesan,
            'lagu' : lagus
            }
            return render(request, template, data)
    else:
        form = Formlagu(instance=lagus)
        data = {
            'Title': "Halaman Update",
            'Heading': "Mengubah Data Tangkapan Ikan dalam Database",
            'form' : form,
            'lagu' : lagus
        }
        return render(request, template, data)

def delete(request, id):
    lagus = lagu.objects.get(id=id)
    lagus.delete()
    
    return redirect("/index2")

def updatepeta(request, id):
    petas = peta.objects.get(id=id)
    template = 'updatepeta.html'
    
    if request.POST:
        form = Formpeta(request.POST, instance=petas)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diubah!"
            data = {
            'Title': "Halaman Update",
            'Heading': "Mengubah Data Peta",
            'form' : form,
            'pesan' : pesan,
            'peta' : petas
            }
            return render(request, template, data)
    else:
        form = Formpeta(instance=petas)
        data = {
            'Title': "Halaman Update",
            'Heading': "Mengubah Data Peta",
            'form' : form,
            'peta' : petas
        }
        return render(request, template, data)

def deletepeta(request, id):
    petas = peta.objects.get(id=id)
    petas.delete()
    
    return redirect("/crudpeta")

# Create your views here.
