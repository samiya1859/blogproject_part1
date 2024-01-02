
from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_category(request):
    if request.method=='POST': #user post request koreche
        category_form = forms.CategoryForm(request.POST) #user er post request data ekhane capture korlam
        if category_form.is_valid(): #post kora data gulo amra check korbo valid kina
            category_form.save() #jodi data valid hoy tahole database e save korbo
            return redirect ('add_category') #shob thik thakle add author e url pathay dibo
    else: #user normallly blank form dekhte pabe
        category_form=forms.CategoryForm()

    return render(request,'add_category.html',{'form':category_form})