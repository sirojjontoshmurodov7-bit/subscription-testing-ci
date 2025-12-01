class Subscription:
    def __init__(self):
        self.state = "trial"

    def activate(self):
        if self.state == "trial":
            self.state = "active"

    def payment_failed(self):
        if self.state == "active":
            self.state = "suspended"

    def payment_success(self):
        if self.state == "suspended":
            self.state = "active"

    def cancel(self):
        if self.state in ["active", "suspended"]:
            self.state = "canceled"
