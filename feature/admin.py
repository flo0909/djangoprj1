from django.contrib import admin
from .models import Ticket, TicketProgress

admin.site.register(Ticket)
admin.site.register(TicketProgress)
