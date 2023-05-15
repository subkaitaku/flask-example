import os

print(os.environ)
reload = os.getenv("RELOAD")
debug = os.getenv("DEBUG")
bind = "0.0.0.0:80"
accesslog = os.getenv("LOG")
errorlog = os.getenv("LOG")
loglevel = os.getenv("LOG_LEVEL")
