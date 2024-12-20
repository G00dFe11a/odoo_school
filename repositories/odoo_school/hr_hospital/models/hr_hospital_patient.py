import logging

# noinspection PyUnresolvedReferences
from odoo import models, fields

_logger = logging.getLogger(__name__)

CONST_EXP = "Odoo school constant example"


class OSHHPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
    description = fields.Text()

    res_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string="Examing doctor",
    )
