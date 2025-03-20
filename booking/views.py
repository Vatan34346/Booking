from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Booking
from .forms import BookingForm


@login_required
def booking_list(req):
    """Booking lisdt of users"""
    bookings = Booking.objects.filter(user=req.user).order_by('-date', 'time')
    return render(req, 'booking/booking_list.html', {'bookings': bookings})


@login_required
def create_booking(req):
    """Booking creation"""
    if req.method == "POST":
        form = BookingForm(req.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = req.user
            booking.save()
            messages.success(req, "Successfully booked!")
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(req, 'booking/booking_form.html', {'form': form})


@login_required
def update_booking(req, booking_id):
    """Updating booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=req.user)
    if req.method == "POST":
        form = BookingForm(req.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(req, "Booking  is successfully updated!")
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)

    return render(req, 'booking/booking_form.html', {'form': form, 'booking': booking})


@login_required
def delete_booking(req, booking_id):
    """Delete booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=req.user)
    if req.method == "POST":
        booking.delete()
        messages.success(req, "Booking deleted")
        return redirect('booking_list')

    return render(req, 'booking/booking_confirm_delete.html', {'booking': booking})


@login_required
def booking_events(req):
    """Api for uploading booking to calendar"""
    bookings = Booking.objects.all()
    events = []
    print(bookings)
    for booking in bookings:
        events.append({
            "title": f"Table {booking.table_number} (Guests: {booking.guests})",
            "start": f"{booking.date}T{booking.time}",
            "end": f"{booking.date}T{booking.time}",
            "url": f"/booking/{booking.id}/edit/",
        })

    return JsonResponse(events, safe=False)


@login_required
def calendar_view(req):
    """Calendar page"""
    return render(req, 'booking/calendar.html')
