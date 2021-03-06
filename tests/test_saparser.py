import unittest
from pprint import pprint
from score import SAParser, query_scorepage


class TestSAParser(unittest.TestCase):
    def data_13s(self):
        with open("tests/data/kdubs_13s.html") as file:
            return file.read()

    def data_14s(self):
        with open("tests/data/kdubs_14s.html") as file:
            return file.read()

    def test_14s_alignment(self):
        parser = SAParser(self.data_14s())
        ids = parser.get_songids()
        songnames = parser.get_songnames()
        charts = parser.get_charts()
        scores = parser.get_scores()
        combos = parser.get_combotype()

        num_songs = len(ids)
        self.assertEqual(num_songs, len(scores))
        self.assertEqual(num_songs, len(songnames))
        self.assertEqual(num_songs, len(charts))
        self.assertEqual(num_songs, len(combos))

    def test_13s_alignment(self):
        parser = SAParser(self.data_13s())
        ids = parser.get_songids()
        songnames = parser.get_songnames()
        charts = parser.get_charts()
        scores = parser.get_scores()
        combos = parser.get_combotype()

        parser.debug()
        num_songs = len(ids)
        self.assertEqual(num_songs, len(scores))
        self.assertEqual(num_songs, len(songnames))
        self.assertEqual(num_songs, len(charts))
        self.assertEqual(num_songs, len(combos))


class TestQueryScorepage(unittest.TestCase):
    def test_query(self):
        data = query_scorepage("51527333", "14")
        # self.assertEqual(119, len(data))
        for i in data:
            if i.hasEmpty():
                print(i)
            self.assertFalse(i.hasEmpty())
