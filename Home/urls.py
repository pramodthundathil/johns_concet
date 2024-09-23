from django.urls import path 
from .import views 

urlpatterns = [
   
    path("",views.Index,name="Index"),
    path("SignIn",views.SignIn,name="SignIn"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("AboutUs",views.AboutUs,name="AboutUs"),
    path("Service_Architecture",views.Service_Architecture,name="Service_Architecture"),
    path("Service_InteriorDesign",views.Service_InteriorDesign,name="Service_InteriorDesign"),
    path("Service_Civil_Construction",views.Service_Civil_Construction,name="Service_Civil_Construction"),
    path("Service_Renovation",views.Service_Renovation,name="Service_Renovation"),
    path("Blog",views.Blog,name="Blog"),
    path("Contact",views.Contact,name="Contact"),
    path("Gallery",views.Gallery,name="Gallery"),
    path("Projects",views.Projects,name="Projects")
]