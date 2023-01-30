from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, DaysForm
from .models import get_suppliers


# ChoiceField MultipleChoiceField TypedMultipleChoiceField

def index(request):
    return render(request, 'suppliers/index.html',
                  {'Title': 'Страница API'})


def suppliersView(request):
    form = DaysForm()
    suppliers = get_suppliers()
    print(form)
    if form.is_valid():
        print(form.cleaned_data)
        # subject = form.cleaned_data["subject"]
        # from_email = form.cleaned_data["from_email"]
        # message = form.cleaned_data['message']
        # try:
        #     send_mail(subject, message, from_email, ["admin@example.com"])
        # except BadHeaderError:
        #     return HttpResponse("Invalid header found.")
        # return redirect("success")
        pass  # TODO Create Logic
    return render(request, "suppliers/supplier_2.html", {"suppliers": suppliers})


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
        print(form)
    else:
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "suppliers/email.html", {"form": form})


def successView(request):
    return HttpResponse("Success! Thank you for your message.")
