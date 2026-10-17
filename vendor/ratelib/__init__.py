class RateLimiter:
    def __init__(self, burst, rate):
        self.burst = burst
        self.rate = rate
