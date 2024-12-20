import logging

# noinspection PyUnresolvedReferences
from odoo import models, fields

_logger = logging.getLogger(__name__)

CONST_EXP = "Odoo school constant example"


class OSHHDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
    description = fields.Text()
