import unittest


class BigInteger(object):
    """
    Sometimes we need to work with numbers that exceed the range of an integer. One workaround is to represent numbers
    in a list. For example, the number 1234 would be represented as [1, 2, 3, 4]. This would prevent overflow issues as
    lists can grow arbitrarily large. We will need to provide arithmetic implementations to allow users to
    add and subtract numbers using our BigInteger implementation.
    """

    def __init__(self, string_representation):
        """
        This is the constructor method. Initialize any data structures you want to use here
        """
        self.numbers = [integer for integer in string_representation]

    def __repr__(self):
        """
        This is the `toString()` equivalent for Python. Implementing this method allows us to get a readable string
        representation of the class

        >>> str(BigInteger('1234'))
        1234 # instead of some hash code

        """
        return ''.join(self.numbers)

    def __add__(self, other):
        """
        Implementing this method allows us to use the `+` operator with this class. For example

        >>> BigInteger('1') + BigInteger('2')
        BigInteger('3')

        Adds `self` with `other`: in other words, performs the operation self + other

        Returns a big integer representing the sum of the two numbers
        :param other: BigInteger
        :return: BigInteger
        """
        return BigInteger('')

    def __sub__(self, other):
        """
        Implementing this method allows us to use the `-` operator with this class. For example

        >>> BigInteger('2') + BigInteger('1')
        BigInteger('1')

        Subtracts `other` from `self: in other words, performs the operation self - other. Throws an exception if
        `other` is greater than `self`

        Returns a big integer representing the difference of the two numbers
        :param other: BigInteger
        :return: BigInteger
        """
        if str(self) < str(other):
            raise Exception('{} - {} will result in a negative number'.format(self, other))

        raise Exception('Implement me!')

    def __eq__(self, other):
        """
        This is the `equals()` equivalent for Python. Implementing this method allows us to compare two instances of a
        class to determine if they are equal.

        This method is already implemented.
        """
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__


class BigNumberTest(unittest.TestCase):
    def test_singleDigitAdditionWithNoOverflowReturnsProperBigInteger(self):
        number1 = BigInteger('2')
        number2 = BigInteger('5')

        expected = BigInteger('7')
        assert number1 + number2 == expected, 'your sum does not equal 7 :('

    def test_singleDigitSubtractionReturnsProperBigInteger(self):
        number1 = BigInteger('5')
        number2 = BigInteger('2')

        expected = BigInteger('3')
        assert number1 - number2 == expected, 'your difference does not equal 3 :('
