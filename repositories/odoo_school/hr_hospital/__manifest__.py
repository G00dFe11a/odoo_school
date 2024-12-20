{
    'name': 'Odoo School HR Hospital',
    'author': 'Odoo School',
    'website': 'https://odoo.school/',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.1.0.0',

    'depends': [
        'base'
    ],

    'external_dependencies': {
        'python': []
    },

    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menu.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_disease_views.xml',
        'views/hr_hospital_appointment_views.xml',
        'demo/hr.hospital.disease.xml'

    ],
    'demo': [
        'demo/hr.hospital.doctor.csv',
        'demo/hr.hospital.patient.csv'
    ],

    'installable': True,
    'auto_install': False
}
