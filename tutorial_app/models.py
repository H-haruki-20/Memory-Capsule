from django.db import models

# Create your models here.


CATEGORY = (("hobby","趣味"),("study","勉強"),("other","その他"))
class BlogModel(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=30,
        choices=CATEGORY
    )
    def __str__(self) -> str:
        return self.title