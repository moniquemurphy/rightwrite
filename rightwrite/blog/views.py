from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import EntryForm

class EntryView(FormView):

    template_name = 'blog/createentry.html'
    form_class = EntryForm
    success_url = reverse_lazy('create_entry')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(EntryView, self).get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs