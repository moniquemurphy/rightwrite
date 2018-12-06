from django.views.generic.edit import FormView
from .forms import PostForm

class PostView(FormView):

    template_name = 'mainsite/newpost.html'
    form_class = PostForm
    success_url = 'home'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)