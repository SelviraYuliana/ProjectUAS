from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from yuliana.models import Produk
from .keranjang import Yulianacart
from .forms import YulianacartAddProductForm

@require_POST
def yulianacart_add(request, product_id):
    yulianacart = Yulianacart(request) # create a new cart object passing it the request object
    product = get_object_or_404(Produk, id=product_id)
    quantity = int(request.POST.get('quantity'))
    form = YulianacartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        yulianacart.add(product=product, quantity=quantity, update_quantity=cd['update'])
    return redirect('yulianacart_detail')

def yulianacart_remove(request, product_id):
    yulianacart = Yulianacart(request)
    product = get_object_or_404(Produk, id=product_id)
    yulianacart.remove(product)
    return redirect('yulianacart_detail')

def yulianacart_detail(request):
    yulianacart = Yulianacart(request)
    context = {
        'judul': 'Halaman Pemesanan Produk',
        'yulianacart':yulianacart
    }
    for item in yulianacart:
        item['update_quantity_form'] = YulianacartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'pemesanan.html',context)

   