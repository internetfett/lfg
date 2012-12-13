from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.simple import redirect_to

from lfg.games.models import Game
from lfg.players.forms import CreatePlayerForm, PlayerPlaytimeFormSet
from lfg.players.models import Player


class PlayerMixin(object):
    template_name = 'players/create.html'
    form_class = CreatePlayerForm
    success_url = '/thanks/'
    model = Player

    def get_context_data(self, **kwargs):
        context = super(PlayerMixin, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PlayerPlaytimeFormSet(self.request.POST)
        else:
            context['formset'] = PlayerPlaytimeFormSet()
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
        return super(PlayerMixin, self).dispatch(*args, **kwargs)


class CreatePlayerView(PlayerMixin, CreateView):
    pass


class DeletePlayerView(PlayerMixin, DeleteView):
    template_name = 'Players/delete.html'

    def get_object(self, queryset=None):
        obj = super(DeletePlayerView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj


class UpdatePlayerView(PlayerMixin, UpdateView):
    template_name = 'players/update.html'

    def get_context_data(self, **kwargs):
        context = super(UpdatePlayerView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PlayerPlaytimeFormSet(self.request.POST, instance=self.get_object())
        else:
            context['formset'] = PlayerPlaytimeFormSet(instance=self.get_object())
        return context

    def get_object(self, queryset=None):
        obj = super(UpdatePlayerView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj


class PlayerDetailView(DetailView):
    template_name = 'players/detail.html'
    model = Player
