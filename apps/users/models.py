from django.db.models import Model, ImageField, ForeignKey, CASCADE, CharField, TextField, URLField


class Project(Model):
    title = CharField(max_length=255)
    description = TextField()
    keyword = TextField()
    image = ImageField(upload_to='products/images/')
    image1 = ImageField(upload_to='products/images/')
    url = URLField()

    def __str__(self):
        return self.title
