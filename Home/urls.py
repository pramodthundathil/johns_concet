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
    path("Realestate_Renovation",views.Realestate_Renovation,name="Realestate_Renovation"),
    path("Blogs",views.Blogs,name="Blogs"),
    path("BlogSingle/<int:pk>",views.BlogSingle,name="BlogSingle"),
    path("Contact",views.Contact,name="Contact"),
    path("Gallery",views.Gallery,name="Gallery"),
    path("Projects_",views.Projects_,name="Projects_"),
    path("Careers",views.Careers,name="Careers"),
    path("Jobapplication/<int:pk>",views.Jobapplication, name="Jobapplication"),
    path("Projects_Apartments",views.Projects_Apartments, name="Projects_Apartments"),
    path("Projects_Residence",views.Projects_Residence, name="Projects_Residence"),
    path("Projects_Commercial",views.Projects_Commercial, name="Projects_Commercial"),
    path("Projects_Office",views.Projects_Office, name="Projects_Office"),
    path("Projects_Renovation",views.Projects_Renovation, name="Projects_Renovation"),

    path("ProjectSingle/<int:pk>",views.ProjectSingle,name="ProjectSingle"),
    path("Testimonial",views.Testimonial,name="Testimonial"),
    

    

    # admin urls
    path("SignIn",views.SignIn,name="Signin"),
    path("Adminstration",views.Adminstration,name="Adminstration"),
    path("HomePageEdits",views.HomePageEdits,name="HomePageEdits"),
    path('BlogeEdits', views.BlogeEdits, name='BlogeEdits'),
    path('GalleryEdits', views.GalleryEdits, name='GalleryEdits'),
    path('JobsEdits', views.JobsEdits, name='JobsEdits'),
    path('ProjectsEdits', views.ProjectsEdits, name='ProjectsEdits'),
    path('video_slide_create', views.video_slide_create, name='video_slide_create'),
    path('picture_slide_create', views.picture_slide_create, name='picture_slide_create'),
    path('job_create', views.job_create, name='job_create'),
    path('JobApplicationSingleView/<int:pk>', views.JobApplicationSingleView, name='JobApplicationSingleView'),
    path('delete_application/<int:pk>', views.delete_application, name='delete_application'),
    path('JobDelete/<int:pk>', views.JobDelete, name='JobDelete'),
    path('JobSingleView/<int:pk>', views.JobSingleView, name='JobSingleView'),
    path('create_project', views.create_project, name='create_project'),
    path("DeleteProject/<int:pk>",views.DeleteProject,name="DeleteProject"),
    path("ProjectSingleAdmin/<int:pk>",views.ProjectSingleAdmin,name="ProjectSingleAdmin"),
    path("AddPicturesToProject/<int:pk>",views.AddPicturesToProject,name="AddPicturesToProject"),
    path("PhotodeleteFromProject/<int:pk>",views.PhotodeleteFromProject,name="PhotodeleteFromProject"),
    path("DeleteGalleryImage/<int:pk>",views.DeleteGalleryImage,name="DeleteGalleryImage"),

    path("TestimonialAdmin",views.TestimonialAdmin,name="TestimonialAdmin"),
    path("DeleteTestimonial/<int:pk>",views.DeleteTestimonial,name="DeleteTestimonial"),
    path("BlogDelete/<int:pk>",views.BlogDelete,name="BlogDelete"),
    path("Enquiry",views.Enquiry,name="Enquiry"),
    path("DeleteEnquiry/<int:pk>",views.DeleteEnquiry,name="DeleteEnquiry"),



    

]