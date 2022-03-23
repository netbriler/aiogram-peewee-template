def setup_middleware(dp):
    from .throttling import ThrottlingMiddleware
    from .logging import LoggingMiddleware
    from .user import UsersMiddleware
    from .i18n import i18n

    dp.middleware.setup(UsersMiddleware())
    dp.middleware.setup(i18n)
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(LoggingMiddleware())
