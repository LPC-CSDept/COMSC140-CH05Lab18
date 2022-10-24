import random
import main


def test_makeLabmda1():

    numbers1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    add100 = main.makeLambda(100)

    numbers1 = add100(numbers1)
    print('After lambda function add100 call', numbers1)

    assert numbers1[0] == 110, "Invalid value. Expected 110"
    assert numbers1[9] == 200, "Invalid value. Expected 200"


def test_makeLabmda2():

    numbers2 = [10, 20, 30, 40, 50]
    add20 = main.makeLambda(20)

    numbers2 = add20(numbers2)
    print('After lambda function add100 call', numbers2)

    assert numbers2[0] == 30, "Invalid value. Expected 30"
    assert numbers2[4] == 70, "Invalid value. Expected 70"
