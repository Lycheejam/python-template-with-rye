from src.hello_world import HelloWorld


def test_hello_world():
    hello = HelloWorld("World")
    assert hello.say_hello() == "Hello, World!"
