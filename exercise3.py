import unittest


def encrypt(text):
    key= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    master = ['e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d']

    textin = list(text)

    crypt = []

    for n in textin:
        index = key.index(n)
        crypt.append(master[index])

    return "".join(crypt)


def cat_dog_exact_repeat(text):
    times_cat_found = text.count("cat")
    times_dog_found = text.count("dog")

    return times_cat_found == times_dog_found


class TestExercise3(unittest.TestCase):
    """
    python -m unittest -v exercise3
    """

    def test_ecrypt(self):
        self.assertEqual(encrypt("helloworld"), "lippsasvph")

    def test_cat_dog_exact_repeat(self):
        self.assertTrue(cat_dog_exact_repeat("catdogcatdogcatdognotnotcatdog"))
        self.assertFalse(cat_dog_exact_repeat("cadogcadogcadognotnotcatdog"))
