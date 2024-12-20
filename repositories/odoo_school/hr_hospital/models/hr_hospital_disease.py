import logging

# noinspection PyUnresolvedReferences
from odoo import models, fields

_logger = logging.getLogger(__name__)

CONST_EXP = "Odoo school constant example"


class OSHHDisease(models.Model):
    _name = 'hr.hospital.disease'
    _description = 'Disease'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
    description = fields.Text()
