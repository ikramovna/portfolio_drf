from django.db.models import Model, ImageField, ForeignKey, CASCADE, CharField, TextField, URLField, SlugField, \
    ManyToManyField
from django.utils.text import slugify


class Project(Model):
    title = CharField(max_length=255)
    description = TextField()
    keyword = TextField()
    image = ImageField(upload_to='products/images/', blank=True, null=True)
    url = URLField()
    slug = SlugField(max_length=255, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # if not self.slug:
        self.slug = slugify(self.title)
        while Project.objects.filter(slug=self.slug).exists():
            slug = Project.objects.filter(slug=self.slug).first().slug
            if '-' in slug:
                try:
                    if slug.split('-')[-1] in self.title:
                        self.slug += '-1'
                    else:
                        self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                except:
                    self.slug = slug + '-1'
            else:
                self.slug += '-1'

        super().save(force_insert, force_update, using, update_fields)

    # def __str__(self):
    #     return self.title
