#!/usr/bin/env python
"""
Tests for the `tutorial-hooks-conf` receivers module.
"""
import datetime

from django.test import TestCase
from opaque_keys.edx.keys import CourseKey
from openedx_events.learning.data import CourseData, CourseEnrollmentData, UserData, UserPersonalData
from openedx_events.learning.signals import COURSE_ENROLLMENT_CREATED

from tutorial_hooks_conf.receivers import send_enrollment_data_to_webhook


class EnrollmentReceiverTest(TestCase):
    """
    Tests the registration receiver processes the data correctly.
    """

    def setUp(self):
        """
        Setup common conditions for every test case.
        """
        super().setUp()
        self.enrollment = CourseEnrollmentData(
            user=UserData(
                pii=UserPersonalData(
                    username="student",
                    email="student@myuniversity.com",
                    name="A Full Name",
                ),
                id=42,
                is_active=True,
            ),
            course=CourseData(
                course_key=CourseKey.from_string("course-v1:Demo+HooksTutorial+2023"),
                display_name="Hooks Tutorial Course",
            ),
            mode="honor",
            is_active=True,
            creation_date=datetime.datetime(2023, 3, 28, 15, 55, 00),
        )

    def test_receiver_called(self):
        """
        Test that receiver is called with the correct information.
        """
        COURSE_ENROLLMENT_CREATED.connect(send_enrollment_data_to_webhook)

        COURSE_ENROLLMENT_CREATED.send_event(
            enrollment=self.enrollment,
        )
