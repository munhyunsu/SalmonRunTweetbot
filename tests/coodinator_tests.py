import unittest
import datetime

import coordinator

GROUND_TRUTH = [{'start_time': datetime.datetime(2017, 7, 18, 9),
                 'end_time': datetime.datetime(2017, 7, 19, 15)},
                {'start_time': datetime.datetime(2017, 7, 20, 3),
                 'end_time': datetime.datetime(2017, 7, 21, 9)},
                {'start_time': datetime.datetime(2017, 7, 21, 21),
                 'end_time': datetime.datetime(2017, 7, 23, 9)},
                {'start_time': datetime.datetime(2017, 7, 23, 21),
                 'end_time': datetime.datetime(2017, 7, 25, 3)}]


class CoordinatorTests(unittest.TestCase):
    def setUp(self):
        self.coord = coordinator.Coordinator()
        schedule_list = GROUND_TRUTH
        self.coord.feed_schedule_list(schedule_list)

    def tearDown(self):
        del self.coord

    def test_nothing(self):
        result = self.coord.get_start_schedule(now=datetime.datetime(2017, 7, 18, 2))
        self.assertIsNone(result)
        result = self.coord.get_start_schedule(now=datetime.datetime(2017, 7, 18, 8))
        self.assertIsNone(result)
        result = self.coord.get_start_schedule(now=datetime.datetime(2017, 7, 19, 14))
        self.assertIsNone(result)

    def test_get_start_schedule(self):
        for entry in GROUND_TRUTH:
            pivot_time = entry['start_time']
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
            pivot_time = entry['end_time']
            result = self.coord.get_end_schedule(now=pivot_time + datetime.timedelta(minutes=29))
            if len(GROUND_TRUTH) > index+1:
                self.assertEqual(GROUND_TRUTH[index+1], result)
            else:
                self.assertIsNone(result)
            result = self.coord.get_end_schedule(now=pivot_time + datetime.timedelta(minutes=0))
            if len(GROUND_TRUTH) > index+1:
                self.assertEqual(GROUND_TRUTH[index+1], result)
            else:
                self.assertIsNone(result)
            result = self.coord.get_end_schedule(now=pivot_time - datetime.timedelta(minutes=29))
            if len(GROUND_TRUTH) > index+1:
                self.assertEqual(GROUND_TRUTH[index+1], result)
            else:
                self.assertIsNone(result)
            result = self.coord.get_end_schedule(now=pivot_time + datetime.timedelta(minutes=30))
            self.assertIsNone(result)
            result = self.coord.get_end_schedule(now=pivot_time - datetime.timedelta(minutes=30))
            self.assertIsNone(result)

    def test_get_plan_schedule(self):
        for entry in GROUND_TRUTH:
            pivot_time = entry['start_time'] - datetime.timedelta(hours=6)
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