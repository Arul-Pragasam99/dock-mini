import redis

cache_client = redis.Redis(
    host="redis_service",
    port=6379,
    decode_responses=True
)