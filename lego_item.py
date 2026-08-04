class LegoItem:
    def __init__(self, set_name, set_number, theme, condition, complete, purchase_price, estimated_value):
        self.set_name = set_name
        self.set_number = set_number
        self.theme = theme
        self.condition = condition
        self.complete = complete
        self.purchase_price = purchase_price
        self.estimated_value = estimated_value
    def __str__(self):
        return (
            f"Set Name: {self.set_name}\n"
            f"Set Number: {self.set_number}\n"
            f"Theme: {self.theme}\n"
            f"Condition: {self.condition}\n"
            f"Complete: {self.complete}\n"
            f"Purchase Price: ${self.purchase_price:.2f}\n"
            f"Estimated Value: ${self.estimated_value:.2f}"
        )
    def to_dict(self):
        return {
            "set_name": self.set_name,
            "set_number": self.set_number,
            "theme": self.theme,
            "condition": self.condition,
            "complete": self.complete,
            "purchase_price": self.purchase_price,
            "estimated_value": self.estimated_value
    }