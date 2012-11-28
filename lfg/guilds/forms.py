from django import forms
from django.utils.translation import ugettext_lazy as _
from lfg.games.models import Faction, CharacterClass, CharacterSubclass, CharacterRole
from lfg.guilds.models import Guild, GuildType
from lfg.servers.models import Server

class CreateGuildForm(forms.ModelForm):
    DAY_CHOICES = (
        ('1', 'Sunday'),
        ('2', 'Monday'),
        ('3', 'Tuesday'),
        ('4', 'Wednesday'),
        ('5', 'Thursday'),
        ('6', 'Friday'),
        ('7', 'Saturday'),
    )
    name = forms.CharField(_('name'), required=True)
    server = forms.ModelChoiceField(label=_('Server'), queryset=Server.objects.all(), required=True)
    faction = forms.ModelChoiceField(label=_('Faction'), queryset=Faction.objects.all(), required=True)
    guildtype = forms.ModelChoiceField(label=_('Guild Focus'), queryset=GuildType.objects.all(), required=True)
    tagline = forms.CharField(label=_('Tagline'), required=True)
    website = forms.CharField(label=_('Website'), required=False)
    blurb = forms.CharField(label=_('Description'), required=False, widget=forms.Textarea)
    classes = forms.ModelChoiceField(label=_('Class'), queryset=CharacterClass.objects.all())
    subclasses = forms.ModelChoiceField(label=_('Subclass'), queryset=CharacterSubclass.objects.all())
    roles = forms.ModelChoiceField(label=_('Role'), queryset=CharacterRole.objects.all())
        
    class Meta:
       model = Guild
       fields = ('name', 'server', 'faction', 'guildtype', 'tagline', 'website', 'blurb', 'classes', 'subclasses', 'roles')
    
    def clean(self):
        cleaned_data = super(CreateGuildForm, self).clean()
        return cleaned_data
