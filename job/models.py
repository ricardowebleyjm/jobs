from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=255,)
    job_description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    company = models.ForeignKey("Company", null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey("JobCategory", null=True, blank=True, on_delete=models.CASCADE)

class JobCategory(models.Model):
    category = models.CharField(max_length=255)

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    company_address = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=11)
    company_url = models.URLField()

