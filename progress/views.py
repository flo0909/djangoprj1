from django.shortcuts import render, redirect, reverse
from feature.models import Ticket, TicketProgress
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404



def progress(request, ticket_id ):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket_done = Ticket.objects.all().filter(done='True')
    ticket_done_count = Ticket.objects.all().filter(done='True').count()
    try:
        ticketprog = TicketProgress.objects.get(ticket_prog=ticket)
        

    except ObjectDoesNotExist:
        return redirect(reverse('feature:ticketlist'))
    try:

        ticketSample1 = TicketProgress.objects.all().filter(progress__lte='99')[0]
        ticketSample2 = TicketProgress.objects.all().filter(progress__lte='99')[1]
        
   
    except:
        pass

    return render(request, 'progress/progress.html', dict(
        ticket=ticket,
        ticket_done_count=ticket_done_count,
        ticket_done=ticket_done,
        ticketprog=ticketprog,
        ticketSample1=ticketSample1,
        ticketSample2=ticketSample2
        ))