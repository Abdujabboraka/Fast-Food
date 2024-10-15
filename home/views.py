from django.shortcuts import render, redirect
from .models import Order, Menu
from .forms import OrderForm
# Create your views here.
def homepage(request):
    orders = Order.objects.all()
    menus = Menu.objects.all()
    context = {'orders': orders, 'menus': menus}
    return render(request, 'home.html', context)




def order(request):
    if request.method == 'POST':
        o_status = 'Edit Order'
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                customer_name=form.cleaned_data['customer_name'],
                customer_phone=form.cleaned_data['customer_phone']
            )
            order.items.set(form.cleaned_data['items'])
            order.save()
            return redirect('success')

    else:
        o_status = 'Place New Order'
        form = OrderForm()
    context = {
        'form': form,
        'status' : o_status
    }
    return render(request, 'order.html', context)


def success(request):

    return render(request, 'success.html')