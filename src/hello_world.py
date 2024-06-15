class HelloWorld:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def say_hello(self) -> str:
        return f"Hello, {self.name}!"
