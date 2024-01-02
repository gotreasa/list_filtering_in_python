import pytest
from modules import list_filtering


def describe_filter_list():
    def should_error_for_non_list():
        """🧪 should give an error when something other than a list is supplied"""
        with pytest.raises(ValueError, match="❗️ Input should be a list"):
            list_filtering.filter_list("blah")

    def should_give_1_2_to_match_input():
        """🧪 should take the list 1,2 and give back 1,2"""
        assert list_filtering.filter_list([1, 2]) == [1, 2]

    def should_give_1_3_to_match_input():
        """🧪 should take the list 1,3 and give back 1,3"""
        assert list_filtering.filter_list([1, 3]) == [1, 3]

    def should_give_4_2_to_match_input():
        """🧪 should take the list 4, 2 and give back 4, 2"""
        assert list_filtering.filter_list([4, 2]) == [4, 2]

    def should_give_strip_letters_from_1_2_a_b():
        """🧪 should take the list 1,2,'a','b' and give back 1,2"""
        assert list_filtering.filter_list([1, 2, "a", "b"]) == [1, 2]

    def should_give_strip_letters_from_1_a_b_0_15():
        """🧪 should take the list 1,'a','b',0,15 and give back 1,0,15"""
        assert list_filtering.filter_list([1, "a", "b", 0, 15]) == [1, 0, 15]
