class Locator:
    def __init__(self, locator_type, locator_string):
        self.locator_type = locator_type
        self.locator = locator_string

    def __call__(self, **kwargs):
        locator = self.locator.format(**kwargs) if kwargs else self.locator
        return self.locator_type, locator
