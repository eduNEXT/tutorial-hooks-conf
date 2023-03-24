"""
Openedx Pipeline Steps for tutorial_hooks_conf.
"""
# pylint: disable=arguments-differ, unused-argument
import logging

import crum
from openedx_filters import PipelineStep
from openedx_filters.learning.filters import CourseAboutRenderStarted

log = logging.getLogger()


ALLOWED_DOMAINS = [
    "myuniversity.com",
    "allowed.com",
]
SPECIAL_ORGS = [
    "Demo",
]


class OnlyVisibleForEmailDomains(PipelineStep):
    """
    Filter to make the /courses/<course-ID>/about page visible to a subset of users.
    """

    def run_filter(self, context, template_name):
        """
        Compare the user domain to a list of allowed domains.

        The filter only continues if everything matches.
        """
        if context["course"].org not in SPECIAL_ORGS:
            return {}

        user = crum.get_current_request().user

        try:
            domain = user.email.split('@')[1]
            if domain in ALLOWED_DOMAINS:
                return {}

        except AttributeError:
            pass

        raise CourseAboutRenderStarted.RedirectToPage(message="Not allowed", redirect_to="/courses/")
