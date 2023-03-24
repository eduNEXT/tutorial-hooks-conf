"""
Openedx receivers for events in the tutorial_hooks_conf.
"""
import logging

log = logging.getLogger()


def send_enrollment_data_to_webhook(enrollment, **kwargs):  # pylint: disable=unused-argument
    """
    Listen for the enrollment event data and pass it to google sheets.
    """
    log.info("The receiver for COURSE_ENROLLMENT_CREATED is working")
