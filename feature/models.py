from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Ticket(models.Model):
    name = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.30)
    date_posted = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    voted = models.TextField()
    def __str__(self):
        return self.name

class TicketProgress(models.Model):
    ticket_prog = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    progress = models.IntegerField()
    def __str__(self):
        return self.ticket_prog.name