# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Venue / Event Booking Management',
    'version': '18.0.1.0.0',
    'summary': 'Core Module for Managing Different Types of Venue/ Event Booking.',
    'category': 'Services/Venue',
    'author': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': [
        'base',
        'mail',
        'portal',
        'website',
        'account',
    ],
    'data': [
        'security/venue_booking_management_groups.xml',
        'security/venue_booking_security.xml',
        'security/ir.model.access.csv',
        'data/venue_booking_data.xml',
        'data/venue_type_data.xml',
        'data/venue_data.xml',
        'views/venue_booking_views.xml',
        'views/venue_type_views.xml',
        'views/venue_views.xml',
        'views/res_partner_views.xml',
        'wizards/venue_booking_analysis_views.xml',
        'report/venue_booking_report_views.xml',
        'report/venue_booking_report_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'venue_booking_management/static/src/js/**/*',
            'venue_booking_management/static/src/xml/**/*',
            'venue_booking_management/static/src/scss/**/*',
        ],
        'web.assets_frontend': [
            'venue_booking_management/static/src/js/website_venue_booking.js',
            'venue_booking_management/static/src/scss/website_venue_booking.scss',
        ],
    },
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}

