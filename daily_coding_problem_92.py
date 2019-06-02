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
                visiting, visited, result = build_course_list(k, courseList, visiting, visited, result)
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


'''
Bool version

# 
# Your previous Plain Text content is preserved below:
# 
# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#  
# Examples
# Example 1:
# Bool is_possible(number_of_courses, prerequisite_pairs):
# Input: 4, [[1,0], [1,2], [1,3]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# 
# 
# 1:
# 
# [1]
# 
# recur(0)
# 
# 0
# 
# visitingSet = Set()
# completedSet = Set()
# 
# prepprocess inputs
# dict()
# key: course number, val : list of courses
# 
def is_possible(courses, prereqs):
    if (not courses or not prereqs):
        return True

    visitingSet = set()
    completedSet = set()
  
  # lookup table
    prereq_dict = dict()
    for pair in prereqs:
        if pair[0] not in prereq_dict:
            prereq_dict[pair[0]] = [pair[1]]
        else:
            prereq_dict[pair[0]].append(pair[1])
  # instantaited dict
  
    # {1: [0]}
    # {0: [1]}
    for k, v in prereq_dict.items():
        if k not in completedSet:
      # go over each item in its values and do recursion
      
            valid_course_list = course_helper(k, prereq_dict, visitingSet, completedSet)
      
  # if visitedSet is empty and completed set is full then we can have a valid course list
    return valid_course_list and not visitingSet
    
def course_helper(course, prereq_dict, visitingSet, completedSet):
  
    if (course in visitingSet):
        return False
    is_valid = True
    if (course not in completedSet):
        visitingSet.add(course)
        for val in prereq_dict[course]:
            if val in prereq_dict:
                is_valid = course_helper(val, prereq_dict, visitingSet, completedSet)

        visitingSet.remove(course)
        completedSet.add(course)
    return is_valid
    
if __name__ == '__main__':
    assert is_possible(0, []) == True
    assert is_possible(2, [[1,0]]) == True
    assert is_possible(2, [[1,0], [0, 1]]) == False
    assert is_possible(4, [[1,0], [1,2], [1,3]] ) == True
    assert is_possible(3, [[1, 0], [1, 2], [0, 2]]) == True

'''
