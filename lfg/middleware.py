from django.conf import settings
from lfg.games.models import Game

class LFGGameMiddleware(object):

    def process_request(self, request):
        """
        :param request:
        Patches and instance of the current game to the request.
        :return: None
        """
        try:
            game = Game.objects.get(abbr=request.subdomain)
        except Game.DoesNotExist:
            game = Game.objects.get(id=settings.DEFAULT_GAME_ID)

        # Patch it to the request
        setattr(request, 'game', game)

        return None