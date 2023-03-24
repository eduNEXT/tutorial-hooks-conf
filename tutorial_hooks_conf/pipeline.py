"""
Openedx Pipeline Steps for tutorial_hooks_conf.
"""
# pylint: disable=arguments-differ, unused-argument
import logging

from openedx_filters import PipelineStep

log = logging.getLogger()


class OnlyVisibleForEmailDomains(PipelineStep):
    """
    Filter to make the /courses/<course-ID>/about page visible to a subset of users.
    """

    def run_filter(self, context, template_name):
        """
        Compare the user domain to a list of allowed domains.

        The filter only continues if everything matches.
        """
        log.info("The pipelineStep is being executed")

        return {
            "context": context,
            "template_name": template_name,
        }
