from django.db import models

# Create your models here.
# class Song(models.Model):
#     title= models.TextField()
#     artist= models.TextField()
#     # image= models.ImageField()
#     audio_file = models.FileField(blank=True,null=True)
#     duration=models.CharField(max_length=20)
#     paginate_by = 2

#     def __str__(self):
#         return self.title

# class Song(models.Model):
#     songName = models.CharField(max_length = 30)
#     artist = models.CharField('Artist', max_length=30)
#     album = models.CharField('Album', max_length=30)
#     audio_track = models.FileField(upload_to="song/")

#     def __unicode__(self):
#         return self.songName

# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='documents/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

# class Audio_store(models.Model):
#     record=models.FileField(upload_to='documents/')
#     class Meta:
#         db_table='Audio_store'