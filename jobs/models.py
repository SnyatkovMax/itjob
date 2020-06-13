from django.db import models


class JobType(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)

    def __str__(self):
        return self.name


class Lang(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)

    def __str__(self):
        return self.name



class Job(models.Model):
    job_name = models.CharField(max_length=100, unique=False, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    company = models.CharField(max_length=100, unique=False, null=False)
    company_logo = models.FileField(null=True, upload_to='upload/')
    companyURL = models.URLField(null=True)
    companyEmail = models.EmailField(null=True)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False, default=500)
    description = models.TextField(null=False)

    def __str__(self):
        return f'{self.job_name} / {self.city} / {self.company} / {self.company_logo} / {self.companyURL} / ' \
               f'{self.companyEmail} / {self.lang} / {self.job_type} / {self.experience} / {self.salary} /' \
               f' {self.description}'
