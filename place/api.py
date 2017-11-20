"""Place api."""
from place.models import Place, Comment, Rating


def get_rating(place_id: int, user: object) -> dict:
    """Get place rating."""
    result = Rating.objects.average(place_id, user)
    return result


def vote_rating(place_id: int, user: object, vote: int) -> None:
    """Vote for place post."""
    try:
        place = Place.objects.get(pk=place_id)
        Rating.objects.update_or_create(
            place=place, user=user,
            defaults={'value': vote})
    except Place.DoesNotExist:
        pass


def get_comment(place_id: int, offset: int) -> dict:
    """Get place rating."""
    result = Comment.objects.get_last_comments(place_id, int(offset))
    return result


def send_comment(place_id: int, user: object, comment: str) -> None:
    """Add comment for place post."""
    try:
        place = Place.objects.get(pk=place_id)
        Comment.objects.create(place=place, user=user, content=comment)
    except Place.DoesNotExist:
        pass