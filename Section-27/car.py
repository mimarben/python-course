class Car:
    def __init__(self, **kwargs):
        self.maker = kwargs["maker"]
        self.model = kwargs["model"]
    