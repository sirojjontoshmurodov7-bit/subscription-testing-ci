from app.subscription import Subscription

def test_trial_to_active():
    s = Subscription()
    s.activate()
    assert s.state == "active"

def test_active_to_suspended():
    s = Subscription()
    s.activate()
    s.payment_failed()
    assert s.state == "suspended"

def test_suspended_to_active():
    s = Subscription()
    s.activate()
    s.payment_failed()
    s.payment_success()
    assert s.state == "active"

def test_cancel_from_active():
    s = Subscription()
    s.activate()
    s.cancel()
    assert s.state == "canceled"
