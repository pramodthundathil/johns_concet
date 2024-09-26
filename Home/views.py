from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *



def Index(request):
    video = VideoSlide.objects.all().order_by('-id')[:2]
    pictures = PictureSlids.objects.all()[:2]
    projects = Projects.objects.filter(is_featured_product = True)[:5]
    context = {
       "video":video,
       "pictures":pictures,
       "projects":projects
    }
    return render(request,"index.html",context)

def AboutUs(request):
    return render(request,'aboutus.html')

def Testimonial(request):
    testimonial = TestimonialVideos.objects.all().order_by("-id")
    return render(request,"testimonial.html",{"testimonial":testimonial})

def Service_Architecture(request):
    return render(request,"archituture_service.html")

def Service_InteriorDesign(request):
    return render(request,"interior_design_service.html") 

def Service_Civil_Construction(request):
    return render(request,"civil_contstruction_service.html") 

def Service_Renovation(request):
    return render(request,"renovation_service.html") 

def Realestate_Renovation(request):
    return render(request,"realestate_service.html") 

def Blogs(request):
    blogs = Blog.objects.all().order_by("-id")

    context = {
       "blogs":blogs 
    }
    return render(request,"blog.html",context) 

def BlogSingle(request,pk):
    blog = Blog.objects.get(id = pk)
    return render(request,"blogsingle.html",{"blog":blog})

def Contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        enquiry = Enquirys(
            name= name,
            phone = phone,
            subject = subject,
            message = message
        )
        enquiry.save()
        messages.info(request,"Enquiry Sent to Johns Concept... ")
        return redirect("Contact")
    return render(request,"contact.html")

def Gallery(request):
    architecture = GalleryImages.objects.filter(category = "Architecture").order_by("-id")
    interior = GalleryImages.objects.filter(category = "Interior").order_by("-id")
    ongoingworks = GalleryImages.objects.filter(category = "Ongoingworks").order_by("-id")
    other = GalleryImages.objects.filter(category = "Other").order_by("-id")

    context ={
       "architecture":architecture,
       "interior":interior,
       "ongoingworks":ongoingworks,
       "other":other
    }
    return render(request,"gallery.html",context)

def Projects_(request):
    return render(request,"projects.html")


def Projects_Apartments(request):
    title = "Apartments"
    projects_completed = Projects.objects.filter(project_category = "Apartments", project_status = "Completed").order_by("-id")
    projects_ongoing = Projects.objects.filter(project_category = "Apartments", project_status = "On Going").order_by("-id")
    

    context = {
        "title":title,
        "projects_completed":projects_completed,
        "projects_ongoing":projects_ongoing
       
    }
    return render(request,"projects.html",context)

def Projects_Residence(request):
    title = "Residence"
    projects_completed = Projects.objects.filter(project_category = "Residence", project_status = "Completed").order_by("-id")
    projects_ongoing = Projects.objects.filter(project_category = "Residence", project_status = "On Going").order_by("-id")
    

    context = {
        "title":title,
        "projects_completed":projects_completed,
        "projects_ongoing":projects_ongoing
       
    }
    return render(request,"projects.html",context)


def Projects_Commercial(request):
    title = "Commercial"
    projects_completed = Projects.objects.filter(project_category = "Commercial", project_status = "Completed").order_by("-id")
    projects_ongoing = Projects.objects.filter(project_category = "Commercial", project_status = "On Going").order_by("-id")
    

    context = {
        "title":title,
        "projects_completed":projects_completed,
        "projects_ongoing":projects_ongoing

       
    }
    return render(request,"projects.html",context)


def Projects_Office(request):
    title = "Office"
    projects_completed = Projects.objects.filter(project_category = "Office", project_status = "Completed").order_by("-id")
    projects_ongoing = Projects.objects.filter(project_category = "Office", project_status = "On Going").order_by("-id")
    

    context = {
        "title":title,
        "projects_completed":projects_completed,
        "projects_ongoing":projects_ongoing

       
    }
    return render(request,"projects.html",context)

def Projects_Renovation(request):
    title = "Renovation"
    projects_completed = Projects.objects.filter(project_category = "Renovation", project_status = "Completed").order_by("-id")
    projects_ongoing = Projects.objects.filter(project_category = "Renovation", project_status = "On Going").order_by("-id")
    

    context = {
        "title":title,
        "projects_completed":projects_completed,
        "projects_ongoing":projects_ongoing

       
    }
    return render(request,"projects.html",context)


def ProjectSingle(request,pk):
    project = Projects.objects.get(id = pk)
    pictures = ProjectPictures.objects.filter(project = project)

    context = {
        "project":project,
        "pictures":pictures
    }
    return render(request,"projectsingle.html",context)

def Careers(request):
    careers = Job.objects.all()

    context = {
        "careers":careers
    }
    return render(request,"careers.html",context)

def Jobapplication(request,pk):
    item = Job.objects.get(id = pk)
    if request.method == 'POST':
        # Collecting form data
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pnum = request.POST.get('pnum')
        email = request.POST.get('email')
        education = request.POST.get('edu')
        experience = request.POST.get('experiance')
        address = request.POST.get('address')
        
        # Handling file uploads
        resume = request.FILES.get('resume')
        portfolio = request.FILES.get('folio')

        # Saving data to the model
        application = JobApplication(
            job = item,
            first_name=fname,
            last_name=lname,
            phone_number=pnum,
            email=email,
            education=education,
            experience=experience,
            address=address,
            resume=resume,
            portfolio=portfolio
        )
        application.save()

        messages.success(request, "Application submitted successfully!")
        return redirect('Careers')
    context = {
        "item":item
    }
    return render(request,'jobapplication.html',context)






# AdminPannel Functions start __________________++++++++++++++++++++++++++++++++


def SignIn(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pswd = request.POST['pswd']
    
        user = authenticate(request,username = uname, password = pswd)
        if user is not None:
            user = login(request,user)
            return redirect('Adminstration')
        else:
            messages.error(request,"username or password in correct")
            return redirect("SignIn")
        
    else:
        return render(request,"dashboard/login.html")
    
def SignOut(request):
    logout(request)
    return redirect("Index")

def Adminstration(request):
    return render(request,"dashboard/index.html")


# --------------------------------------------------------------------------------------
# Home Page edits 
# --------------------------------------------------------------------------------------
def HomePageEdits(request):
    videoslids = VideoSlide.objects.all()
    pictureslids = PictureSlids.objects.all()
    print(videoslids)

    context = {
        "videoslids":videoslids,
        "pictureslids":pictureslids
    }
    return render(request,"dashboard/homepageedits.html",context)


def video_slide_create(request):
    if request.method == 'POST':
        video = request.FILES.get('video')
        caption = request.POST.get('caption')
        sub_headding = request.POST.get('sub_headding')
        
        # Creating and saving the VideoSlide instance
        video_slide = VideoSlide(
            video=video,
            caption=caption,
            sub_headding=sub_headding
        )
        video_slide.save()

        # Adding success message
        messages.success(request, "Video Slide created successfully!")
        return redirect('HomePageEdits')  # Replace with your redirect URL

    return redirect('HomePageEdits') 

def picture_slide_create(request):
    if request.method == 'POST':
        pic = request.FILES.get('pic')
        caption = request.POST.get('caption')
        sub_headding = request.POST.get('sub_headding')
        
        # Creating and saving the VideoSlide instance
        pic_slide = PictureSlids(
            pictures=pic,
            caption=caption,
            sub_headding=sub_headding
        )
        pic_slide.save()

        # Adding success message
        messages.success(request, "Picture Slide created successfully!")
        return redirect('HomePageEdits')  # Replace with your redirect URL

    return redirect('HomePageEdits')


def DeleteVideoCarousal(request, pk):
    video = VideoSlide.objects.get(id = pk)
    video.video.delete()
    video.delete()
    messages.success(request, "Video Slide Delete successfully!")
    return redirect('HomePageEdits')

def DeletepictureCarousal(request, pk):
    Pic = PictureSlids.objects.get(id = pk)
    Pic.pictures.delete()
    Pic.delete()
    messages.success(request, "Video Slide Delete successfully!")
    return redirect('HomePageEdits')

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------


def BlogeEdits(request):
    blogs = Blog.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")
        description = request.POST.get("description")

        blog = Blog(
            blogtitle = title,
            image = image,
            description = description
        )
        blog.save()
        messages.success(request, "Blog created successfully!")
        return redirect("BlogeEdits")
    context = {
        "blogs":blogs
    }
    return render(request,"dashboard/blog.html",context)

def BlogDelete(request,pk):
    blog = Blog.objects.get(id = pk)
    blog.image.delete()
    blog.delete()
    messages.success(request, "Blog created successfully!")
    return redirect("BlogeEdits")


# --------------------------------------------------------------------------------------
# Gallery edits 
# --------------------------------------------------------------------------------------

def GalleryEdits(request):
    pictures = GalleryImages.objects.all()
    if request.method == "POST":
        image = request.FILES.get('image')
        title = request.POST.get('title')
        category = request.POST.get("gallery_category")

        images = GalleryImages(
            image = image,
            title = title,
            category = category
        )
        images.save()
        messages.info(request,'Gallery Image Saved ')
        return redirect('GalleryEdits')
    context = {
        "pictures":pictures
    }
    return render(request,"dashboard/gallery.html",context)

def DeleteGalleryImage(request,pk):
    image = GalleryImages.objects.get(id = pk)
    image.image.delete()
    image.delete()
    messages.info(request,'Image deleted......')
    return redirect("GalleryEdits")

# --------------------------------------------------------------------------------------
# Job edits 
# --------------------------------------------------------------------------------------

def JobsEdits(request):
    jobs = Job.objects.all()
    applications = JobApplication.objects.all()
    context = {
       "jobs":jobs ,
       "applications":applications
    }
    return render(request,"dashboard/jobs.html",context)


def job_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        experience = request.POST.get('experience')
        education = request.POST.get('education')
        description = request.POST.get('description')
        salary = request.POST.get('salary')
        location = request.POST.get('location')
    
        
        # Create and save the Job instance
        job = Job(
            title=title,
            experience=experience,
            education=education,
            description=description,
            salary=salary,
            location=location,
           
        )
        job.save()

        # Add success message
        messages.success(request, "Job posted successfully!")
        return redirect('JobsEdits')  # Replace with your redirect URL

    return redirect('JobsEdits')

def JobDelete(request,pk):
    Job.objects.get(id = pk).delete()
    messages.info(request, "Job Deleted successfully!")
    return redirect("JobsEdits")

def JobSingleView(request,pk):
    job = get_object_or_404(Job, id=pk)
    
    if request.method == "POST":
        # Get the form data
        title = request.POST.get('title')
        education = request.POST.get('education')
        experience = request.POST.get('experiance')  # Ensure consistent spelling
        description = request.POST.get('descrition')  # Consistent name with form typo
        salary = request.POST.get('salary')
        location = request.POST.get('location')
        
        # Update the job instance with new values
        job.title = title
        job.education = education
        job.experience = experience
        job.description = description
        job.salary = salary
        job.location = location
        
        # Save the updated job
        job.save()

        # Add success message
        messages.success(request, "Job updated successfully!")
        
        # Redirect to the same page or any other page
        return redirect('JobSingleView', pk=pk) 
    context = {"job":job}
    return render(request,"dashboard/jobsingleview.html",context)



def JobApplicationSingleView(request,pk):
    jobapplication = JobApplication.objects.get(id = pk)

    context = {
        "jobapplication":jobapplication
    }
    return render(request,"dashboard/applicationsingleview.html",context)


def delete_application(request,pk):
    Jobapplications = JobApplication.objects.get(id = pk)
    Jobapplications.resume.delete()
    Jobapplications.portfolio.delete()
    Jobapplications.delete()
    messages.info(request,"Job Application deleted success.....")
    return redirect("JobsEdits")

# --------------------------------------------------------------------------------------
# Projects 
# --------------------------------------------------------------------------------------

def ProjectsEdits(request):
    projects = Projects.objects.all()

    context = {
        "projects":projects
    }
    return render(request,"dashboard/projects.html",context)



def create_project(request):
    if request.method == 'POST':
        project_title = request.POST.get('project_title')
        project_subname = request.POST.get('project_subname')
        project_description = request.POST.get('project_description')
        land_area = request.POST.get('land_area')
        bulding_area = request.POST.get('bulding_area')
        location = request.POST.get('location')
        project_category = request.POST.get('project_category')
        project_status = request.POST.get('project_status')
        is_featured_product = bool(request.POST.get('is_featured_product'))
        client = request.POST.get('client')

        primary_image = request.FILES.get('primary_image')
        plan_image_1 = request.FILES.get('plan_image_1')
        plan_image_2 = request.FILES.get('plan_image_2')

        # Save project to the database
        new_project = Projects.objects.create(
            project_title = project_title,
            project_subname=project_subname,
            project_description=project_description,
            land_area=land_area,
            bulding_area=bulding_area,
            location=location,
            project_category=project_category,
            project_status=project_status,
            is_featured_product=is_featured_product,
            client = client,
            primary_image=primary_image,
            plan_image_1=plan_image_1,
            plan_image_2=plan_image_2,
        )
        new_project.save()
        messages.info(request,"Product added success.....")
        # Redirect to a success page or project list after saving
        return redirect('ProjectsEdits')  # Update the URL accordingly

    return redirect( 'ProjectsEdits')

def AddPicturesToProject(request,pk):
    project = Projects.objects.get(id = pk)
    if request.method == "POST":
        image = request.FILES.get('image')
        caption = request.POST.get('caption')

        images = ProjectPictures(
            project = project,
            image = image,
            title = caption
        )
        images.save()
        messages.info(request,"Pictures add to Project")
        return redirect("ProjectSingleAdmin",pk = pk)
    return redirect("ProjectSingleAdmin",pk = pk)

def ProjectSingleAdmin(request,pk):
    # project  = Projects.objects.get(id = pk)
    project = get_object_or_404(Projects, id=pk)
    pictures = ProjectPictures.objects.filter(project = project)

    if request.method == 'POST':
        project.project_title = request.POST.get('project_title')
        project.project_subname = request.POST.get('project_subname')
        project.project_description = request.POST.get('project_description')
        project.land_area = request.POST.get('land_area')
        project.bulding_area = request.POST.get('bulding_area')
        project.location = request.POST.get('location')
        project.project_category = request.POST.get('project_category')
        project.project_status = request.POST.get('project_status')
        project.is_featured_product = bool(request.POST.get('is_featured_product'))

        if 'primary_image' in request.FILES:
            project.primary_image = request.FILES['primary_image']
        if 'plan_image_1' in request.FILES:
            project.plan_image_1 = request.FILES['plan_image_1']
        if 'plan_image_2' in request.FILES:
            project.plan_image_2 = request.FILES['plan_image_2']

        project.save()

        messages.success(request, 'Project updated successfully!')
        return redirect('ProjectSingleAdmin', pk=pk)

    context = {
        "project":project,
        "pictures":pictures
    }
    return render(request,'dashboard/projectsingle.html',context)


def DeleteProject(request,pk):
    pro = Projects.objects.get(id = pk)
    pro.primary_image.delete()
    pro.plan_image_1.delete()
    pro.plan_image_2.delete()
    pro.delete()
    messages.info(request,"Product Deleted success.....")
        # Redirect to a success page or project list after saving
    return redirect('ProjectsEdits')

def PhotodeleteFromProject(request,pk):
    photo = ProjectPictures.objects.get(id = pk)
    project_pk = photo.project.id
    photo.image.delete()
    photo.delete()
    messages.info(request,"Photo Deleted success.....")
    return redirect("ProjectSingleAdmin",pk = project_pk)


# --------------------------------------------------------------------------------------
# Testimonial edits 
# --------------------------------------------------------------------------------------
def TestimonialAdmin(request):
    testimonial = TestimonialVideos.objects.all()
    if request.method =="POST":
        video = request.FILES.get("video")
        client = request.POST.get("client")
        testi = TestimonialVideos(
            video = video,
            client = client
        )
        testi.save()
        messages.info(request,"Testimonial addedeted success.....")
        return redirect("TestimonialAdmin")

    context = {
        "testimonial":testimonial
    }
    return render(request,"dashboard/testimonial.html",context)

def DeleteTestimonial(request,pk):
    testimonial = TestimonialVideos.objects.get(id = pk)
    testimonial.video.delete()
    testimonial.delete()
    messages.info(request,"Testimonial Deleted success.....")
    return redirect("TestimonialAdmin")
    

def Enquiry(request):
    enquiry = Enquirys.objects.all()

    return render(request,"dashboard/enquiry.html",{"enquiry":enquiry})

def DeleteEnquiry(request,pk):
    Enquirys.objects.get(id = pk).delete()
    messages.info(request,"Enquiry Deleted success.....")
    return redirect("Enquiry")








