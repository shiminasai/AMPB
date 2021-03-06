from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField
from sorl.thumbnail import ImageField
from solo.models import SingletonModel
from django.template.defaultfilters import slugify

# Create your models here.
class Introduccion(SingletonModel):
	titulo = models.CharField(max_length = 250)
	subtitulo = models.CharField(max_length = 250)
	texto = models.TextField()
	imagen = ImageField(upload_to='intro/',null=True,blank=True)
	video = EmbedVideoField(null=True,blank=True)

	def __str__(self):
		return "Introducción"

	class Meta:
		verbose_name = "Introducción"

class QuienesSomos(models.Model):
	titulo = models.CharField(max_length = 250)
	texto = RichTextUploadingField()
	slug = models.SlugField(max_length=250,editable=False)
	orden = models.IntegerField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		return super(QuienesSomos, self).save(*args, **kwargs)

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name_plural = "Quienes Somos"
