"""
Openedx receivers for events in the tutorial_hooks_conf.
"""
import logging

import requests

log = logging.getLogger()


def send_enrollment_data_to_webhook(enrollment, **kwargs):  # pylint: disable=unused-argument
    """
    Listen for the enrollment event data and pass it to google sheets.
    """
    envelope = kwargs.get("metadata")

    requests.post(
        "https://hooks.zapier.com/hooks/catch/105048/33sbbyf/",
        {
            "user_id": enrollment.user.id,
            "username": enrollment.user.pii.name,
            "user_email": enrollment.user.pii.email,
            "event_type": envelope.event_type,
            "timestamp": str(envelope.time),
            "container": envelope.sourcehost,
        },
        timeout=0.1,
    )
