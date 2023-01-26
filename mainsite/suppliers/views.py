from django.template.defaulttags import ForNode
from django.views import generic
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Supplier, get_suppliers
from .forms import ContactForm, DaysForm


# class SuppliersView(generic.ListView):
#     template_name = 'suppliers/supplier.html'
#     context_object_name = 'suppliers_list'
#
#     def get_queryset(self):
#         """
#         Return all Suppliers with is_outdated=False
#         """
#         return Supplier.objects.filter(is_outdated=False)

# def get_supplier_parameters(self, supplier: Supplier):
#     """
#     Return all SupplierParameters with is_outdated=False
#     """
#     return SupplierParameter.objects.filter(
#         supplier=supplier,
#         is_outdated=False,
#     )
# ChoiceField MultipleChoiceField TypedMultipleChoiceField

def suppliersView(request):
    form = DaysForm()
    suppliers = get_suppliers()
    if form.is_valid():
        # subject = form.cleaned_data["subject"]
        # from_email = form.cleaned_data["from_email"]
        # message = form.cleaned_data['message']
        # try:
        #     send_mail(subject, message, from_email, ["admin@example.com"])
        # except BadHeaderError:
        #     return HttpResponse("Invalid header found.")
        # return redirect("success")
        pass  # TODO Create Logic
    return render(request, "supplier_2.html", {"suppliers": suppliers})


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
    return render(request, "email.html", {"form": form})


def successView(request):
    return HttpResponse("Success! Thank you for your message.")
