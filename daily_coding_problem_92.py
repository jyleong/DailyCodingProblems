'''
We're given a hashmap associating each courseId key with a list of courseIds values, 
which represents that the prerequisites of courseId are courseIds. Return a sorted 
ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, 
should return ['CSC100', 'CSC200', 'CSCS300'].

'''
import unittest

def getCourseOrder(courseList):
    def build_course_list(course, courseList, visiting, visited, result):
        if (course in visiting):
            raise Exception('There is a cycle!! Cannot make proper course list')
        if (course not in visited):
            visiting.add(course)
            for c in courseList[course]:
                visiting, visited, result = build_course_list(c, courseList, visiting, visited, result)
            visited.add(course)
            visiting.remove(course)
            result.append(course)
        return visiting, visited, result

    visiting = set()
    visited = set()
    result = []
    if not courseList or len(courseList) == 0:
        return result
    for k, v in courseList.items():
        if k not in visited:
            try:
                visiting, visitied, result = build_course_list(k, courseList, visiting, visited, result)
            except Exception as e:
                print(e)
                return None
    return result


class Daily_Coding_Problem_Test(unittest.TestCase):
    def test_case_1(self):
        preReqs = {
            'CSC100': [],
            'CSC200': [],
            'CSC300': []
        }
        expected = ['CSC100', 'CSC200', 'CSC300']
        self.assertEqual(getCourseOrder(preReqs), expected)

    def test_case_2(self):
        preReqs = {
            'CSC300': ['CSC100', 'CSC200'],
            'CSC200': ['CSC100'],
            'CSC100': []
        }
        expected = ['CSC100', 'CSC200', 'CSC300']
        self.assertEqual(getCourseOrder(preReqs), expected)

    def test_case_3(self):
        preReqs = {
            'CSC400': ['CSC200'],
            'CSC300': ['CSC100', 'CSC200'],
            'CSC200': ['CSC100'],
            'CSC100': []
        }
        expected = ['CSC100', 'CSC200', 'CSC400', 'CSC300']
        self.assertEqual(getCourseOrder(preReqs), expected)

    def test_case_4(self):
        preReqs = {
            'CSC400': ['CSC300'],
            'CSC300': ['CSC100', 'CSC200'],
            'CSC200': ['CSC100'],
            'CSC100': ['CSC400']
        }
        self.assertIsNone(getCourseOrder(preReqs))

if __name__ == '__main__':

    unittest.main()
