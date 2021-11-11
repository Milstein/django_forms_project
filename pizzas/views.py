from django.shortcuts import render, get_object_or_404

from .forms import PizzaForm, MultiplePizzaForm

from .models import Pizza

from django.forms import formset_factory


def home(request):
    return render(request, 'pizzas/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        # form = PizzaForm(request.POST, request.FILES)
        form = PizzaForm(request.POST)
        if form.is_valid():
            created_pizza = form.save()
            created_pizza_pk = created_pizza.id
            topping1 = form.cleaned_data['topping1']
            topping2 = form.cleaned_data['topping2']
            size = form.cleaned_data['size']
            note = 'Thanks for ordering! Your {0} and {1} {2} pizza is on its way.'.format(topping1, topping2, size)
            
            form = PizzaForm()

        else:
            created_pizza_pk = None
            note = 'Order was not created, please try again!'

        context = {
            'form': form,
            'note': note,
            'created_pizza_pk': created_pizza_pk,
            'multiple_form': multiple_form
        }
        
        return render(request, 'pizzas/order.html', context)
    
    else:
        form = PizzaForm()        
        context = {
            'form': form,
            'multiple_form': multiple_form
        }
        return render(request, 'pizzas/order.html', context)


def more_pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
            number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()    

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
            note = 'Pizza have been ordered!'
        else:
            note = 'Order was not created, please try again!'
        
        context ={
            'formset': formset,
            'note': note
        }

        return render(request, 'pizzas/pizzas.html', context)

    else:
        context ={
            'formset': formset
        }
        return render(request, 'pizzas/pizzas.html', context)


def edit_order(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Your order is been updated!'

            context = {
                'form': form,
                'pizza': pizza,
                'note': note
            }
            return render(request, 'pizzas/edit_order.html', context)
    
    context = {
            'form': form,
            'pizza': pizza
    }
    return render(request, 'pizzas/edit_order.html', context)
