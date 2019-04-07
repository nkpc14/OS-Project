from collections import deque


class Queue:
    def __init__(self):
        self.queue = list()

    def addProcess(self, process):
        self.queue.append(process)

    def popProcess(self):
        return self.queue.pop()

    def getQueue(self):
        return self.queue


class ManagementClass:
    def __init__(self):
        self.mainTimer = 0

    def getTimer(self):
        return self.mainTimer

    def incrementTimer(self):
        self.mainTimer += 1


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
        self.startTime = 0
        self.endTime = 0

    def __str__(self):
        return str(self.arrival_time)

    def createProcess(self, process_name, arrival_time, burst_time):
        self.process_name = process_name
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)


class FacultyQueryManagement:
    # QueryManagement class to handel Query
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

    def createProcesses(self):
        N = int(input("Enter the number of process you want to create"))
        for _ in range(N):
            process = Process()
            process.createProcess(
                input("Enter the Name of the Process: "),
                input("Enter the Arrival Time of the Process: "),
                input("Enter the Burst Time of the Process: ")
            )
            self.facultyProcess.append(process)

    def printProcessList(self):
        for process in self.facultyProcess:
            print(process.process_name)

    def getTurnAroundTime(self):
        for process in self.facultyProcess:
            process.turnAroundTime = process.burst_time + process.waitingTime

    def checkEmpty(self):
        if len(self.facultyProcess) == 0:
            return False
        else:
            return True

    def getAverageTime(self):
        self.startExecution()
        self.getTurnAroundTime()

        totalWaitingTime = 0
        totalTurnAroundTime = 0

        for process in self.facultyProcess:
            totalWaitingTime += process.waitingTime
            totalTurnAroundTime += process.turnAroundTime
            print(
                " " + process.process_name + " " + str(process.burst_time) + " " + str(process.waitingTime) + " " + str(
                    process.turnAroundTime))
        print("Average Waiting Time = ", (totalWaitingTime / self.length))
        print("Average Turn Around Time = ", (totalTurnAroundTime / self.length))

    def getWaitingTime(self):
        self.createProcesses()
        mainTimer = ManagementClass()
        print("Main Timer First: " + str(mainTimer.mainTimer))
        self.length = len(self.facultyProcess)
        for process in self.facultyProcess:
            process.remaining = process.burst_time

        while self.checkEmpty():
            # done = True
            # incrementing Timer by 1

            # Fetching the process one by one

            for process in self.facultyProcess:
                # Fetched a process
                print("Main Timer for: " + str(mainTimer.mainTimer))
                # If mainTimer is greater than arrivalTime than the process has come
                if mainTimer.mainTimer >= process.arrival_time:
                    # now the process has come and start the execution of the process
                    print("Main timer: " + str(mainTimer.mainTimer))
                    print("Process AT: " + str(process.arrival_time))

                    # Check if the process is remaining to be executed
                    if process.remainingTime > 0:
                        # done = False

                        # if process remainingTime is greater than quantumTime
                        if process.remainingTime >= self.quantum_time:

                            # keep incrementing the mainTimer
                            for _ in range(self.quantum_time):
                                mainTimer.incrementTimer()
                                print("Main Timer if: " + str(mainTimer.mainTimer))
                            # And update the remainingTime
                            process.remainingTime -= self.quantum_time
                        else:
                            # if Process remainingTime is less than quantum time
                            # Means the process is in its last cycle of execution

                            # keep incrementing the mainTimer
                            for _ in range(process.remainingTime):
                                mainTimer.incrementTimer()
                                print("Main Timer else: " + str(mainTimer.mainTimer))
                            # Updating the Waiting Time
                            process.waitingTime = mainTimer.mainTimer - process.burst_time

                            # Update the Process remainingTime to 0
                            # Process has finished its execution
                            process.remainingTime = 0
                            # pop the process
                            self.facultyProcess.pop(self.facultyProcess.index(process))

            mainTimer.incrementTimer()
            print("Main Timer while: " + str(mainTimer.mainTimer))
            # if mainTimer.mainTimer > 150:
            #     break

    def checkProcessQueue(self):
        if len(self.processQueue) == 0:
            return True
        else:
            return True

    def processQueueExecution(self,process):
        pass

    def startExecution(self):
        temp = None
        self.createProcesses()
        mainTimer = ManagementClass()
        print("Main Timer First: " + str(mainTimer.mainTimer))
        self.length = len(self.facultyProcess)

        # Sorting the list at ArrivalTime
        self.facultyProcess.sort(key=lambda x: x.arrival_time, reverse=False)
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


if __name__ == "__main__":
    faculty = FacultyQueryManagement()
    # faculty.checkProcessQueue()
    faculty.getAverageTime()
