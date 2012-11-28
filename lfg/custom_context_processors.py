def game_info(request):
    from lfg.games.models import Game
    try:
        game = Game.objects.get(abbr=request.subdomain)
        game_name = game.name
        game_id = game.id
    except:
        game_name = 'World of Warcraft'
        game_id = 1
    return {'game_name': game_name, 'game_id': game_id}
