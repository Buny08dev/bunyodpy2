from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
from django.http import HttpResponse
from django.views.generic import FormView,ListView,View,DetailView,TemplateView
from django.core.paginator import Paginator

from bun_core.forms import AddProduct
from bun_core.models import bunbase,Categories,Products
# bunbase.objects.values("id", "title")

# bunbase.objects.values_list("title", flat=True) only one o`zgaruvchi

# bunbase.objects.count()

# bunbase.objects.bulk_create([
#     bunbase(title="A"),
#     bunbase(title="B"),
# ])  ishlatarman!!



# Create your views here.
class MainView(View):
    def get(self,request):
        return render(request, 'home.html', {"title":"hello world"})

class NewsView(ListView):
    model=Products
    context_object_name="products_"
    template_name="news.html"
    paginate_by=4
    

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset,"\n",self.kwargs,"\n")
        slug=self.kwargs.get("slug")
        if slug:
            queryset=queryset.filter(category__slug=slug)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categories.objects.all()
        print("asdasdadsasddasdadassadasdadasd")
        context["products"]=context['page_obj']
        return context

class ProductView(DetailView):
    model=Products
    context_object_name="product"
    template_name="product_view.html" 
    slug_field="slug"
    slug_url_kwarg="product_slug"

    def get_queryset(self):
        return Products.objects.filter(category__slug=self.kwargs['category_slug'])

class AboutView(TemplateView):
    template_name="about.html"

# TESTing
def test(request):
    print(request.GET.get("name"))
    print(request.GET.get("year"))
    print(request.GET)
    # pagenation=Paginator(get_list_or_404(Products),2)
    # page_product=pagenation.page(page)
    return render(request,"test.html")

def create_(request):
    if request.method=="POST":
        form=AddProduct(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("news")
    form=AddProduct()
    return render(request, "main.html",{"agree":"yes","form":form})

def update_(request,id):
    if request.method=="POST":
        obj=bunbase.objects.get(id=id)

        obj.title = request.POST.get("title")
        obj.description = request.POST.get("description")
        obj.is_active = request.POST.get("is_active")

        if "image" in request.FILES:
            obj.image = request.FILES.get("image")

        obj.save()
        return redirect("news")
    return render(request, "main.html",{"agree":"yes"})

def delete_(request,id):
    Products.objects.get(id=id).delete()
    return redirect("news")


# Created your views here.

# def product_view(request,category_slug,product_slug):
#     prod=Products.objects.filter(category__slug=category_slug,slug=product_slug)
#     return render(request,"product_view.html",{"products":prod})

# def news(request,slug=None):
#     prod=Products.objects.all()
#     cat=Categories.objects.all()
#     if slug:
#         prod=Products.objects.filter(category__slug=slug)
#     return render(request, "news.html",{"products":prod,"categories":cat})