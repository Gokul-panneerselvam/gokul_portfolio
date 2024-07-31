from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length =100)
    about = models.TextField()
    father_name = models.CharField(max_length =100)
    dob = models.DateField(max_length =100)
    sex = models.CharField(max_length =100)
    state = models.CharField(max_length =100)
    physical_challenged = models.CharField(max_length =100)

class Education(models.Model):
    deg = models.CharField(max_length =20)
    percent= models.DecimalField( max_digits=4, decimal_places=2)
    institution = models.CharField(max_length=100)
    year=models.CharField(max_length=20)

class Resume(models.Model):
    resume_file = models.FileField(upload_to="resume/")

    def delete(self, *args, **kwargs):
        # Delete the file from the storage
        if self.resume_file and self.resume_file.name:
            storage = self.resume_file.storage
            if storage.exists(self.resume_file.name):
                storage.delete(self.resume_file.name)
        # Call the parent class's delete method
        super().delete(*args, **kwargs)

class Project(models.Model):
    name=models.CharField(max_length=100)
    discription=models.TextField()
    icon=models.ImageField(upload_to="project/")

class Skill(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="skills/")

class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    phone=models.IntegerField()
    message=models.TextField()

