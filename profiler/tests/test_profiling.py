
# Copyright 2018 Vauxoo (https://www.vauxoo.com) <info@vauxoo.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.tests.common import TransactionCase


class TestProfiling(TransactionCase):

    def test_profile_creation(self):
        """We are testing the creation of a profile."""
        prof_obj = self.env['profiler.profile']
        profile = prof_obj.create({'name': 'this_profiler'})
        self.assertEqual(0, profiler.attachment_count)
        profile.enable()
        self.env['res.partner'].search([], limit=1)
        profile.disable()
        self.assertNotEqual(0, profiler.attachment_count)

    def test_profile_creation(self):
        """We are testing the creation of a profile."""
        prof_obj = self.env['profiler.profile']
        profile = prof_obj.create({
            'name': 'this_profiler',
            'use_py_index': True,
        })
        self.assertEqual(0, profiler.attachment_count)
        profile.enable()
        self.env['res.partner'].search([], limit=1)
        profile.disable()
        self.assertNotEqual(0, profiler.attachment_count)

    def test_onchange(self):
        prof_obj = self.env['profiler.profile']
        profile = prof_obj.create({'name': 'this_profiler'})
        self.assertFalse(profile.description)
        profiler.enable_postgresql = True
        profiler.onchange_enable_postgresql()
        self.assertTrue(profiler.description)
        profile.enable()
        self.env['res.partner'].search([], limit=1)
        profiler.disable()
