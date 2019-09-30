from django.shortcuts import render, redirect, reverse
from .models import Ticket, TicketProgress
from .forms import TicketForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth , messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

@login_required
def ticketlist(request):
    
    ticket_obj = Ticket.objects.order_by('-date_posted')
    paginator = Paginator(ticket_obj, 3)
    page = request.GET.get('page')
    ticket = paginator.get_page(page)
    form = TicketForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        form = TicketForm()
    return render(request, 'feature/ticketlist.html', {'ticket':ticket, 'form':form})

@login_required
def ticketdetail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    try:
        ticketprogress = TicketProgress.objects.get(ticket_prog=ticket_id)

    except ObjectDoesNotExist:
        ticketprogress = 0
        ticket = get_object_or_404(Ticket, pk=ticket_id)

    return render(request, 'feature/ticketdetail.html', dict(ticket=ticket, ticketprogress=ticketprogress))


@login_required
def ticketdelete(request, ticket_id):
    form = Ticket.objects.filter(pk=ticket_id)
    if request.method == 'POST':
        form.delete()
    return redirect(reverse('app1:ticketlist'))


@login_required
def ticketupdate(request, ticket_id):

    ticket = Ticket.objects.get(pk=ticket_id)
    if request.POST:
        form = TicketForm(request.POST)

    if form.is_valid():
        ticket = Ticket.objects.get(pk=ticket_id)
        form = TicketForm(request.POST, instance = ticket)
        form.save()
        return redirect(reverse('app1:ticketlist')) 
    else:      
        u_form = {"name": ticket.name, "content":ticket.content} 
        form = TicketForm(initial=u_form)
        
    return render(request, 'app1/update.html',{'form':form})

@login_required
def ticketresult(request, ticket_id):
    mylist = ''
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        User.objects.filter(username=request.user)
        value = int(request.POST['value']) 
        ticket.votes += value

        if request.user.username in ticket.voted:
            messages.warning(request, "You already voted for this post!")
            return redirect(reverse('app1:ticketlist'))

        elif not request.user.username in ticket.voted:        
            mylist = ' ' + str(request.user.username) + ' ' 
            savedVoted = ticket.voted
            ticket.voted  = mylist + savedVoted
            ticket.save()
    return redirect(reverse('app1:ticketdetail', args=(ticket.id,)))