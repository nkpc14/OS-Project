# Universal Class for the Main Timer and Premption
class Universal:
    UniversalTimer = 0
    PREEMPTION = list()
    STUDENT_AVAILABLE = False

# Queue to Hold the process
class Queue:
    def __init__(self):
        self.queue = list()
    # Method To add Process to Queue
    def addProcess(self, process):
        self.queue.append(process)
    # Method to pop process form the Queue
    def popProcess(self):
        return self.queue.pop()
    # Method ot get the list of objects in the Queue
    def getQueue(self):
        return self.queue

# Management class To manage the MainTimer
# MainTimer take care of the Whole Time process
class ManagementClass:
    def __init__(self):
        self.mainTimer = 0
    # Method to get the Main Timer
    def getTimer(self):
        return self.mainTimer
    # Method to Increment the Main Timer
    def incrementTimer(self):
        self.mainTimer += 1
        Universal.UniversalTimer = self.mainTimer

# Process class to Create object of each process
class Process:
    # Process Creation Class
    def __init__(self):
        self.process_name = ""
        self.arrival_time = 0
        self.burst_time = 0
        self.completion_time = 0
        self.remainingTime = 0
        self.waitingTime = 0
        self.turnAroundTime = 0
        self.startTime = self.arrival_time
        self.endTime = 0
        self.priority = 1

    # This is to get the name which we call any object in print
    def __str__(self):
        return str(self.arrival_time)
    # Method to Create the Object of the process
    def createProcess(self, process_name, arrival_time, burst_time, priority):
        self.process_name = process_name
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)
        self.remainingTime = self.burst_time
        self.priority = int(priority)

# Class to handel complete Process Execution Process creation API
class FacultyQueryManagement:
    # QueryManagement class to handel Query
    # Constructor to provide the initial values
    def __init__(self):
        # Initializing default values
        self.count = 0
        self.quantum_time = 2
        self.facultyProcess = list()
        self.Time = 0
        self.no_of_process = 0
        self.processQueue = list()
        self.executedProcess = list()
        self.length = 0
        self.startLength = len(self.facultyProcess)

    # Method which ask the user and creates N number of process
    def createProcesses(self):
        N = int(input("Enter the number of process you want to create"))
        for _ in range(N):
            process = Process()
            process.createProcess(
                input("Enter the Name of the Process: "),
                input("Enter the Arrival Time of the Process: "),
                input("Enter the Burst Time of the Process: "),
                input("Add to :\n0.Faculty Queue\n1.Student Queue")
            )
            self.facultyProcess.append(process)

    # Method to print all the process present in the facultyQueue
    def printProcessList(self):
        for process in self.facultyProcess:
            print("PRINTING PROCESS")
            print(process.process_name)
            print("Remaining Time: " + str(process.remainingTime))
            print("Arrival Time: " + str(process.arrival_time))
            print("PRIORITY: " + str(process.priority))

    # Method to get the Turn Around Time
    def getTurnAroundTime(self):
        for process in self.executedProcess:
            process.turnAroundTime = process.burst_time + process.waitingTime

    # Method to check if the Queue is empty or NOT
    def checkEmpty(self):
        if len(self.facultyProcess) == 0:
            print("Faculty  empty")
            return True
        else:
            print("Faculty not empty")
            return False

    # Method to get the Average Waiting Time and Average Turn Around Time
    def getAverageTime(self):
        # This class the Stating of the Exection of the processs
        self.startExecution()
        # This calculate the Turn Around Time
        self.getTurnAroundTime()

        # Initial values to 0
        totalWaitingTime = 0
        totalTurnAroundTime = 0

        # After the exection
        # Process present in the Exection Queue are fetched
        for process in self.executedProcess:
            totalWaitingTime += process.waitingTime
            totalTurnAroundTime += process.turnAroundTime
            print(
                " " + process.process_name + " " + str(process.burst_time) + " " + str(process.waitingTime) + " " + str(
                    process.turnAroundTime))
        print("Average Waiting Time = ", (totalWaitingTime / self.startLength))
        print("Average Turn Around Time = ", (totalTurnAroundTime / self.startLength))

    # This is to check the length of the process queue
    # To check if any process is present in the process Queue
    def checkProcessQueue(self):
        if len(self.processQueue) == 0:
            return True
        else:
            return False

    # Method to calculate the Waiting Time
    def getWaitingTimeMain(self):
        temp = None
        self.createProcesses()
        mainTimer = ManagementClass()
        print("Main Timer First: " + str(mainTimer.mainTimer))
        self.length = len(self.facultyProcess)

        # Sorting the list at ArrivalTime
        self.facultyProcess.sort(key=lambda x: (x.arrival_time, x.priority), reverse=False)
        # self.facultyProcess.sort(key=lambda x: x.priority, reverse=False)
        # self.printProcessList()
        # Copying the Burst Time to Remaining Time of each process
        for process in self.facultyProcess:
            process.remaining = process.burst_time

        while self.checkEmpty():
            print("Main Timer While: " + str(mainTimer.mainTimer))
            # Checking if the Process Queue is empty
            if self.checkProcessQueue():

                # Add one process from Faculty Queue to Process Queue
                self.processQueue.append(self.facultyProcess.pop(0))

                for process in self.processQueue:

                    # If mainTimer is greater than arrivalTime than the process has come
                    if mainTimer.mainTimer >= process.arrival_time:

                        # Check if the process is remaining to be executed
                        if process.remainingTime > 0:

                            # if process remainingTime is greater than quantumTime
                            if process.remainingTime >= self.quantum_time:

                                # keep incrementing the mainTimer
                                for _ in range(self.quantum_time):
                                    mainTimer.incrementTimer()
                                process.remainingTime -= self.quantum_time

                                temp = self.facultyProcess[0]
                                if not (mainTimer.mainTimer >= temp.arrival_time):
                                    pass
                            else:

                                for _ in range(process.remainingTime):
                                    mainTimer.incrementTimer()
                                process.waitingTime = mainTimer.mainTimer - process.burst_time
                                process.remainingTime = 0
                                self.executedProcess.append(self.processQueue.pop(0))
                        else:
                            # if the Burst Time was 0 Initially
                            # Then pop this process and Add it to Executed Queue
                            self.executedProcess.append(self.processQueue.pop(0))
                    else:
                        # if the mainTimer less than Arrival Time
                        # Then simply increment the mainTimer
                        mainTimer.incrementTimer()
            else:
                # if the Process Queue is Not Empty

                # Fetch a Process
                for process in self.processQueue:

                    # If mainTimer is greater than arrivalTime than the process has come
                    if mainTimer.mainTimer >= process.arrival_time:

                        # Check if the process is remaining to be executed
                        if process.remainingTime > 0:

                            # if process remainingTime is greater than quantumTime
                            if process.remainingTime >= self.quantum_time:

                                # keep incrementing the mainTimer
                                for _ in range(self.quantum_time):
                                    mainTimer.incrementTimer()
                                process.remainingTime -= self.quantum_time
                            else:

                                for _ in range(process.remainingTime):
                                    mainTimer.incrementTimer()
                                process.waitingTime = mainTimer.mainTimer - process.burst_time
                                process.remainingTime = 0
                                self.executedProcess.append(self.processQueue.pop(0))
                        else:
                            # if the Burst Time was 0 Initially
                            # Then pop this process and Add it to Executed Queue
                            self.executedProcess.append(self.processQueue.pop(0))
                    else:
                        # if the mainTimer less than Arrival Time
                        # Then simply increment the mainTimer
                        mainTimer.incrementTimer()
            mainTimer.incrementTimer()

    # This Method Starts the Exection
    def startExecution(self):
        self.length = len(self.facultyProcess)
        # Creating Process List
        print("Creating Process List")
        self.createProcesses()
        self.startLength = len(self.facultyProcess)
        mainTimer = ManagementClass()
        print("mainTimer Initial Value: " + str(mainTimer.mainTimer))
        print("Initial List")
        self.printProcessList()
        self.facultyProcess.sort(key=lambda x: (x.arrival_time, x.priority), reverse=False)
        print("Sorted List")
        self.printProcessList()

        while not self.checkEmpty():
            present_process = self.facultyProcess.pop(0)
            print("Popped +" + present_process.process_name)
            self.executeProcess(present_process, mainTimer)

    # Method to update the waiting time to the process
    def getWaitingTime(self, process):
        TAT = process.endTime - process.arrival_time
        print("ENDTIME: " + str(process.endTime))
        print("ARRIVAL TIME: " + str(process.arrival_time))
        process.waitingTime = TAT - process.burst_time
        print("UPDATING WAITING TIME: " + str(process.waitingTime))

    # Final Method which handles the Waiting Time in perefect way
    def executeProcess(self, process, mainTimer):
        while True:
            if mainTimer.mainTimer >= process.arrival_time:
                print("mainTimer.mainTimer >= process.arrival_time")
                if process.remainingTime > 0:
                    print("process.remainingTime > 0")
                    if process.remainingTime >= self.quantum_time:
                        print("process.remainTime >= self.quantum_time")
                        print("Incrementing mainTimer Quantum")
                        for _ in range(self.quantum_time):
                            mainTimer.incrementTimer()
                        print("Quantum mainTimer :" + str(mainTimer.mainTimer))
                        process.remainingTime -= self.quantum_time
                        print("Updated RemainingTime" + str(process.remainingTime))
                        if process.remainingTime == 0:
                            # process.waitingTime = mainTimer.mainTimer - process.burst_time
                            process.endTime = mainTimer.mainTimer
                            self.getWaitingTime(process)
                            self.executedProcess.append(process)
                    else:
                        for _ in range(process.remainingTime):
                            mainTimer.incrementTimer()
                        # process.waitingTime = mainTimer.mainTimer - process.burst_time
                        process.remainingTime = 0
                        print("Appending To Executed Process: " + str(process.process_name))
                        process.endTime = mainTimer.mainTimer
                        self.getWaitingTime(process)
                        self.executedProcess.append(process)
                else:
                    print("RemainingTime < 0 LOL!")
            else:
                print("mainTimer.mainTimer < process.arrival_time")
                mainTimer.incrementTimer()
                print("mainTimer value is :" + str(mainTimer.mainTimer))
            if not (self.length == 0):
                if self.stopAt(process, mainTimer, self.facultyProcess[0]):
                    break
            else:
                if not process.remainingTime == 0:
                    self.facultyProcess = [process] + self.facultyProcess
                break

    # Method which tells the CPU when to stop the Exection
    def stopAt(self, process, mainTimer, next_process):
        if (next_process.arrival_time <= mainTimer.mainTimer) and (next_process.priority <= process.priority):
            return True
        else:
            return False


if __name__ == "__main__":
    faculty = FacultyQueryManagement()
    # faculty.checkProcessQueue()
    faculty.getAverageTime()
