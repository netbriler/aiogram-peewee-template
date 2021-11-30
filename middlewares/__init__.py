def setup_middleware(dp):
    from .throttling import ThrottlingMiddleware
    from .logging import LoggingMiddleware

    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(LoggingMiddleware())
