"""
Common settings for the tutorial-hooks-conf project.
"""


def plugin_settings(settings):
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """
    settings.OPEN_EDX_FILTERS_CONFIG = getattr(settings, "OPEN_EDX_FILTERS_CONFIG", {})
