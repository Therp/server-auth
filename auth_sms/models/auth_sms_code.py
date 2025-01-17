# Copyright 2019-2025 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class AuthSmsCode(models.Model):
    _name = "auth_sms.code"
    _description = "Hold a code for a session"
    _rec_name = "code"

    code = fields.Char(required=True, index=True)
    user_id = fields.Many2one(
        comodel_name="res.users",
        required=True,
        index=True,
        ondelete="cascade",
    )
    session_id = fields.Char(index=True)
