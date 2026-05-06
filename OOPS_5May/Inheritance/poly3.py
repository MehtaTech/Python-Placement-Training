
class Institution:
    __institutionid = 0
    __institutionname = ""
    __noofstudentsplaced = 0
    __noofstudentscleared = 0
    __location = ""
    __grade = ""

    def __init__(self,institutionid,institutionname,noofstudentsplaced,noofstudentscleared,location,grade):
        self.__institutionid = institutionid
        self.__institutionname = institutionname
        self.__noofstudentsplaced = noofstudentsplaced
        self.__noofstudentscleared = noofstudentscleared
        self.__location = location


        # geter
        def getinstitutionid(self):
            return self.__institutionid
        def getinstitutionname(self):
            return self.__institutionname
        def getnoofstudentsplaced(self):
            return self.__noofstudentsplaced
        def getnoofstudentscleared(self):
            return self.__noofstudentscleared
        def getlocation(self):
            return self.__location

        # Setter
        def setinstitutionid(self, institutionid):
            self.__institutionid = institutionid

        def setinstitutionname(self, institutionname ):
            self.__institutionname = institutionname

        def setnoofstudentsplaced(self, noofstudentsplaced):
            self.__noofstudentsplaced = noofstudentsplaced

        def setnoofstudentscleared(self, noofstudentcleared):
            self.__noofstudentscleared = noofstudentcleared

        def setlocation(self, location):
            self.__location = location
        

            
            
class Solution:
    @staticmethod
    def FindNumClearancedByLoc(institutions, location):
        total_cleared = 0
        for inst in institutions:
            if inst.getlocation() == location:   # check location
                total_cleared += inst.getnoofstudentscleared()
                return total_cleared


