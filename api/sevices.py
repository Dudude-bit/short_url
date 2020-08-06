from string import ascii_letters
import random
import redis

redis = redis.Redis()

def generate_slug():
    slug = ''.join([random.choice(ascii_letters) for _ in range(8)])
    if slug in set(map(lambda x: x.decode('utf8'), redis.smembers('slugs_set'))):
        return generate_slug()
    redis.sadd('slugs_set', slug)
    return slug
