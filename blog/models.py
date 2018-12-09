from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=50, null=True, blank=True)
    category_color = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:25]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %d %Y')



