from loader import dp
from .admin import Admin

if __name__ == 'bot.filters':
    dp.filters_factory.bind(Admin)
