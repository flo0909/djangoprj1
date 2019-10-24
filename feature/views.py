from django.shortcuts import render, redirect, reverse
from .models import Ticket, TicketProgress
from cart.models import Order
from .forms import TicketForm
from app1.models import Answer
from app1.forms import AnswerForm
from accounts.models import UserProfile
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth , messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator


@login_required
def ticketlist(request):
    order = Order.objects.filter(user=request.user).first()
    profile = UserProfile.objects.all()
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
    return render(request, 'feature/ticketlist.html', {'ticket':ticket, 'form':form, 'profile':profile, 'order':order})

@login_required
def ticketdetail(request, ticket_id):
    answer = 'There is no answer yet'
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    
    try:
        profile = get_object_or_404(UserProfile, user=ticket.author)
    except ObjectDoesNotExist:
        pass
    try:
        ticketprogress = TicketProgress.objects.get(ticket_prog=ticket_id)
        if ticketprogress.progress == 100:
            ticket.done = True
            ticket.save()
        else:
            ticket.done = False

    except ObjectDoesNotExist:
        ticketprogress = 0
        ticket = get_object_or_404(Ticket, pk=ticket_id)
    try:
        answer = Answer.objects.get(name=ticket.name)
    except ObjectDoesNotExist:
        pass

    return render(request, 'feature/ticketdetail.html', dict(ticket=ticket, ticketprogress=ticketprogress, answer=answer, profile=profile))


@login_required
def ticketdelete(request, ticket_id):
    form = Ticket.objects.filter(pk=ticket_id)
    if request.method == 'POST':
        form.delete()
    return redirect(reverse('feature:ticketlist'))


@login_required
def ticketupdate(request, ticket_id):

    ticket = Ticket.objects.get(pk=ticket_id)
    if request.POST:
        form = TicketForm(request.POST)

    if form.is_valid():
        ticket = Ticket.objects.get(pk=ticket_id)
        form = TicketForm(request.POST, instance = ticket)
        form.save()
        return redirect(reverse('feature:ticketlist')) 
    else:      
        u_form = {"name": ticket.name, "content":ticket.content} 
        form = TicketForm(initial=u_form)
        
    return render(request, 'feature/ticketupdate.html',{'form':form})

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
            return redirect(reverse('feature:ticketlist'))

        elif not request.user.username in ticket.voted:        
            mylist = ' ' + str(request.user.username) + ' ' 
            savedVoted = ticket.voted
            ticket.voted  = mylist + savedVoted
            ticket.save()
    return redirect(reverse('feature:ticketdetail', args=(ticket.id,)))

def ticketanswer(request, ticket_id):
    answer = []
    form = AnswerForm(request.POST)
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    try:
        answer = Answer.objects.get(name=ticket.name)
    except ObjectDoesNotExist:
        form = AnswerForm(request.POST)
        if request.method == 'POST':
            answer = Answer.objects.create(name=ticket.name, content=request.POST['content'])
            return redirect(reverse('feature:ticketlist'))
    return render(request, 'feature/ticketanswer.html', {'form':form, 'answer':answer, 'ticket':ticket})

def ticketdone(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
     
    return render(request, 'feature/ticketdone.html', {'ticket': ticket})