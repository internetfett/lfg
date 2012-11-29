from django import forms
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from lfg.games.models import Faction, CharacterClass, CharacterSubclass, CharacterRole
from lfg.guilds.models import Guild, GuildType, GuildPlaytime
from lfg.servers.models import Server


class CreateGuildForm(forms.ModelForm):
    name = forms.CharField(_('name'), required=True)
    server = forms.ModelChoiceField(label=_('Server'), queryset=Server.objects.all(), required=True)
    faction = forms.ModelChoiceField(label=_('Faction'), queryset=Faction.objects.all(), required=True)
    guildtype = forms.ModelChoiceField(label=_('Guild Focus'), queryset=GuildType.objects.all(), required=True)
    tagline = forms.CharField(label=_('Tagline'), required=True)
    website = forms.CharField(label=_('Website'), required=False)
    blurb = forms.CharField(label=_('Description'), required=False, widget=forms.Textarea)
    classes = forms.ModelMultipleChoiceField(label=_('Class'), queryset=CharacterClass.objects.all(), widget=forms.CheckboxSelectMultiple)
    subclasses = forms.ModelMultipleChoiceField(label=_('Subclass'), queryset=CharacterSubclass.objects.all(), widget=forms.CheckboxSelectMultiple)
    roles = forms.ModelMultipleChoiceField(label=_('Role'), queryset=CharacterRole.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Guild
        fields = ('name', 'server', 'faction', 'guildtype', 'tagline', 'website', 'blurb', 'classes', 'subclasses', 'roles')
        exclude = ('owner', 'game')

    def clean(self):
        cleaned_data = super(CreateGuildForm, self).clean()
        return cleaned_data


class GuildPlaytimeForm(forms.ModelForm):
    DAY_CHOICES = (
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
        model = GuildPlaytime

GuildPlaytimeFormSet = inlineformset_factory(Guild, GuildPlaytime, extra=7, max_num=7, form=GuildPlaytimeForm)
