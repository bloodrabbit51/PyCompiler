code = ""
testCaseStack = []
variableStack = []
teststepcount = 1

class testStart():
    def __init__(self,value):
        self.value = value
        self.put()
        self.push()

    def put(self):
        global code
        global teststepcount
        teststepcount = 1
        with open("data/starttestcase.cs") as fp:
            for line in fp:
                if("XTESTCASEXID" in line):
                    code = code + line.replace("XTESTCASEXID",str(self.value).replace("\"",""))
                else:
                    code = code + line
            code = code + "{\n"
    def push(self):
        global testCaseStack
        testCaseStack.append("START")

class testStop():
    def __init__(self,value):
        self.value = value
        self.put()
        self.pop()

    def put(self):
        global code
        code = code + "  return(APP_TC_PASSED);\n"
        code = code + "} /* End of " + str(self.value) + "  */\n"

    def pop(self):
        global testCaseStack
        testCaseStack.pop()

class TestDes():
    def __init__(self,value):
        self.value = value
        self.put()

    def put(self):
        global code
        code = code + "\n\n  /* Test Description */\n"
        code = code + "  " + str(self.value).replace("<","").replace(">","") + ";\n\n"

class TestRes():
    def __init__(self,inp,out,operator):
        self.inp = inp
        self.out = out
        self.operator = operator
        self.put()

    def put(self):
        global code
        global teststepcount
        code = code + " /* Expected Result - "+ str(teststepcount) + " */\n"
        code = code + "  App_GddTestStepId++;\n"
        code = code + "  if(" + str(self.inp).replace("<","").replace(">","") + self.operator + str(self.out).replace("<","").replace(">","") + ")\n"
        code = code + "  {\n    return(APP_TC_FAILED);\n  }\n\n"
        teststepcount = teststepcount + 1

class TestResSingle():
    def __init__(self,api,opr):
        self.api = api
        self.opr = opr
        self.put()

    def put(self):
        global code
        global teststepcount
        code = code + " /* Expected Result - " + str(teststepcount) + " */\n"
        code = code + "  App_GddTestStepId++;\n"
        code = code + "  if(" + self.opr + "(" + str(self.api).replace("<","").replace(">","") + "))\n"
        code = code + "  {\n    return(APP_TC_FAILED);\n  }\n\n"
        teststepcount = teststepcount + 1


class Codegen():
    def doit(self):
        global code
        return code


