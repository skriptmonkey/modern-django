from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY',
        default='ogvl7w3-ix9h5pd%t6)v^mavx&ujww**sfnngwrjx@u%hbpdj)')

DEBUG = env.bool('DJANGo_DEBUG', default=True)
