# Sudesh Sharma is a Linux expert who wants to have an online system where he can handle student queries. Since there
# can be multiple requests at any time he wishes to dedicate a fixed amount of time to every request so that everyone
# gets a fair share of his time. He will log into the system from 10am to 12am only.  He wants to have separate
# requests queues for students and faculty. Implement a strategy for the same. The summary at the end of the session
# should include the total time he spent on handling queries and average query time.


class Process:

    def __init__(self):
        self.process_name = ""
        self.arrival_time = 0
        self.burst_time = 0
        self.completion_time = 0
        self.remaining = 0


class QueryManagement:

    def __init__(self):
        self.count = 0
        self.arrival_time = 0
        self.burst_time = 0
        self.quantum_time = 0
        self.studentProcess = list()
        self.facultyProcess = list()

    def createProcess(self, name, arrival_time, burst_time):
        process = Process()
        process.process_name = name
        process.arrival_time = arrival_time
        process.burst_time = burst_time
        self.facultyProcess.append(process)

    def facultyQueue(self, no_of_process):
        totle_time = 0
        queue = 0
        round_robin = list()
        flag = False
        x = 0
        n = 0
        z = 0
        waiting_time = 0

        for count in range(no_of_process):
            print("Enter the details of Process" + str(count + 1))
            name = input("Process Name: ")
            arrival_time = int(input("Arrival Time: "))
            burst_time = int(input("Burst Time"))
            self.createProcess(name, arrival_time, burst_time)

        self.quantum_time = int(input("Enter the Quantum TIme for Faculty Queue: "))

        # Sorting the processes by their ARRIVAL time
        # If the ARRIVAL time is same then scheduling is based on First Come First Serve
        for count in range(no_of_process):
            for x in range(count + 1, count):
                if self.facultyProcess[count].arrival_time > self.facultyProcess[x].arrival_time:
                    temp = self.facultyProcess[count]
                    self.facultyProcess[count] = self.facultyProcess[x]
                    self.facultyProcess[x] = temp

        # Initialy all the burst time is remaining and completion of process is zero

        while True:
            for count in range(no_of_process):
                if totle_time >= self.facultyProcess[count].arrival_time:
                    z = 0
                    for x in range(queue + 1):
                        if round_robin[x] == count:
                            z += 1
                    if z == 0:
                        queue += 1
                        round_robin[queue] = count  # check
            if queue == 0:
                n = 0
            if self.facultyProcess[n].remaining > 0:
                if self.facultyProcess[n].remaining < self.quantum_time:
                    totle_time += self.facultyProcess[n].remaining
                    self.facultyProcess[n].remaining = 0
                else:
                    totle_time += self.quantum_time
                    self.facultyProcess[n].remaining -= self.quantum_time
                self.facultyProcess[n].completion_time = totle_time
                print( "Total time:  "+str(totle_time))
                n += 1
            flag = False
            for count in range(no_of_process):
                if self.facultyProcess[count].remaining > 0:
                    flag = True
            if flag == False:
                break

        print("*********************************************")
        print("********ROUND ROBIN ALGORITHM OUTPUT*********")
        print("*********************************************")
        print("Process Name | Arival Time | Burst Time | Completion Time|")

        for count in range(no_of_process):
            waiting_time = self.facultyProcess[count].completion_time - self.facultyProcess[count].burst_time - \
                           self.facultyProcess[count].arrival_time
            print(
                "|\t" + str(self.facultyProcess[count].process_name) + "|" + str(self.facultyProcess[count].arrival_time) + "|" +
                str(self.facultyProcess[count].burst_time) + "|" + str(self.facultyProcess[count].completion_time))


if __name__ == "__main__":
    # select_queue = None
    no_of_process = None
    qm = QueryManagement()
    print("Please choose a queue to post your query:")
    print("1. FACULTY queue")
    print("2. STUDENT queue")
    select_queue = int(input())
    if select_queue == 1:
        no_of_process = int(input("Enter number of process for FACULTY queue:"))
        qm.facultyQueue(no_of_process)
    else:
        pass
