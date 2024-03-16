from datetime import date
from datetime import datetime


class Cooperative():  # Populates Cooperative Class as stated in TMA
    _course = {'C001': ('Gluten-Free', 'How to start a gluten-free diet', '100', 0), 'E012': (
    'Engineering In Business', 'Development and implementation of business solutions', '10000', 'Engineering')}
    _scheduledCourses = {('12 Oct 2019', 'C001'): ('C001', '12 Oct 2019'),
                         ('12 Oct 2019', 'E012'): ('E012', '12 Oct 2019')}
    _members = {1: (1, 'Helen', 11111111, '01 Jan 1964', '1000', 55),
                2: (2, 'Irene', 22222222, '01 Oct 1949', 'not disclosed', 69),
                3: (3, 'Jackson', 33333333, '01 Mar 1959', '2500', 60),
                4: (4, 'Kendrick', 44444444, '01 Nov 1979', '1000', 39)}

    @property
    def memberStr(self):
        for key, value in Cooperative._members.items():
            print("ID: " + str(key),
                  Member(Cooperative._members[key][1], Cooperative._members[key][2], Cooperative._members[key][3],
                         Cooperative._members[key][4]))

    def coursesStr(self):
        for key, value in Cooperative._course.items():
            if Cooperative._course[key][3] in VocationalCourse.specialisedIndustries:
                print(VocationalCourse(key, Cooperative._course[key][0], Cooperative._course[key][1],
                                       Cooperative._course[key][2], Cooperative._course[key][3]))
            if Cooperative._course[key][3] == 0:
                print(NonVocationalCourse(key, Cooperative._course[key][0], Cooperative._course[key][1],
                                          Cooperative._course[key][2]))

    def scheduledCoursesStr(self):
        for key, value in ScheduledCourse._ScheduledCourse.items():
            if ScheduledCourse._ScheduledCourse[key][3] in VocationalCourse.specialisedIndustries:
                print(ScheduledCourse(Cooperative._scheduledCourses[key][0], Cooperative._scheduledCourses[key][1]))
                print(
                    VocationalCourse(ScheduledCourse._ScheduledCourse[key][4], ScheduledCourse._ScheduledCourse[key][0],
                                     ScheduledCourse._ScheduledCourse[key][1], ScheduledCourse._ScheduledCourse[key][2],
                                     ScheduledCourse._ScheduledCourse[key][3]))
                if (len(ScheduledCourse._participantList)) != 0:
                    print("HERE")
                    print("Participant List: ")
                    for ParticipantList in ScheduledCourse._participantList:
                        print("ID: " + str(ParticipantList[0]),
                              Member(ParticipantList[1], ParticipantList[2], ParticipantList[3], ParticipantList[4]),
                              "Age: " + str(ParticipantList[5]))
                    print("Number of Participants: " + str(len(ScheduledCourse._participantList)))
                elif (len(ScheduledCourse._participantList)) == 0:
                    print("Participant List: " + "\n" + "\n" + "Number of Participants: " + str(
                        len(ScheduledCourse._participantList)))
            if ScheduledCourse._ScheduledCourse[key][3] == 0:
                print(ScheduledCourse(Cooperative._scheduledCourses[key][0], Cooperative._scheduledCourses[key][1]))
                print(NonVocationalCourse(ScheduledCourse._ScheduledCourse[key][4],
                                          ScheduledCourse._ScheduledCourse[key][0],
                                          ScheduledCourse._ScheduledCourse[key][1],
                                          ScheduledCourse._ScheduledCourse[key][2]))
                if (len(ScheduledCourse._participantListNon)) != 0:
                    print("Participant List: ")
                    for ParticipantList in ScheduledCourse._participantListNon:
                        print("ID: " + str(ParticipantList[0]),
                              Member(ParticipantList[1], ParticipantList[2], ParticipantList[3], ParticipantList[4]),
                              "Age: " + str(ParticipantList[5]))
                    print("Number of Participants: " + str(len(ScheduledCourse._participantListNon)))
                elif (len(ScheduledCourse._participantListNon)) == 0:
                    print("Participant List: " + "\n" + "\n" + "Number of Participants: " + str(
                        len(ScheduledCourse._participantListNon)))

    def AddMember(self):
        UserMemberName = input('Enter name: ')
        while True:
            try:
                UserMemberContact = int(input('Enter contact: '))
                break
            except:
                print("That's not a valid option!")
        while True:
            UserMemberDOB = input('Enter date of birth in d/m/yyyy format: ')
            try:
                UserMemberDOB = datetime.strptime(UserMemberDOB, '%d/%m/%Y')
            except ValueError:
                print("Please enter date in d/m/yyyy format")
                continue
            else:
                break
        newformat = UserMemberDOB.strftime('%d %b %Y')
        UserMemberDOB = newformat
        while True:
            UserMemberIncome = input('Enter monthly income to nearest whole number or <ENTER> if not disclosing: ')
            try:
                val = int(UserMemberIncome)
                print("Add Member operation is successful")
                break
            except:
                if UserMemberIncome == "":
                    UserMemberIncome = "not disclosed"
                    print("Add Member operation is successful")
                    break
            finally:
                if UserMemberIncome == ValueError:
                    print("That's not a Valid Option")

        UserAge = datetime.strptime(UserMemberDOB, '%d %b %Y')
        UserAge = Member.calculateAge(UserAge)
        for key in Cooperative._members.keys():
            Member._nextId = (len(Cooperative._members.keys()))
            Member._nextId += 1
            Cooperative._members[
                Member._nextId] = Member._nextId, UserMemberName, UserMemberContact, newformat, UserMemberIncome, UserAge
            break

    def AddCourse(self):
        while True:
            UserCourseVocational = input('Enter V to add vocational Course or N to add non-vocational Course: ')
            if UserCourseVocational == "V" or UserCourseVocational == "v":
                while True:
                    UserCourseCode = input('Enter Course Code: ')
                    if UserCourseCode not in Cooperative._course.keys():
                        break
                    elif UserCourseCode in Cooperative._course.keys():
                        print("Duplicate course code " + UserCourseCode)
                        continue
                UserCourseTitle = input('Enter title: ')
                UserCourseDescription = input('Enter description: ')
                while True:
                    UserCourseFee = input('Enter fees: ')
                    try:
                        val = int(UserCourseFee)
                        break
                    except ValueError:
                        print("Please enter whole number")
                UserCourseIndustry = input('Enter industry: ')
                Cooperative._course[
                    UserCourseCode] = UserCourseTitle, UserCourseDescription, UserCourseFee, UserCourseIndustry
                print("Add Course Operation is successful")
                break
            elif UserCourseVocational == "N" or UserCourseVocational == "n":
                while True:
                    UserCourseCode = input('Enter Course Code: ')
                    if UserCourseCode not in Cooperative._course.keys():
                        break
                    elif UserCourseCode in Cooperative._course.keys():
                        print("Duplicate course code " + UserCourseCode)
                        continue
                UserCourseTitle = input('Enter title: ')
                UserCourseDescription = input('Enter description: ')
                while True:
                    UserCourseFee = input('Enter fees: ')
                    try:
                        val = int(UserCourseFee)
                        break
                    except ValueError:
                        print("Please enter whole number")
                UserCourseIndustry = 0
                Cooperative._course[
                    UserCourseCode] = UserCourseTitle, UserCourseDescription, UserCourseFee, UserCourseIndustry
                print("Add Course Operation is successful")
                break
            else:
                print("Please Enter V or N")
                continue

    def AddSchedule(self):
        UserScheduleCode = input("Enter Course Code: ")
        if UserScheduleCode in Cooperative._course.keys():
            while True:
                UserScheduleDate = input("Enter Schedule date in d/m/yyyy format: ")
                try:
                    UserScheduleDate = datetime.strptime(UserScheduleDate, '%d/%m/%Y')
                except ValueError:
                    print("Please enter date in d/m/yyyy format")
                    continue
                else:
                    break
            newformat = UserScheduleDate.strftime('%d %b %Y')
            UserScheduleDate = newformat
            if (UserScheduleDate, UserScheduleCode) not in Cooperative._scheduledCourses.keys():
                Cooperative._scheduledCourses[UserScheduleDate, UserScheduleCode] = UserScheduleCode, UserScheduleDate
                AppendScheduleCourse = (Cooperative._course).get(UserScheduleCode)
                AppendScheduleCourse = list(AppendScheduleCourse)
                AppendScheduleCourse.append(UserScheduleCode)
                ScheduledCourse._ScheduledCourse[UserScheduleDate, UserScheduleCode] = AppendScheduleCourse
                print("Add Schedule operation is successful")
            else:
                print("Duplicate Schedule Date found, Please Try again")

    def EnrollMember(self, mid, code, scheduleDate):
        if mid not in ScheduledCourse._participantList:
            ScheduledCourse._participantList.append(mid)
        else:
            print("Already in List!")
            return UserAns
        for sublist in ScheduledCourse._participantList:
            getCourse = Cooperative._course.get(UserCourseCodeSearch)
            if getCourse[3] in VocationalCourse.specialisedIndustries:
                getCourseFee = getCourse[2]
                getCourseFee = int(getCourseFee)
                UserAge = sublist[5]
                UserIncome = sublist[4]
                if UserIncome == str("not disclosed"):
                    Subsidy = 0
                    Payment = getCourseFee
                    print("ID: " + str(mid[0]), Member(mid[1], mid[2], mid[3], mid[4]))
                    print("Course Fee:$ " + str(getCourseFee) + " Subsidy:$ " + str(Subsidy) + " Payment:$ " + str(
                        Payment))
                    print("Enroll operation is successful")
                    return UserAns
                if UserIncome != str("not disclosed"):
                    CalculateSubsidy = VocationalCourse.getSubsidy(self, UserIncome, UserAge)
                    Subsidy = (getCourseFee / 100) * CalculateSubsidy
                    Payment = getCourseFee - ((getCourseFee / 100) * CalculateSubsidy)
                    print("ID: " + str(mid[0]), Member(mid[1], mid[2], mid[3], mid[4]))
                    print("Course Fee:$ " + str(getCourseFee) + " Subsidy:$ " + str(Subsidy) + " Payment:$ " + str(
                        Payment))
                    print("Enroll operation is successful")
                    return UserAns
            elif getCourse[3] == 0:
                getCourseFee = getCourse[2]
                getCourseFee = int(getCourseFee)
                UserAge = sublist[5]
                UserIncome = sublist[4]
                if UserIncome == str("not disclosed"):
                    Subsidy = 0
                    Payment = getCourseFee
                    print("ID: " + str(mid[0]), Member(mid[1], mid[2], mid[3], mid[4]))
                    print("Course Fee:$ " + str(getCourseFee) + " Subsidy:$ " + str(Subsidy) + " Payment:$ " + str(
                        Payment))
                    print("Enroll operation is successful")
                    ScheduledCourse._participantList.remove(SearchMember)
                    ScheduledCourse._participantListNon.append(SearchMember)
                    return UserAns
                if UserIncome != str("not disclosed"):
                    UserIncome = int(UserIncome)
                    CalculateSubsidy = NonVocationalCourse.getSubsidy(self, UserIncome, UserAge)
                    Subsidy = (getCourseFee / 100) * CalculateSubsidy
                    Payment = getCourseFee - ((getCourseFee / 100) * CalculateSubsidy)
                    print("ID: " + str(mid[0]), Member(mid[1], mid[2], mid[3], mid[4]))
                    print("Course Fee:$ " + str(getCourseFee) + " Subsidy:$ " + str(Subsidy) + " Payment:$ " + str(
                        Payment))
                    print("Enroll operation is successful")
                    ScheduledCourse._participantList.remove(SearchMember)
                    ScheduledCourse._participantListNon.append(SearchMember)
                    return UserAns

    def CancelEnrollment(self, mid, code, scheduleDate, cancelDate):
        while True:
            mid = ScheduledCourse.searchParticipant(self, mid)
            if mid == 0:
                print("User ID not Found")
                continue
            if mid != 0:
                break
        delta = scheduleDate - cancelDate
        CancelDays = delta.days
        CancelDays = int(delta.days)
        CancellationRate = Course.CancellationPenaltyRate(self, CancelDays)
        getCourse = Cooperative._course.get(code)
        if getCourse[3] in VocationalCourse.specialisedIndustries:
            for sublist in ScheduledCourse._participantList:
                getCourseFee = getCourse[2]
                getCourseFee = int(getCourseFee)
                UserAge = sublist[5]
                UserIncome = sublist[4]
                CancellationRate = CancellationRate + 0.1
                if UserIncome == str("not disclosed"):
                    Subsidy = 0
                    Payment = getCourseFee
                    Penalty = Payment * CancellationRate
                    print("ID: " + str(mid[0]), Member(mid[1], mid[2], mid[3], mid[4]))
                    print("Course Fee:$ " + str(getCourseFee) + " Subsidy:$ " + str(Subsidy) + " Payment:$ " + str(
                        Payment))
                    print("Enroll operation is successful")
                    ScheduledCourse._participantList.remove(sublist)
                    return UserAns
                if UserIncome != str("not disclosed"):
                    CalculateSubsidy = VocationalCourse.getSubsidy(self, UserIncome, UserAge)
                    Subsidy = (getCourseFee / 100) * CalculateSubsidy
                    Payment = getCourseFee - ((getCourseFee / 100) * CalculateSubsidy)
                    Penalty = Payment * CancellationRate
                    print("ID: " + str(mid[0]), Member(mid[1], mid[2], mid[3], mid[4]))
                    print("Course Fee:$ " + str(getCourseFee) + " Subsidy:$ " + str(Subsidy) + " Payment:$ " + str(
                        Payment))
                    print("Penalty Rate: " + str(CancellationRate), "%", " Penalty Amount: " + str(Penalty))
                    print("Enroll operation is successful")
                    ScheduledCourse._participantList.remove(sublist)
                    return UserAns
        elif getCourse[3] == 0:
            for sublist in ScheduledCourse._participantListNon:
                getCourseFee = getCourse[2]
                getCourseFee = int(getCourseFee)
                UserAge = sublist[5]
                UserIncome = sublist[4]
                CancellationRate = CancellationRate + 0.1
                if UserIncome == str("not disclosed"):
                    Subsidy = 0
                    Payment = getCourseFee
                    Penalty = Payment * CancellationRate
                    print("ID: " + str(mid[0]), Member(mid[1], mid[2], mid[3], mid[4]))
                    print("Course Fee:$ " + str(getCourseFee) + " Subsidy:$ " + str(Subsidy) + " Payment:$ " + str(
                        Payment))
                    print("Enroll operation is successful")
                    ScheduledCourse._participantListNon.remove(sublist)
                    return UserAns
                if UserIncome != str("not disclosed"):
                    UserIncome = int(UserIncome)
                    CalculateSubsidy = NonVocationalCourse.getSubsidy(self, UserIncome, UserAge)
                    Subsidy = (getCourseFee / 100) * CalculateSubsidy
                    Payment = getCourseFee - ((getCourseFee / 100) * CalculateSubsidy)
                    Penalty = Payment * CancellationRate
                    print("ID: " + str(mid[0]), Member(mid[1], mid[2], mid[3], mid[4]))
                    print("Course Fee:$ " + str(getCourseFee) + " Subsidy:$ " + str(Subsidy) + " Payment:$ " + str(
                        Payment))
                    print("Penalty Rate: " + str(CancellationRate), "%", " Penalty Amount: " + str(Penalty))
                    print("Enroll operation is successful")
                    ScheduledCourse._participantListNon.remove(sublist)
                    return UserAns

    def getMember(self, mid):
        key = list(Cooperative._members.keys())
        if mid in key:
            return Cooperative._members.get(mid)
        elif mid not in key:
            print("No member with member id " + str(mid))
            return False

    def getCourse(self, code):
        if code not in Cooperative._course.keys():
            print("No Course with code " + code)
            return False
        elif code in Cooperative._course.keys():
            return True

    def getScheduledCourse(self, code, scheduleDate):
        key = list(Cooperative._scheduledCourses.keys())
        if (scheduleDate, code) not in key:
            print("No Schedule for course with code " + code + "on " + scheduleDate)
            return False
        elif (scheduleDate, code) in key:
            return True


class CooperativeException(Exception):
    pass


class Member():
    _nextId = 1

    def __init__(self, name, contact, dob, monthlyincome=None):
        self.name = name
        self.contact = contact
        self.dob = dob
        self.monthlyincome = monthlyincome
        self.id = id
        Member._nextId = self.id

    def calculateAge(birthDate):  # Method to Calculate Age
        today = date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        return age

    def mid(self):
        return self.mid

    def __str__(self):
        return " Name: " + self.name + "      Contact: " + str(self.contact) + " Monthly Income:$ " + str(
            self.monthlyincome) + " Date of Birth: " + str(self.dob)


class Course():
    baseCancellationPenaltyRate = 0.3

    def __init__(self, courseCode, title, description, fees):
        self.courseCode = courseCode
        self.title = title
        self.description = description
        self.fees = fees

    def CancellationPenaltyRate(self, days):  # Method to calculate Penalty based on number of days
        if days > 7:
            CancelRate = 0
        if days < 7 and days > 4:
            CancelRate = 0.15
        else:
            CancelRate = 0.3
        return CancelRate

    def courseCode(self):
        return self.courseCode

    def fees(self):
        self.fees = format(self.fees, '.2f')
        return self.fees

    def __str__(self):
        return "Course Code: " + str(self.courseCode) + " Title: " + self.title + " Fees:$" + str(
            self.fees) + "\n" + "     Description: " + self.description


class VocationalCourse(Course):
    cancellationPenaltyAddRate = 0.1
    specialisedIndustries = ['Engineering', 'Electronics', 'Computing']

    def __init__(self, courseCode, title, description, fees, industry):  # Subclass for Course
        super().__init__(courseCode, title, description, fees)
        self.Industries = industry

    def getSubsidy(self, income, age):
        if age >= 55 and age < 60:
            Subsidy = 90
        if age > 60:
            Subsidy = 95
        if age < 55:
            Subsidy = 80
        return Subsidy

    def __str__(self):
        return "Vocational Course Code: " + str(self.courseCode) + " Title: " + self.title + " Fees:$" + str(
            self.fees) + "\n" + "     Description: " + self.description + " Industry: " + self.Industries


class NonVocationalCourse(Course):
    def __init__(self, courseCode, title, description, fees):  # Subclass for Course
        super().__init__(courseCode, title, description, fees)

    def getSubsidy(self, income, age):
        if age >= 55 and income < 1200:
            Subsidy = 50
        else:
            Subsidy = 0
        return Subsidy

    def __str__(self):
        return "Non Vocational Course Code: " + str(self.courseCode) + " Title: " + self.title + " Fees:$ " + str(
            self.fees) + "\n" + "     Description: " + self.description + "\n"


class ScheduledCourse(Member, Course, Cooperative):
    _participantList = []
    _participantListNon = []
    _scheduleDate = ()
    _ScheduledCourse = {('12 Oct 2019', 'C001'): ['Gluten-Free', 'How to start a gluten-free diet', '100', 0, 'C001'],
                        ('12 Oct 2019', 'E012'): ['Engineering In Business',
                                                  'Development and implementation of business solutions', '10000',
                                                  'Engineering', 'E012']}

    def __init__(self, course, scheduleDate):
        self.course = course
        self.scheduleDate = scheduleDate

    def course(self):
        return self.course

    def scheduleDate(self):
        today = date.today()
        return today

    def searchParticipant(self, mid):  # Method to search for Participant in list
        search_participant = Cooperative._members.get(mid)
        if search_participant not in ScheduledCourse._participantList:
            participant = 0
        if search_participant in ScheduledCourse._participantList:
            participant = list(search_participant)
        if search_participant in ScheduledCourse._participantListNon:
            participant = list(search_participant)
        return participant

    def __str__(self):
        return "Scheduled Date: " + str(self.scheduleDate)


obj = Cooperative()
UserAns = True
while UserAns:

    print("""   
                Menu
                1. List Members
                2. List Courses
                3. List Schedules
                4. Add Member
                5. Add Course
                6. Add Schedule
                7. Enroll Member
                8. Cancel Enrollment
                0. Exit
                """)
    UserAns = input('Enter choice: ')
    if UserAns == "1":  # Option 1 shows the current members
        obj.memberStr
    if UserAns == "2":  # Option 2 shows the current courses
        obj.coursesStr()
    if UserAns == "3":  # Option 3 shows the current scheduled courses
        obj.scheduledCoursesStr()
    if UserAns == "4":  # Option 4 allows user to add a member
        obj.AddMember()
    if UserAns == "5":  # Option 5 allows user to add a course
        obj.AddCourse()
    if UserAns == "6":  # Option 6 allows user to add a scheduled course
        obj.AddSchedule()
    if UserAns == "7":  # Option 7 allows user to enroll a participant for a scheduled course
        mid = input("Enter Member id: ")
        mid = int(mid)
        SearchMember = obj.getMember(mid)
        if SearchMember == False:
            continue
        UserCourseCodeSearch = input("Enter Course code: ")
        Search = obj.getCourse(UserCourseCodeSearch)
        if Search == False:
            continue
        while True:
            UserCourseScheduleSearch = input("Enter Schedule date in d/m/yyyy format: ")
            try:
                UserCourseScheduleSearch = datetime.strptime(UserCourseScheduleSearch, '%d/%m/%Y')
            except ValueError:
                print("Please enter date in d/m/yyyy format")
                continue
            else:
                break
        UserCourseScheduleSearch = UserCourseScheduleSearch.strftime('%d %b %Y')
        show = obj.getScheduledCourse(UserCourseCodeSearch, UserCourseScheduleSearch)
        if show == False:
            continue
        obj.EnrollMember(SearchMember, UserCourseCodeSearch, UserCourseScheduleSearch)
    if UserAns == "8":  # Option 8 allows user to cancel the enrollment of a participant for a scheduled course.
        UserIDCancelSearch = input("Enter Member id: ")
        UserIDCancelSearch = int(UserIDCancelSearch)
        UserCourseCancelSearch = input("Enter Course Code: ")
        Search = obj.getCourse(UserCourseCancelSearch)
        if Search == False:
            continue
        while True:
            UserCourseScheduleCancelSearch = input("Enter Schedule date in d/m/yyyy format: ")
            try:
                UserCourseScheduleCancelSearch = datetime.strptime(UserCourseScheduleCancelSearch, '%d/%m/%Y')
            except ValueError:
                print("Please enter date in d/m/yyyy format")
                continue
            else:
                break
        newformat = UserCourseScheduleCancelSearch.strftime('%d %b %Y')
        show = obj.getScheduledCourse(UserCourseCancelSearch, newformat)
        if show == False:
            continue
        while True:
            UserCourseScheduleCancelDate = input("Enter Cancel in d/m/yyyy format: ")
            try:
                UserCourseScheduleCancelDate = datetime.strptime(UserCourseScheduleCancelDate, '%d/%m/%Y')
            except ValueError:
                print("Please enter date in d/m/yyyy format")
                continue
            else:
                break
        obj.CancelEnrollment(UserIDCancelSearch, UserCourseCancelSearch, UserCourseScheduleCancelSearch,
                             UserCourseScheduleCancelDate)
    if UserAns == "0":  # Option 0 exits Program
        exit()
