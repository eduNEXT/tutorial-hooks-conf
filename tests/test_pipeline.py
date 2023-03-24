#!/usr/bin/env python
"""
Tests for the `tutorial-hooks-conf` filters module.
"""

from unittest.mock import Mock, patch

from django.test import TestCase, override_settings
from openedx_filters.learning.filters import CourseAboutRenderStarted


@override_settings(
    OPEN_EDX_FILTERS_CONFIG={
        "org.openedx.learning.course_about.render.started.v1": {
            "fail_silently": False,
            "pipeline": [
                "tutorial_hooks_conf.pipeline.OnlyVisibleForEmailDomains"
            ]
        }
    }
)
class OnlyVisibleForEmailDomainsTestCase(TestCase):
    """
    You can test your own code independently of the edx-platform repo
    """

    def test_redirect_denied(self):
        """
        Email domains not in the list will get a redirection
        """
        mock_req = Mock()
        mock_req.user.email = "denied@not-allowed.com"
        mock_course = Mock()
        mock_course.org = "Demo"
        with patch('tutorial_hooks_conf.pipeline.crum.get_current_request', return_value=mock_req):
            with self.assertRaises(CourseAboutRenderStarted.RedirectToPage):
                CourseAboutRenderStarted.run_filter(
                    context={"course": mock_course},
                    template_name="some_template.html"
                )

    def test_let_allowed_pass(self):
        """
        Email domains in the list get the page rendered as usual.
        """
        mock_req = Mock()
        mock_req.user.email = "welcome@allowed.com"
        mock_course = Mock()
        mock_course.org = "Demo"
        with patch('tutorial_hooks_conf.pipeline.crum.get_current_request', return_value=mock_req):
            CourseAboutRenderStarted.run_filter(
                    context={"course": mock_course},
                    template_name="some_template.html"
                )
