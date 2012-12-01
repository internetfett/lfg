from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.simple import redirect_to

from lfg.games.models import Game
from lfg.guilds.forms import CreateGuildForm, GuildPlaytimeFormSet
from lfg.guilds.models import Guild


class GuildMixin(object):
    template_name = 'guilds/create.html'
    form_class = CreateGuildForm
    success_url = '/thanks/'
    model = Guild

    def get_context_data(self, **kwargs):
        context = super(GuildMixin, self).get_context_data(**kwargs)
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
        return super(GuildMixin, self).dispatch(*args, **kwargs)


class CreateGuildView(GuildMixin, CreateView):
    pass


class DeleteGuildView(GuildMixin, DeleteView):
    template_name = 'guilds/delete.html'

    def get_object(self, queryset=None):
        obj = super(DeleteGuildView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj


class UpdateGuildView(GuildMixin, UpdateView):
    template_name = 'guilds/update.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateGuildView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = GuildPlaytimeFormSet(self.request.POST, instance=self.get_object())
        else:
            context['formset'] = GuildPlaytimeFormSet(instance=self.get_object())
        return context

    def get_object(self, queryset=None):
        obj = super(UpdateGuildView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj


class GuildDetailView(DetailView):
    template_name = 'guilds/detail.html'
    model = Guild
