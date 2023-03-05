from django import forms

from mainsite.suppliers.models import MAX_LENGTH


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class DaysForm(forms.Form):
    INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 32)]
    todays_date = forms.CharField(max_length=MAX_LENGTH,
                                  widget=forms.Select(choices=INTEGER_CHOICES))
    # selected_date =
