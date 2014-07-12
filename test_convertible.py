import unittest
import tempfile

import os

from convertible import from_json, to_json, read_json, write_json


class Klass:

    def __init__(self, member1, member2):
        self.member1 = member1
        self.member2 = member2


class TestJson(unittest.TestCase):

    def test_from_object_json(self):
        json_text = '{"member1": "value", "member2": 345}'
        actual = from_json(json_text)
        self.assertEquals("value", actual.member1)
        self.assertEquals(345, actual.member2)

    def test_from_nested_json(self):
        json_text = '{"member1": "value1", "member2": {"member1": 345, "member2": "value2"}}'
        actual = from_json(json_text)
        self.assertEquals("value1", actual.member1)
        self.assertEquals(345, actual.member2.member1)
        self.assertEquals("value2", actual.member2.member2)

    def test_from_list_json(self):
        json_text = '[{"member1": "value1", "member2": 123}, {"member1": "value2", "member2": 345}]'
        actual = from_json(json_text)
        self.assertEquals(2, len(actual))
        self.assertEquals("value1", actual[0].member1)
        self.assertEquals(123, actual[0].member2)
        self.assertEquals("value2", actual[1].member1)
        self.assertEquals(345, actual[1].member2)

    def test_object_to_json(self):
        obj = Klass("value", 345)
        actual = to_json(obj)
        expected = '{"member1": "value", "member2": 345}'
        self.assertEquals(expected, actual)

    def test_nested_to_json(self):
        obj = Klass(True, Klass("value", 345))
        actual = to_json(obj)
        expected = '{"member1": true, "member2": {"member1": "value", "member2": 345}}'
        self.assertEquals(expected, actual)

    def test_list_to_json(self):
        objects_list = [Klass("value1", 123), Klass("value2", 345)]
        actual = to_json(objects_list)
        expected = '[{"member1": "value1", "member2": 123}, {"member1": "value2", "member2": 345}]'
        self.assertEquals(expected, actual)

    def test_dictionary_to_json(self):
        objects_dict = {"obj1": Klass("value1", 123), "obj2": Klass("value2", 345)}
        actual = to_json(objects_dict)
        expected = '{"obj1": {"member1": "value1", "member2": 123}, "obj2": {"member1": "value2", "member2": 345}}'
        self.assertEquals(expected, actual)


class TestJsonFile(unittest.TestCase):

    def temp_text(self, text=''):
        fd, filename = tempfile.mkstemp()
        f = os.fdopen(fd, 'w')
        f.write(text)
        f.close()
        return filename

    def test_read_file(self):
        filename = self.temp_text('{"member1": "value", "member2": 345}')

        actual = read_json(filename)
        self.assertEquals("value", actual.member1)
        self.assertEquals(345, actual.member2)

    def test_write_file(self):
        filename = self.temp_text()

        obj = Klass("value", 345)
        write_json(filename, obj)

        actual = read_json(filename)
        self.assertEquals("value", actual.member1)
        self.assertEquals(345, actual.member2)

    def test_from_non_existing_file(self):
        filename = self.temp_text('{"member1": "value", "member2": 345}')
        os.remove(filename)
        actual = read_json(filename)
        self.assertIsNone(actual)

    def test_from_empty_file(self):
        filename = self.temp_text()
        actual = read_json(filename)
        self.assertIsNone(actual)

    def test_from_new_lines_and_spaces(self):
        filename = self.temp_text(' \n \n  \n')
        actual = read_json(filename)
        self.assertIsNone(actual)

    def test_None_to_json(self):
        filename = self.temp_text()

        write_json(filename, None)

        actual = read_json(filename)
        self.assertIsNone(actual)