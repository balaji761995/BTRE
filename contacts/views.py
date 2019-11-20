from django.shortcuts import render, redirect
import pdb;
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
# Create your views here.

def contact(request):
    if request.method == 'POST':
        # pdb.set_trace()


        listing = request.POST['listing']
        # pdb.set_trace()
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id, listing_id=listing_id)
            if has_contacted:
                messages.error(request, 'you have already made an enquiry to this property')
                return redirect('/listings/'+listing_id)


        contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        send_mail(
            'Property Listing Inquiry',
            'There has been Inquiry for' + listing + ', Sign in to the admin portal for more info',
            'balaji761995@gmail.com',
            [realtor_email,'nbalaji765@gmail.com']
        )
        messages.success(request, 'you request has been submited, a realtor will get back to you')
        # pdb.set_trace()
        return redirect('/listings/'+listing_id)
