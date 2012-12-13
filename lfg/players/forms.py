from django import forms
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from lfg.games.models import Faction, CharacterClass, CharacterSubclass, CharacterRole
from lfg.players.models import Player, PlayerPlaytime
from lfg.servers.models import Server


class CreatePlayerForm(forms.ModelForm):
    name = forms.CharField(_('name'), required=True)
    server = forms.ModelChoiceField(label=_('Server'), queryset=Server.objects.all(), required=True)
    faction = forms.ModelChoiceField(label=_('Faction'), queryset=Faction.objects.all(), required=True)
    level = forms.IntegerField(label=_('Level'), required=True)
    blurb = forms.CharField(label=_('Description'), required=False, widget=forms.Textarea)
    classes = forms.ModelMultipleChoiceField(label=_('Class'), queryset=CharacterClass.objects.all(), widget=forms.CheckboxSelectMultiple)
    subclasses = forms.ModelMultipleChoiceField(label=_('Subclass'), queryset=CharacterSubclass.objects.all(), widget=forms.CheckboxSelectMultiple)
    roles = forms.ModelMultipleChoiceField(label=_('Role'), queryset=CharacterRole.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Player
        fields = ('name', 'server', 'faction', 'level', 'blurb', 'classes', 'subclasses', 'roles')
        exclude = ('owner', 'game')

    def clean(self):
        cleaned_data = super(CreatePlayerForm, self).clean()
        return cleaned_data


class PlayerPlaytimeForm(forms.ModelForm):
    DAY_CHOICES = (
        ('', ''),
        ('1', 'Sunday'),
        ('2', 'Monday'),
        ('3', 'Tuesday'),
        ('4', 'Wednesday'),
        ('5', 'Thursday'),
        ('6', 'Friday'),
        ('7', 'Saturday'),
    )
    day = forms.ChoiceField(label=_('Day'), choices=DAY_CHOICES, required=True)
    start_time = forms.TimeField(label=_('Start Time'), required=True)
    end_time = forms.TimeField(label=_('End Time'), required=True)

    class Meta:
        model = PlayerPlaytime

PlayerPlaytimeFormSet = inlineformset_factory(Player, PlayerPlaytime, extra=7, max_num=7, form=PlayerPlaytimeForm)
