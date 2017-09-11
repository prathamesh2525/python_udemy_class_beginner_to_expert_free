import unittest


def find_letter(letter, text):
    """

    :param letter: Letter to search for
    :param text: text to search in
    :return:Boolean
    """

    return letter in text


def reverse(text):
    rtext = list(text)
    rtext.reverse()
    return "".join(rtext)


class TestExercise2(unittest.TestCase):
    """
    python -m unittest -v exercise2
    """

    def test_letter_found(self):
        self.assertTrue(find_letter("S", "Example String"))

    def test_reverse(self):
        self.assertEqual(reverse("helloworld"), "dlrowolleh")