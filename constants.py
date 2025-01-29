SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# For Asteroid class
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

# For Player class
PLAYER_RADIUS = 20        
PLAYER_TURN_SPEED = 180   # Reduced from 300 - now it's half a rotation per second
PLAYER_SPEED = 120        # Reduced from 200 - smoother linear movement

# For Shot class
SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3