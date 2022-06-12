from SimplePigLatin import main

# initial test
def test_init():
    assert (main()) == False


# 1 input validation


def test_IntegerInput():
    param = 10
    assert main(param) == False
