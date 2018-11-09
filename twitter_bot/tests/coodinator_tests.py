import unittest
import datetime

from twitter_bot.modules.coordinator import Coordinator, ISO8601, TIMEZONE


GROUND_TRUTH = [{'start_time': '2017-07-18T09:00:00+09:00',
                 'end_time': '2017-07-19T15:00:00+09:00'},
                {'start_time': '2017-07-20T03:00:00+09:00',
                 'end_time': '2017-07-21T09:00:00+09:00'},
                {'start_time': '2017-07-21T21:00:00+09:00',
                 'end_time': '2017-07-23T09:00:00+09:00'},
                {'start_time': '2017-07-23T23:00:00+09:00',
                 'end_time': '2017-07-18T09:00:00+09:00'}]


class CoordinatorTests(unittest.TestCase):
    def setUp(self):
        self.coord = Coordinator(GROUND_TRUTH)

    def tearDown(self):
        del self.coord

    def test_nothing(self):
        result = self.coord.get_start_schedule(now=datetime.datetime(2017, 7, 18, 2, tzinfo=TIMEZONE))
        self.assertIsNone(result)
        result = self.coord.get_start_schedule(now=datetime.datetime(2017, 7, 18, 8, tzinfo=TIMEZONE))
        self.assertIsNone(result)
        result = self.coord.get_start_schedule(now=datetime.datetime(2017, 7, 19, 14, tzinfo=TIMEZONE))
        self.assertIsNone(result)

    def test_get_start_schedule(self):
        for entry in GROUND_TRUTH:
            pivot_time = ''.join(entry['start_time'].rsplit(':', 1))
            pivot_time = datetime.datetime.strptime(pivot_time, ISO8601)
            result = self.coord.get_start_schedule(now=pivot_time + datetime.timedelta(minutes=29))
            self.assertEqual(entry, result)
            result = self.coord.get_start_schedule(now=pivot_time + datetime.timedelta(minutes=0))
            self.assertEqual(entry, result)
            result = self.coord.get_start_schedule(now=pivot_time - datetime.timedelta(minutes=29))
            self.assertEqual(entry, result)
            result = self.coord.get_start_schedule(now=pivot_time + datetime.timedelta(minutes=30))
            self.assertIsNone(result)
            result = self.coord.get_start_schedule(now=pivot_time - datetime.timedelta(minutes=30))
            self.assertIsNone(result)

    def test_get_end_schedule(self):
        for index in range(0, len(GROUND_TRUTH)):
            entry = GROUND_TRUTH[index]
            pivot_time = ''.join(entry['end_time'].rsplit(':', 1))
            pivot_time = datetime.datetime.strptime(pivot_time, ISO8601)
            result = self.coord.get_end_schedule(now=pivot_time + datetime.timedelta(minutes=59))
            if len(GROUND_TRUTH) > index+1:
                self.assertEqual(GROUND_TRUTH[index+1], result)
            else:
                self.assertIsNone(result)
            result = self.coord.get_end_schedule(now=pivot_time + datetime.timedelta(minutes=0))
            if len(GROUND_TRUTH) > index+1:
                self.assertEqual(GROUND_TRUTH[index+1], result)
            else:
                self.assertIsNone(result)
            result = self.coord.get_end_schedule(now=pivot_time + datetime.timedelta(minutes=60))
            self.assertIsNone(result)
            result = self.coord.get_end_schedule(now=pivot_time - datetime.timedelta(minutes=60))
            self.assertIsNone(result)

    def test_get_plan_schedule(self):
        for entry in GROUND_TRUTH:
            pivot_time = ''.join(entry['start_time'].rsplit(':', 1))
            pivot_time = datetime.datetime.strptime(pivot_time, ISO8601) - datetime.timedelta(hours=6)
            result = self.coord.get_plan_schedule(now=pivot_time + datetime.timedelta(minutes=29))
            self.assertEqual(entry, result)
            result = self.coord.get_plan_schedule(now=pivot_time + datetime.timedelta(minutes=0))
            self.assertEqual(entry, result)
            result = self.coord.get_plan_schedule(now=pivot_time - datetime.timedelta(minutes=29))
            self.assertEqual(entry, result)
            result = self.coord.get_plan_schedule(now=pivot_time + datetime.timedelta(minutes=30))
            self.assertIsNone(result)
            result = self.coord.get_plan_schedule(now=pivot_time - datetime.timedelta(minutes=30))
            self.assertIsNone(result)

    def test_get_1h_before_end_schedule(self):
        for entry in GROUND_TRUTH:
            pivot_time = ''.join(entry['end_time'].rsplit(':', 1))
            pivot_time = datetime.datetime.strptime(pivot_time, ISO8601) - datetime.timedelta(hours=1)
            result = self.coord.get_1h_before_end_schedule(now=pivot_time + datetime.timedelta(minutes=29))
            self.assertEqual(entry, result)
            result = self.coord.get_1h_before_end_schedule(now=pivot_time + datetime.timedelta(minutes=0))
            self.assertEqual(entry, result)
            result = self.coord.get_1h_before_end_schedule(now=pivot_time - datetime.timedelta(minutes=29))
            self.assertEqual(entry, result)
            result = self.coord.get_1h_before_end_schedule(now=pivot_time + datetime.timedelta(minutes=30))
            self.assertIsNone(result)
            result = self.coord.get_1h_before_end_schedule(now=pivot_time - datetime.timedelta(minutes=30))
            self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
