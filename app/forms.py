from django import forms
from .models import Book
  
# creating a form
class GeeksForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    date_time = forms.DateTimeField()
    is_active = forms.BooleanField()
    price = forms.IntegerField()
    first_name = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number") 
    password = forms.CharField(widget = forms.PasswordInput()) 

class BookForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Book
        fields = "__all__"          # Specify here which fiels are you want.. If you want perticular 2 fields then write those fields names here.
        exclude = ("is_active",)    # write fields name those you dont want.


STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}))
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)