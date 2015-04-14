from django.db import models
from django.contrib.auth.models import User, Group
#from django_resized import ResizedImageField
#from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='perfil_usuario')
	cedula_profesional = models.CharField(max_length=50, blank=True)
	foto_perfil = models.ImageField(upload_to='userprofiles/imagesProfiles', verbose_name='FotoPerfil', blank=True)
	#foto_perfil = ResizedImageField(max_width=500, max_height=500, upload_to='userprofiles/imagesProfiles', verbose_name='FotoPerfil')
	#pictureProfile = models.ImageField(verbose_name='PictureProfile', upload_to='imagesProfiles', blank=True)
	def __unicode__(self):
		return self.user.username