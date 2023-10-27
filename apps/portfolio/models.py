from django.db.models import Model, CharField, TextField, ImageField, URLField


class Project(Model):
    title = CharField(max_length=255)
    description = TextField()
    keyword = TextField()
    image = ImageField(upload_to='images/', blank=True, null=True)
    url = URLField()

