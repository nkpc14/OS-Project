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
        self.startTime = self.arrival_time
        self.endTime = 0

    def __str__(self):
        return str(self.arrival_time)

    def createProcess(self, process_name, arrival_time, burst_time):
        self.process_name = process_name
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)
        self.remainingTime = self.burst_time


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
        self.startLength = len(self.facultyProcess)

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
            print("Remaining Time: " + str(process.remainingTime))
            print("Arrival Time: " + str(process.arrival_time))

    def getTurnAroundTime(self):
        for process in self.executedProcess:
            process.turnAroundTime = process.burst_time + process.waitingTime

    def checkEmpty(self):
        if len(self.facultyProcess) == 0:
            print("Faculty  empty")
            return True
        else:
            print("Faculty not empty")
            return False

    def getAverageTime(self):
        self.startExecution()
        self.getTurnAroundTime()

        totalWaitingTime = 0
        totalTurnAroundTime = 0

        for process in self.executedProcess:
            totalWaitingTime += process.waitingTime
            totalTurnAroundTime += process.turnAroundTime
            print(
                " " + process.process_name + " " + str(process.burst_time) + " " + str(process.waitingTime) + " " + str(
                    process.turnAroundTime))
        print("Average Waiting Time = ", (totalWaitingTime / self.startLength))
        print("Average Turn Around Time = ", (totalTurnAroundTime / self.startLength))

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
        self.facultyProcess.sort(key=lambda x: x.arrival_time, reverse=False)
        print("Sorted List")
        self.printProcessList()

        while not self.checkEmpty():
            present_process = self.facultyProcess.pop(0)
            print("Popped +" + present_process.process_name)
            self.executeProcess(present_process, mainTimer)

    def getWaitingTime(self,process):
        TAT = process.endTime - process.arrival_time
        print("ENDTIME: " + str(process.endTime))
        print("ARRIVAL TIME: " + str(process.arrival_time))
        process.waitingTime = TAT - process.burst_time
        print("UPDATING WAITING TIME: " + str(process.waitingTime))

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

    def stopAt(self, process, mainTimer, next_process):
        if next_process.arrival_time <= mainTimer.mainTimer:
            return True
        else:
            return False


if __name__ == "__main__":
    faculty = FacultyQueryManagement()
    # faculty.checkProcessQueue()
    faculty.getAverageTime()