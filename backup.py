# Sudesh Sharma is a Linux expert who wants to have an online system where he can handle student queries. Since there
# can be multiple requests at any time he wishes to dedicate a fixed amount of time to every request so that everyone
# gets a fair share of his time. He will log into the system from 10am to 12am only.  He wants to have separate
# requests queues for students and faculty. Implement a strategy for the same. The summary at the end of the session
# should include the total time he spent on handling queries and average query time.


class ManagementClass:
    def __init__(self):
        self.mainTimer = 0

    def incrementTimer(self):
        self.mainTimer += 1


class Process:
    # Process Creation Class
    def __init__(self):
        self.process_name = ""
        self.arrival_time = 0
        self.burst_time = 0
        self.completion_time = 0
        self.remaining = 0
        self.waitingTime = 0
        self.turnAroundTime = 0


# FACULTY QUERY


class FacultyQueryManagement(ManagementClass):
    # QueryManagement class to handel Query
    def __init__(self):
        super().__init__()
        # Initializing default values
        self.count = 0
        self.quantum_time = 2
        self.facultyProcess = list()
        self.Time = 0
        self.no_of_process = 0

    def getWaitingTime(self):
        # Copying the Burst Time into remaining time
        for process in self.facultyProcess:
            process.remaining = process.burst_time

        while True:
            # print("In Get Waiting Time function while loop")
            # done is to tell that process is done or not
            done = True
            # Traversing all process
            for process in self.facultyProcess:
                # print("Process Name: ", process.process_name, "is running")
                # If burst time of process is greater than 0
                # Then only process
                if process.remaining > 0:
                    done = False
                    # print("Process remaining time = ", process.remaining)
                    if process.remaining > self.quantum_time:
                        # Incrementing Time
                        self.Time += self.quantum_time

                        # Decrementing Burst time
                        process.remaining -= self.quantum_time
                    else:
                        # Increasing value of Time
                        # How much time process has been processed
                        self.Time = self.Time + process.remaining

                        # Waiting Time
                        process.waitingTime = self.Time - process.burst_time

                        # Fully Executed Process
                        process.remaining = 0
            if done:
                break

    # Turn Around Time
    def getTurnAroundTime(self):
        print("In Get Turn Around Time function")
        for process in self.facultyProcess:
            process.turnAroundTime = process.burst_time + process.waitingTime

    def getAverageTime(self):
        print("In Get Average Time function")
        self.getWaitingTime()
        self.getTurnAroundTime()
        print("Process Burst Time Waiting Time Turn Around Time")
        totalWaitingTime = 0
        totalTurnAroundTime = 0

        for process in self.facultyProcess:
            totalWaitingTime += process.waitingTime
            totalTurnAroundTime += process.turnAroundTime
            print(
                " " + process.process_name + " " + str(process.burst_time) + " " + str(process.waitingTime) + " " + str(
                    process.turnAroundTime))
        print("Average Waiting Time = ", (totalWaitingTime / len(self.facultyProcess)))
        print("Average Turn Around Time = ", (totalTurnAroundTime / len(self.facultyProcess)))

    def createProcess(self, name, arrival_time, burst_time):
        # createProcess method to create a process
        process = Process()
        process.process_name = name
        process.arrival_time = arrival_time
        process.burst_time = burst_time
        self.facultyProcess.append(process)

    def setTimeQuantum(self):
        # To initialize the Time Quantum
        self.quantum_time = int(input("Enter the Quantum TIme for Faculty Queue: "))

    def createProcessList(self):
        # To Create List of Process For the Faculty queue
        for count in range(self.no_of_process):
            print("Enter the details of Process" + str(count + 1))
            name = input("Process Name: ")
            arrival_time = int(input("Arrival Time: "))
            burst_time = int(input("Burst Time"))
            self.createProcess(name, arrival_time, burst_time)


class StudentQueryManagement(ManagementClass):
    # QueryManagement class to handel Query
    def __init__(self):
        # Initializing default values
        super().__init__()
        self.count = 0
        self.quantum_time = 2
        self.studentProcess = list()
        self.Time = 0
        self.no_of_process = 0

    def getWaitingTime(self):
        # Copying the Burst Time into remaining time
        print("In Get Waiting Time function")
        for process in self.studentProcess:
            process.remaining = process.burst_time

        while True:
            # print("In Get Waiting Time function while loop")
            done = True
            # Traversing all process
            for process in self.studentProcess:
                print("Procee Name: ", process.process_name, "is running")
                # If burst time of process is greater than 0
                # Then only process
                if process.remaining > 0:
                    done = False
                    print("Process remaining time = ", process.remaining)
                    if process.remaining > self.quantum_time:
                        # Incrementing Time
                        self.Time += self.quantum_time

                        # Decrementing Burst time
                        process.remaining -= self.quantum_time
                    else:
                        # Increasing value of Time
                        # How much time process has been processed
                        self.Time = self.Time + process.remaining

                        # Waiting Time
                        process.waitingTime = self.Time - process.burst_time

                        # Fully Executed Process
                        process.remaining = 0
            if done:
                break

    # Turn Around Time
    def getTurnAroundTime(self):
        print("In Get Turn Around Time function")
        for process in self.studentProcess:
            process.turnAroundTime = process.burst_time + process.waitingTime

    def getAverageTime(self):
        print("In Get Average Time function")
        self.getWaitingTime()
        self.getTurnAroundTime()
        print("Process Burst Time Waiting Time Turn Around Time")
        totalWaitingTime = 0
        totalTurnAroundTime = 0

        for process in self.studentProcess:
            totalWaitingTime += process.waitingTime
            totalTurnAroundTime += process.turnAroundTime
            print(
                " " + process.process_name + " " + str(process.burst_time) + " " + str(process.waitingTime) + " " + str(
                    process.turnAroundTime))
        print("Average Waiting Time = ", (totalWaitingTime / len(self.studentProcess)))
        print("Average Turn Around Time = ", (totalTurnAroundTime / len(self.studentProcess)))

    def createProcess(self, name, arrival_time, burst_time):
        # createProcess method to create a process
        process = Process()
        process.process_name = name
        process.arrival_time = arrival_time
        process.burst_time = burst_time
        self.studentProcess.append(process)

    def setTimeQuantum(self):
        self.quantum_time = int(input("Enter the Quantum TIme for Student Queue: "))

    def createProcessList(self):
        # To Create List of Process For the Student queue
        for count in range(self.no_of_process):
            print("Enter the details of Process" + str(count + 1))
            name = input("Process Name: ")
            arrival_time = int(input("Arrival Time: "))
            burst_time = int(input("Burst Time"))
            self.createProcess(name, arrival_time, burst_time)


class Access:
    # Access Class to check the time when to access
    def __init__(self):
        print("Our System will only work from 10 am to 12 am ")
        self.begin_time = input("Please Enter the Present Time:")
        self.end_time = 0

    def getStatus(self):
        if self.begin_time <= self.begin_time:
            return True
        else:
            return False


class Validation:
    def isPositiveInteger(self, data):
        if data < 0:
            print("Value Entered can't be Negative")
            return False

    def isZero(self, data):
        if data == 0:
            print("Value Entered can't be Zero")
            return False
        elif data <= 0:
            print("Value Entered can't be Negative")


if __name__ == "__main__":
    no_of_process = None
    print("Please choose a queue to post your query:")
    print("1. FACULTY queue")
    print("2. STUDENT queue")
    select_queue = int(input())
    if select_queue == 1:
        faculty = FacultyQueryManagement()
        faculty.no_of_process = int(input("Enter number of process for FACULTY queue:"))
        faculty.setTimeQuantum()
        faculty.createProcessList()
        faculty.getAverageTime()
    else:
        student = StudentQueryManagement()
        student.no_of_process = int(input("Enter number of process for Student queue:"))
        student.setTimeQuantum()
        student.createProcessList()
        student.getAverageTime()
