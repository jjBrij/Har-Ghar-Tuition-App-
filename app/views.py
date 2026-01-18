from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import Teacher, TutorApplication, Payment
from .forms import TutorApplicationForm, PaymentForm
from django.core.files.storage import default_storage, FileSystemStorage
from decimal import Decimal
import razorpay
import os
import json
from django.views.decorators.csrf import csrf_exempt

def HomeView(request):
    if request.method == 'POST':
        # Extract data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        class_of_study = request.POST.get('class_of_study')
        subjects = request.POST.getlist('subjects')  # Get multiple subjects as a list
        subjects_str = ', '.join(subjects)  # Convert list to a comma-separated string
        num_children = request.POST.get('num_children')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')

        # Save to the database
        try:
            TutorApplication.objects.create(
                name=name,
                email=email,
                class_of_study=class_of_study,
                subjects=subjects_str,  # Save as comma-separated string
                num_children=num_children,
                contact_number=contact_number,
                address=address,
            )
        except Exception as e:
            return render(request, "index.html", {
                'teachers': Teacher.objects.all(),
                'error': f"An error occurred while saving the data: {e}"
            })

        # Send email notification
        subject = f"New Tutor Application from {name}"
        message = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Class of Study: {class_of_study}\n"
            f"Subjects: {subjects_str}\n"
            f"Number of Children: {num_children}\n"
            f"Contact Number: {contact_number}\n"
            f"Address: {address}\n"
        )
        sender_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['hargharpathshala03@gmail.com']

        try:
            send_mail(subject, message, sender_email, recipient_list, fail_silently=False)
        except Exception as e:
            return render(request, "index.html", {
                'teachers': Teacher.objects.all(),
                'error': f"An error occurred while sending the email: {e}"
            })

 
        return redirect('home')


    teachers = Teacher.objects.all()
    return render(request, "index.html", {'teachers': teachers})


def success_page(request):
    return HttpResponse("<h1>Thank you for your submission! An email has been sent to you.</h1>")
from django.shortcuts import render, get_object_or_404
from .models import Student

def search_student(request):
    query = request.GET.get('q', '')
    student = None
    results = None

    if query:
        try:
            student = Student.objects.get(roll_no__iexact=query)
        except Student.DoesNotExist:
            student = Student.objects.filter(student_name__icontains=query).first()

        if student:
            results = student.subjects.all()

    return render(request, 'search_student.html', {
        'query': query,
        'student': student,
        'results': results,
    })



# Initialize Razorpay client with your API Key and Secret
client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

def payment_view(request):
    form = PaymentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        student_id = form.cleaned_data['student_id']
        try:
            # Ensure the amount is an integer in INR
            amount = int(form.cleaned_data['amount'])  # Amount entered by user (in INR)
        except ValueError:
            # Handle the case where the user inputs a non-integer value
            # For example, you can return an error message or handle it gracefully
            return render(request, 'payment/payment_page.html', {
                'form': form,
                'error_message': 'Please enter a valid integer amount in INR.',
            })

        # Convert to paise (100 paise = 1 INR)
        amount_in_paise = amount * 100

        # Create order in Razorpay
        order = client.order.create({
            'amount': amount_in_paise,  # Amount in paise
            'currency': 'INR',
            'payment_capture': '1',  # Auto-capture the payment once successful
        })

        # Store order and user details in session
        request.session['order_id'] = order['id']
        request.session['name'] = name
        request.session['student_id'] = student_id
        request.session['amount'] = amount_in_paise

        # Convert amount to display (INR) for frontend
        display_amount = amount  # As the amount is in INR, no need to convert again

        # Return the payment page with Razorpay order and payment details
        return render(request, 'payment/payment_page.html', {
            'form': form,
            'order': order,
            'name': name,
            'student_id': student_id,
            'amount': amount,  # In INR (integer)
            'display_amount': display_amount,  # For displaying INR amount
        })

    return render(request, 'payment/payment_page.html', {'form': form})


from .models import Payment

client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))


import hmac
import hashlib

@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        payment_data = json.loads(request.body)

        payment_id = payment_data.get('razorpay_payment_id')
        order_id = payment_data.get('razorpay_order_id')
        signature = payment_data.get('razorpay_signature')

        try:
            # Verify Razorpay signature
            params_dict = {
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            client.utility.verify_payment_signature(params_dict)

            # Retrieve session data
            name = request.session.get('name')
            student_id = request.session.get('student_id')
            amount = request.session.get('amount')

            if not (name and student_id and amount):
                return JsonResponse({'status': 'Missing session data. Payment not recorded.'}, status=400)

            # Save payment to the database
            payment = Payment.objects.create(
                name=name,
                student_id=student_id,
                amount=amount / 100,  # Convert from paise to INR
                transaction_id=payment_id
            )

            return JsonResponse({'status': 'Payment verified successfully.'})

        except razorpay.errors.SignatureVerificationError:

            return JsonResponse({'status': 'Payment verification successfully.'}, status=400)

    return JsonResponse({'status': 'Invalid request method.'}, status=405) 
def payment_success(request):
    return render(request, 'payment/payment_success.html')



def tutor_application(request):
    if request.method == 'POST':
        form = TutorApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            subject_expertise = form.cleaned_data['subject_expertise']
            experience = form.cleaned_data['experience']
            availability = form.cleaned_data['availability']
            reason_to_join = form.cleaned_data['reason_to_join']
            
            # Handle file (PDF) upload
            resume_file = form.cleaned_data['resume']

            # Use FileSystemStorage for custom directory
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'resumes'))
            
            # Save the uploaded file
            if resume_file:
                resume_path = fs.save(resume_file.name, resume_file)
                resume_url = fs.url(resume_path)  # Optional if you need a URL reference
                
                # Reset the file pointer to the beginning
                resume_file.seek(0)

            # Create the email
            subject = f"New Tutor Application from {full_name}"
            message = f"""
            Name: {full_name}
            Email: {email}
            Phone: {phone_number}
            Subject Expertise: {subject_expertise}
            Experience: {experience}
            Availability: {availability}
            Reason to Join: {reason_to_join}
            """
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['hargharpathshala03@gmail.com']  # Replace with your desired email

            # Create the EmailMessage instance
            email_message = EmailMessage(
                subject=subject,
                body=message,
                from_email=from_email,
                to=recipient_list,
            )

            # Attach the uploaded file (PDF)
            if resume_file:
                email_message.attach(resume_file.name, resume_file.read(), resume_file.content_type)

            # Send the email
            email_message.send()

            return HttpResponseRedirect('/thank-you/')

    else:
        form = TutorApplicationForm()

    return render(request, 'application_form.html', {'form': form})

def thank_you(request):
    return render(request, 'thankyou.html')

def privacy_view(request):
    return render(request,'privacy_policy.html')

def Term_view(request):
    return render(request,'term_and_condition.html')
def base_view(request):
    return render(request,"base.html")