'''
Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
'''
import unittest

def flatten_dict(nested_dict):
    if not nested_dict:
        return nested_dict
    result = dict()

    def recur(cur_string, nested):
        for k, v in nested.items():
            if isinstance(v, dict):
                if not cur_string or len(cur_string) == 0:
                    recur(k, v)
                else:
                    recur(cur_string + '.' + k, v)
            else:
                if not cur_string or len(cur_string) == 0:
                    result[k] = v
                else:
                    result[cur_string + '.' + k] = v
    recur("", nested_dict)
    return result

class DailyCodingProblemTest(unittest.TestCase):
    def test_case_1(self):
        input = {
            "key": 3,
            "foo": {
                "a": 5,
                "bar": {
                    "baz": 8
                }
            }
        }
        result = flatten_dict(input)
        print(result)
        self.assertEqual(result['key'], 3)
        self.assertEqual(result['foo.a'], 5)
        self.assertEqual(result['foo.bar.baz'], 8)

    def test_case_2(self):
        input = {}
        result = flatten_dict(input)
        self.assertEqual(result, {})



if __name__ == '__main__':
    unittest.main()