from django.db import models

# Create your models here.
class VideoSlide(models.Model):
    video = models.FileField(upload_to='slidevideo')
    caption = models.CharField(max_length=255)
    sub_headding = models.CharField(max_length=255)
    date_updated = models.DateField(auto_now_add=True)


class PictureSlids(models.Model):
    pictures = models.FileField(upload_to='picture')
    caption = models.CharField(max_length=255)
    sub_headding = models.CharField(max_length=255)
    date_updated = models.DateField(auto_now_add=True)

class Job(models.Model):
    title = models.CharField(max_length=255)  # Job Title
    experience = models.CharField(max_length=255)  # Minimum Experience in Years  
    education = models.CharField(max_length=255)  # Education Requirement
    description = models.TextField()  # Job Description
    salary = models.CharField(max_length=100)  # Salary Description
    location = models.CharField(max_length=255)  # Job Location
    posted_on = models.DateField(auto_now_add=True)  # Posting Date
    
    def __str__(self):
        return self.title



class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    education = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    address = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    portfolio = models.FileField(upload_to='portfolios/', blank=True, null=True)  # Portfolio is optional
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Projects(models.Model):
    project_title = models.CharField(max_length=255)
    project_subname = models.CharField(max_length=255)
    project_description = models.CharField(max_length=1000, null=True, blank=True)
    land_area = models.CharField(max_length=11)
    bulding_area = models.CharField(max_length=11)
    location = models.CharField(max_length=100)
    primary_image = models.FileField(upload_to="project_primary_image")
    plan_image_1 = models.FileField(upload_to='planimage')
    plan_image_2 = models.FileField(upload_to='planimage')
    project_category = models.CharField(max_length=255, choices=
                                        (("Apartments","Apartments"),("Residence","Residence"),("Commercial","Commercial"),("Office","Office"),("Renovation","Renovation"))
                                        )
    project_status = models.CharField(max_length=20, choices=(("On Going","On Going"),("Completed","Completed")))
    client  = models.CharField(max_length=50)
    is_featured_product = models.BooleanField(default=False)

    def __str__(self):
        return str(self.project_title)

class ProjectPictures(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    image = models.FileField(upload_to="project_images")
    title = models.CharField(max_length=20, null=True, blank=True)


class GalleryImages(models.Model):
    title = models.CharField(max_length=50)
    image = models.FileField(upload_to="galleryimages")
    category = models.CharField(max_length=20, choices=(("Architecture","Architecture"),("Interior","Interior"),("Ongoingworks","Ongoingworks"),("Other","Other")))
    date = models.DateField(auto_now_add=True)

class TestimonialVideos(models.Model):
    client = models.CharField(max_length=50)
    video = models.FileField(upload_to="testimonial_videos")
    category = models.CharField(max_length=20, choices=(("Architecture","Architecture"),("Interior","Interior"),("Ongoingworks","Ongoingworks"),("Other","Other")),default="Other")
    date = models.DateField(auto_now_add=True)


class Blog(models.Model):
    blogtitle = models.CharField(max_length=100)
    image = models.FileField(upload_to='BlogImage')
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)

class Enquirys(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)


