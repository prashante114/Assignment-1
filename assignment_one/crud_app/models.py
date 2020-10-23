from django.db import models

# Create your models here.

class SoftDelete(models.Model):
    class Meta:
        abstract = True

    deleted_on = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.deleted_on=timezone.now()
        self.save()



class RouterProperties(SoftDelete):
	sapid = models.CharField(max_length=18)
	hostname = models.CharField(max_length=14)
	loopback = models.CharField(max_length=20)
	macaddress = models.CharField(max_length=17)

	def __str__(self):
		"""String for representing the MyModelName object (in Admin site etc.)."""
		return self.sapid