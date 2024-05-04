class YCF:
    __ycf: bool = True

    @staticmethod
    def runningOutside():
        YCF.__ycf = False
        print("running outside YFC")

    @staticmethod
    def isOutside() -> bool:
        return YCF.__ycf is False
