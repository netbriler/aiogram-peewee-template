from loader import dp
from .admin import Admin

if __name__ == 'filters':
    dp.filters_factory.bind(Admin)
