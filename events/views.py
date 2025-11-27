from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Event, EventRegistration
from accounts.decorators import admin_required, student_required
from .forms import EventRegistrationForm


# Create your views here.
def home(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'index.html', {'events': events})

@admin_required
def admin_dashboard(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'admin_dashboard.html', {'events': events})


@admin_required
def add_event(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        venue = request.POST['venue']
        category = request.POST['category']
        poster = request.FILES.get('poster')

        Event.objects.create(
            title=title,
            description=description,
            date=date,
            venue=venue,
            category=category,
            poster=poster
        )
        messages.success(request, "Event added successfully!")
        return redirect('admin_dashboard')

    return render(request, 'add_event.html')


@admin_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        event.title = request.POST['title']
        event.description = request.POST['description']
        event.date = request.POST['date']
        event.venue = request.POST['venue']
        event.category = request.POST['category']
        if request.FILES.get('poster'):
            event.poster = request.FILES.get('poster')
        event.save()
        messages.success(request, "Event updated successfully!")
        return redirect('admin_dashboard')

    return render(request, 'edit_event.html', {'event': event})


@admin_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    messages.success(request, "Event deleted successfully!")
    return redirect('admin_dashboard')


#  STUDENT DASHBOARD
@student_required
def student_dashboard(request):
    my_registrations = EventRegistration.objects.filter(student=request.user)
    return render(request, 'student_dashboard.html', {'registrations': my_registrations})


@student_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    already_registered = EventRegistration.objects.filter(event=event, student=request.user).exists()

    if already_registered:
        messages.warning(request, "You have already registered for this event.")
    # else:
    #     EventRegistration.objects.create(event=event, student=request.user)
    #     messages.success(request, f"You registered for {event.title} successfully!")

        return redirect('student_dashboard')
    
    if request.method == "POST":
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.student = request.user
            registration.save()

            messages.success(request, f"You registered for {event.title} successfully!")
            return redirect('student_dashboard')
    else:
        form = EventRegistrationForm()

    return render(request, "event_register.html", {
        "event": event,
        "form": form
    })