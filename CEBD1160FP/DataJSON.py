# This is a module that contains all the data format storage types


class csvNameEntry:
    def __init__(self):
        self.mState = None
        self.mSex = None
        self.mYear = None
        self.mName = None
        self.mCount = None

    def reset(self):
        self.mState = None
        self.mSex = None
        self.mYear = None
        self.mName = None
        self.mCount = None

    def parseCSVstring(self, entry):
        wArray = entry.split(",")
