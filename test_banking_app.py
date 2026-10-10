from decimal import Decimal

import pytest
from banking_app import Account, account, retrieve_account

def test_account_starts_with_zero_balance():
    new_account = Account()
    
    assert new_account.balance == Decimal("0.00")

def test_retrieve_account_returns_account():
    retrieved_account = retrieve_account()

    assert retrieved_account is account

def test_account_rejects_float_balance():
    with pytest.raises(TypeError):
        Account(balance=100.50)