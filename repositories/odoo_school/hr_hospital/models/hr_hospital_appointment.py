import logging

# noinspection PyUnresolvedReferences
from odoo import models, fields

_logger = logging.getLogger(__name__)

CONST_EXP = "Odoo school constant example"


class OSHHAppointment(models.Model):
    _name = 'hr.hospital.appointment'
    _description = 'Appointment'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
    description = fields.Text()
