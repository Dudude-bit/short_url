from string import ascii_letters
import random
import redis
from django.contrib.auth.models import AnonymousUser
import re

redis = redis.Redis()


def generate_slug():
    slug = ''.join([random.choice(ascii_letters) for _ in range(8)])
    if slug.encode('utf8') in redis.smembers('slugs_set'):
        return generate_slug()
    redis.sadd('slugs_set', slug)
    return slug


def normalize_url(url: str):
    if not url:
        return None
    url = re.sub(r"^(?:https?://)|(?:www.)|(?:)", 'http://', url, count=1, flags=re.IGNORECASE)
    return url


def delete_slug(slug):
    redis.srem('slugs_set', slug)


class CurrentUserDefault:
    requires_context = True

    def __call__(self, serializer_field):
        if type(serializer_field.context['request'].user) == AnonymousUser:
            return None
        return serializer_field.context['request'].user

    def __repr__(self):
        return '%s()' % self.__class__.__name__
