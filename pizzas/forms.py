from django import forms

from .models import Pizza, Size

# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100, widget=forms.PasswordInput)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)

    # TOPPING_OPTIONS =[
    #     ('pep', 'Pepporoni'),
    #     ('cheese', 'Cheese'),
    #     ('olives', 'Olives')
    # ]

    # toppings = forms.MultipleChoiceField(choices=TOPPING_OPTIONS, widget=forms.CheckboxSelectMultiple)

    # CHOICES = [
    #     ('Small', 'Small'),
    #     ('Medium', 'Medium'),
    #     ('Large', 'Large')
    # ]
    # size = forms.ChoiceField(label='Size', choices=CHOICES)


class PizzaForm(forms.ModelForm):

    # widgets options:
    # RadioSelect, Textarea, CheckboxSelectMultiple, PasswordInput
    
    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)
    
    # image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(PizzaForm, self).__init__(*args, **kwargs)

        # change a widget attribute:
        self.fields['topping1'].widget.attrs["class"] = 'form-control'
        self.fields['topping2'].widget.attrs["class"] = 'form-control'
        self.fields['size'].widget.attrs["class"] = 'form-control'

    class Meta:
        model = Pizza
        fields = ("topping1", "topping2", "size",)
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2', 'size': 'Size',}
        # widgets ={
        #     'topping1': forms.Textarea
        #     # ,
        #     # 'size': forms.CheckboxSelectMultiple
        # }


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
