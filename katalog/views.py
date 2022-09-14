from django.shortcuts import render
from katalog.models import CatalogItem

# Create your views here.
def show_katalog(request):
    return render(request, "katalog.html", context)

data_katalog_barang = CatalogItem.objects.all()
context = {
    'list_katalog_barang': data_katalog_barang,
    'nama': 'Ravena Meilani',
    'NPM' : '2106631923'
}