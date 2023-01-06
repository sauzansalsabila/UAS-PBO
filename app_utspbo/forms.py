from django.forms import ModelForm
from django import forms
from app_utspbo.models import *

class Formlagu(ModelForm):
    class Meta:
        model = lagu
        fields = '__all__'

        widgets = {
            'namakapten' : forms.TextInput({'class':'form-control', 'placeholder':'Nama Kapten', 'required':'required'}),
            'tanggalberangkat' : forms.TextInput({'class':'form-control', 'placeholder':'Tanggal Keberangkatan', 'required':'required'}),
            'jenisikan' : forms.TextInput({'class':'form-control', 'placeholder':'Jenis Ikan', 'required':'required'}),
            'alattangkap' : forms.Select({'class':'form-control', 'placeholder':'Alat Tangkap', 'required':'required'}),
            'jumlah' : forms.NumberInput({'class':'form-control', 'placeholder':'Jumlah Tangkapan Ikan', 'required':'required'}),
            'img' : forms.TextInput({'class':'form-control', 'placeholder':'Dokumentasi Perjalanan', 'required':'required'}),
        }

class Formpeta(ModelForm):
    class Meta:
        model = peta
        fields = '__all__'

        widgets = {
            'koordinat' : forms.TextInput({'class':'form-control', 'placeholder':'Koordinat', 'required':'required'}),
            'jumlah' : forms.TextInput({'class':'form-control', 'placeholder':'Jumlah Klorofil-A', 'required':'required'}),
            'deskripsi' : forms.TextInput({'class':'form-control', 'placeholder':'Status Kandungan Klorofil-A', 'required':'required'}),
        }