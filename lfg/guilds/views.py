from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from lfg.guilds.models import Guild
from lfg.guilds.forms import CreateGuildForm

class CreateGuildView(FormView):
    template_name = 'guilds/create.html'
    form_class = CreateGuildForm
    success_url = '/thanks/'
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)
        
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateGuildView, self).dispatch(*args, **kwargs)
