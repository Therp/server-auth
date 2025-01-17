# Copyright 20192024 Therp BV <https://therp.nl>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


class AccessDeniedNoSmsCode(Exception):
    def __init__(self, user, message=None):
        self.user = user
        super().__init__(message)


class AccessDeniedWrongSmsCode(Exception):
    pass


class AccessDeniedSmsRateLimit(Exception):
    pass
