class HelloOldWorld:
    def say_hi(self):
        print("Hello World")


class IhaveDunderAttributes(object):
    __this_should_trigger_pylint__ = True
