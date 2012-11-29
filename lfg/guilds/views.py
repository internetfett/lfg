from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views.generic.simple import redirect_to

from lfg.games.models import Game
from lfg.guilds.forms import CreateGuildForm, GuildPlaytimeFormSet
from lfg.guilds.models import Guild

class CreateGuildView(CreateView):
    template_name = 'guilds/create.html'
    form_class = CreateGuildForm
    success_url = '/thanks/'
    
    def get_context_data(self, **kwargs):
        context = super(CreateGuildView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = GuildPlaytimeFormSet(self.request.POST)
        else:
            context['formset'] = GuildPlaytimeFormSet()
        return context
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = User.objects.get(id=self.request.user.id)
        try:
            game = Game.objects.get(abbr=self.request.subdomain)
            game_id = game.id
        except:
            game_id = 1
        instance.game = Game.objects.get(id=game_id)
        instance.save()
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateGuildView, self).dispatch(*args, **kwargs)
