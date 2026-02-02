from django.urls import path
from bun_core.views import test, create_,MainView,AboutView,ProductView,NewsView,DeleteProductView,UpdateProductView

urlpatterns = [
    path("",MainView.as_view()  ,name="home"),
    # important urls
    path("news/", NewsView.as_view(), name="news"),
    path("about/",AboutView.as_view(),name="about"),
    path("test/",test,name="test"),

    # delete and update urls
    path("create/",create_, name="create"),
    path('delete/<slug:slug>/',DeleteProductView.as_view(),name="delete"),
    path('update/<slug:slug>/',UpdateProductView.as_view(),name='update'),
    # decaratiive urls
    # path("news/<slug:slug>/",NewsView.as_view(), name="news_slug"),
    path("news/<slug:category_slug>/<slug:product_slug>",ProductView.as_view(), name="product_slug"),
]

