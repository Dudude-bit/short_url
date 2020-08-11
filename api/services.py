from string import ascii_letters
import random
import redis

redis = redis.Redis()


def generate_slug():
    slug = ''.join([random.choice(ascii_letters) for _ in range(8)])
    if slug.encode('utf8') in redis.smembers('slugs_set'):
        return generate_slug()
    redis.sadd('slugs_set', slug)
    return slug


def normalize_url(url: str):
    url = url.replace('www.', '')
    url = 'https://' + url if not(url.startswith('https://')) else url
    return url
