from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class UserProfile(AbstractBaseUser):
	idUser = models.IntegerField(primary_key=True)
	userName = models.CharField(verbose_name='Usuario', unique=True, max_length=50)
	nombre = models.CharField(verbose_name='Nombre', max_length=80)
	apellidoP = models.CharField(verbose_name='ApellidoPaterno', max_length=80)
	apellidoM = models.CharField(verbose_name='ApellidoMaterno', max_length=80)
	pictureProfile = models.ImageField(verbose_name='PictureProfile', upload_to='imagesProfiles')

	is_active = models.BooleanField(default=True)

	USERNAME_FIELD = 'userName'
	REQUIRED_FIELDS = ['nombre', 'apellidoP']

	def __unicode__(self):
		return self.username

	def get_full_name(self):
		return self.nombre + " " + self.apellidoP + " " + self.apellidoM

	def get_short_name(self):
		return self.nombred