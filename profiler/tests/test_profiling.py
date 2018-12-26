
# Copyright 2018 Vauxoo (https://www.vauxoo.com) <info@vauxoo.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.tests.common import HttpCase
from xmlrpc.client import Fault


class TestProfiling(HttpCase):

    def test_profile_creation(self):
        """We are testing the creation of a profile."""
        prof_obj = self.env['profiler.profile']
        profile = prof_obj.create({'name': 'this_profiler'})
        self.assertEqual(0, profile.attachment_count)
        profile.enable()
        with self.assertRaises(Fault):
            self.xmlrpc_common.authenticate(
                self.env.cr.dbname, 'this is not a user',
                'this is not a password', {})
        profile.disable()
        self.assertNotEqual(0, profile.attachment_count)

    def test_profile_creation(self):
        """We are testing the creation of a profile."""
        prof_obj = self.env['profiler.profile']
        profile = prof_obj.create({
            'name': 'this_profiler',
            'use_py_index': True,
        })
        self.assertEqual(0, profile.attachment_count)
        profile.enable()
        with self.assertRaises(Fault):
            self.xmlrpc_common.authenticate(
                self.env.cr.dbname, 'this is not a user',
                'this is not a password', {})
        profile.disable()
        self.assertNotEqual(0, profile.attachment_count)

    def test_onchange(self):
        prof_obj = self.env['profiler.profile']
        profile = prof_obj.create({'name': 'this_profiler'})
        self.assertFalse(profile.description)
        profile.enable_postgresql = True
        profile.onchange_enable_postgresql()
        self.assertTrue(profile.description)
        profile.enable()
        with self.assertRaises(Fault):
            self.xmlrpc_common.authenticate(
                self.env.cr.dbname, 'this is not a user',
                'this is not a password', {})
        profile.disable()
