import unittest
import json
import trans as app


class TestTrans(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app_trans = app.Trans()

    def setUp(self):
        filename = r"..\fixtures\words.json"
        with open(filename, encoding="utf-8") as f:
            self.words = json.load(f)

    def test_trans_correct_translation(self):
        for word_eng, word_ru in self.words.items():
            res = self.app_trans.trans_text(word_eng)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(word_ru, res.json()['text'].pop(0))

    def test_trans_incorrect_translation(self):
        word_ru = "досвидания"
        word_eng = "hello"
        res = self.app_trans.trans_text(word_eng)
        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(word_ru, res.json()['text'].pop(0))

    def test_trans_invalid_request(self):
        word_eng = None
        res = self.app_trans.trans_text(word_eng)
        self.assertNotEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()

