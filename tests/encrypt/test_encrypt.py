from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(123456, "3")

    assert encrypt_message("ABCDEF", -1) == "FEDCBA"
    assert encrypt_message("ABCDEF", 3) == "CBA_FED"
    assert encrypt_message("ABCDEF", 2) == "FEDC_BA"
    assert encrypt_message("ABCDEF", 6) == "FEDCBA"
    assert encrypt_message("ABCDEF", 8) == "FEDCBA"
    assert encrypt_message("ABCDEF", 1) == "A_FEDCB"
    assert encrypt_message("ABCDEF", 5) == "EDCBA_F"
    assert encrypt_message("ABCDEF", 7) == "FEDCBA"
    assert encrypt_message("TESTE", 3) == "SET_ET"
