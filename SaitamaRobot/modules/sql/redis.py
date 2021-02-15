from SaitamaRobot import REDIS

# AFK
def is_user_afk(userid):
    afk = REDIS.get(f'is_afk_{userid}')
    if afk:
        return True
    else:
        return False


def start_afk(userid, reason):
    REDIS.set(f'is_afk_{userid}', reason)
    
def afk_reason(userid):
    return strb(REDIS.get(f'is_afk_{userid}'))

def end_afk(userid):
    REDIS.delete(f'is_afk_{userid}')
    return True


# Helpers
def strb(REDIS_string):
    return str(REDIS_string)

