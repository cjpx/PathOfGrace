from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class Section(models.Model):
    TYPE_CHOICES = [
        ('verse', 'Verse'),
        ('chorus', 'Chorus')
    ]

    song = models.ForeignKey(Song, related_name='sections', on_delete=models.CASCADE)
    section_type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.section_type} - {self.song.title}"
    

class Line(models.Model):
    section = models.ForeignKey(Section, related_name='lines', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content