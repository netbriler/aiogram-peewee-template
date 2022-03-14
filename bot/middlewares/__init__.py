def setup_middleware(dp):
    from .throttling import ThrottlingMiddleware
    from .logging import LoggingMiddleware
    from .user import UsersMiddleware

    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(LoggingMiddleware())
    dp.middleware.setup(UsersMiddleware())
