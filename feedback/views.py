
from django.views.generic.edit import CreateView
from feedback.forms import FeedbackForm

# Create your views here.

class FeedbackCreate(CreateView):
    form_class = FeedbackForm
    template_name = 'contact.html'
    success_url = 'success'
