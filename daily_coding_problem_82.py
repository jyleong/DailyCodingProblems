'''
Using a read7() method that returns 7 characters from a file, 
implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, 
three read7() returns “Hello w”, “orld” and then “”.
'''

class FileClass(object):

    def __init__(self, file): # string
        self.content = file
        self.ptr = 0
        self.cur_buffer = ""

    def read_7(self):
        content = ""
        if (len(self.cur_buffer) > 0):
            content += self.cur_buffer
            bufLen = len(self.cur_buffer)
            self.cur_buffer = ""
            end = min(self.ptr+7-bufLen, len(self.content))
            content += self.content[self.ptr:end]
            self.ptr = end
        else:
            end = min(self.ptr+7, len(self.content))
            content = self.content[self.ptr:end]
            self.ptr = end

        return content

    def read_n(self, n):
        c = ""
        bufLen = 0
        if (len(self.cur_buffer) > 0):
            c += self.cur_buffer
            bufLen = len(self.cur_buffer)
            self.cur_buffer = ""
            # use read_7 then minus the bufLen
        while len(c) < n:
            more_chars = self.read_7()
            if (not more_chars):
                break
            c += more_chars
            print("read_n() self.ptr: ", self.ptr)
            print("read_n(): c ", c)
        
        self.cur_buffer = c[n-bufLen:]
        c = c[:n-bufLen]
        return c

fp = FileClass("Hello world")
assert fp.read_7() == "Hello w"
n = fp.read_7()
assert n == "orld"
assert fp.read_7() == ""

fp = FileClass("Hello world")
assert fp.read_n(8) == "Hello wo"
assert fp.read_n(8) == "rld"

fp = FileClass("Hello world")
assert fp.read_n(4) == "Hell"
assert fp.read_7() == "o world"