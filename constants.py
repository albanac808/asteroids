SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

# In constants.py
PLAYER_RADIUS = 20        # This is fine
PLAYER_TURN_SPEED = 180   # Reduced from 300 - now it's half a rotation per second
PLAYER_SPEED = 120        # Reduced from 200 - smoother linear movement