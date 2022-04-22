from aiogram.bot.api import TelegramAPIServer


class TelegramAPITestServer(TelegramAPIServer):
    @classmethod
    def from_base(cls, base: str) -> 'TelegramAPIServer':
        base = base.rstrip("/")
        return cls(
            base=f'{base}/bot{{token}}/test/{{method}}',
            file=f'{base}/file/bot{{token}}/test/{{path}}',
        )


TELEGRAM_TEST = TelegramAPITestServer.from_base('https://api.telegram.org')
