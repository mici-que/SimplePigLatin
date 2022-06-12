from SimplePigLatin import main

# initial test
def test_init():
    assert (main()) == False


# 1 input validation


def test_IntegerInput():
    param = 10
    assert main(param) == False


# 2a calculation - one word


def test_rHoo():
    param = "rHoo"
    assert main(param) == "Hooray"


def test_HelloX():
    param = "Hello!"
    assert main(param) == "elloHay!"
