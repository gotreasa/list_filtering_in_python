import pytest
from modules import list_filtering


def describe_filter_list():
    def should_error_for_non_list():
        """🧪 should give an error when something other than a list is supplied"""
        with pytest.raises(ValueError, match="❗️ Input should be a list"):
            list_filtering.filter_list("blah")
