'''
Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].
'''

import unittest

def generate_ip_addresses(digits):
    result = []
    def ip_addr_helper(digits, idx, valid_addresses, addr):
        if len(addr) > 4:
            return
        if (len(addr) == 4 and idx == len(digits)):
            ip_addr = ".".join([str(x) for x in addr])
            valid_addresses.append(ip_addr)
            return

        for i in range(1,4):
            if idx + i <= len(digits):
                subnet = digits[idx: idx + i]
                if len(subnet) > 1 and subnet[0] == '0':
                    continue
                subnet = int(digits[idx: idx + i])
                if 0 <= subnet and subnet <= 255:
                    # add to current address
                    # recurse
                    ip_addr_helper(digits, idx + i, valid_addresses, addr + [subnet])
    if not digits or len(digits) == 0 \
            or len(digits) > 12:
        return result

    ip_addr_helper(digits, 0, result, [])

    return result

class DailyCodingProblemTest(unittest.TestCase):

    def test_case_1(self):
        test = '2542540123'
        expected = ['254.25.40.123', '254.254.0.123']
        actual = generate_ip_addresses(test)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        test = '2542560123'
        expected = ['254.25.60.123']
        actual = generate_ip_addresses(test)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        test = ''
        expected = []
        actual = generate_ip_addresses(test)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        test = '254254254233221'
        expected = []
        actual = generate_ip_addresses(test)
        self.assertEqual(actual, expected)

if __name__ == '__main__':

    unittest.main()

