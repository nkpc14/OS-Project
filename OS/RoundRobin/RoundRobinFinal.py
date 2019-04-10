from .models import Process as ps,UserQueue,QunatumTime
from django.shortcuts import render

class Universal:
    UniversalTimer = 0
    PREEMPTION = list()
    STUDENT_AVAILABLE = False


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
        Universal.UniversalTimer = self.mainTimer


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

    def __str__(self):
        return str(self.arrival_time)

    def createProcess(self, process_name, arrival_time, burst_time, priority):
        self.process_name = process_name
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)
        self.remainingTime = self.burst_time
        self.priority = int(priority)

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

    def getData(self):
        # return self.executedProcess
        return self.executedProcess

    def setQuantumTime(self,quantumTime):
        self.quantum_time = quantumTime

    def createProcesses(self):
        # faculty = UserQueue.objects.get(id=1)
        # process1 = faculty.process_set.all()
        quantumTime = QunatumTime.objects.all()
        for item in quantumTime:
            self.setQuantumTime(item.quantumTime)
        process1 = ps.objects.filter(user=UserQueue.objects.get(id=1))
        for item in process1:
            process = Process()
            process.createProcess(item.name,
                                  item.arrivalTime,
                                  item.burstTime,
                                  0
                                  )
            self.facultyProcess.append(process)

        # process2 = Process()
        # student = UserQueue.objects.get(id=2)
        # process1 = student.process_set.all()
        process1 = ps.objects.filter(user=UserQueue.objects.get(id=2))
        for item in process1:
            process = Process()
            process.createProcess(item.name,
                                   item.arrivalTime,
                                   item.burstTime,
                                   1
                                   )
            self.facultyProcess.append(process)

    def printProcessList(self):
        for process in self.facultyProcess:
            print("PRINTING PROCESS")
            print(process.process_name)
            print("Remaining Time: " + str(process.remainingTime))
            print("Arrival Time: " + str(process.arrival_time))
            print("PRIORITY: " + str(process.priority))

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
        print("QUNATUM TIME: " + str(self.quantum_time))

    def checkProcessQueue(self):
        if len(self.processQueue) == 0:
            return True
        else:
            return True

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

    def getWaitingTime(self, process):
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
        if (next_process.arrival_time <= mainTimer.mainTimer) and (next_process.priority <= process.priority):
            return True
        else:
            return False


if __name__ == "__main__":
    faculty = FacultyQueryManagement()
    # faculty.checkProcessQueue()
    faculty.getAverageTime()
