import redis
import sys
from . import settings
r = redis.Redis(host='localhost', port=6379, db=0, password=settings.REDIS_PASS)
r.set('foo', 'bar')
r.get('foo')

print(r.get('foo'))