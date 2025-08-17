# Create your views here.
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_thankyou')  # after submit redirect to thank you page
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def feedback_thankyou(request):
    return render(request, 'thankyou.html')