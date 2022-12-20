from .forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse

# Create your views here.
class RevieEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        return HttpResponse('Thanks for the Review!')