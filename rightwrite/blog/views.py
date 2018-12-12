from django.views.generic.edit import FormView
from .forms import EntryForm

class EntryView(FormView):

    template_name = 'blog/newpost.html'
    form_class = EntryForm
    success_url = 'home'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)