import math
import os

class Viterbi:
    def preprocessing(self, initial, stm, em, input, last_line):#preprocessing step
        input = input[:-1]#removing the newline character from the input
        n_states = len(stm)
        log_initial = [math.log(i) for i in initial]#log of initial matrix
        log_stm = []
        log_b = []
        for row in stm:#log of state transition matrix
            ls = []
            for i in row:
                ls.append(math.log(i))
            log_stm.append(ls)
        for s in input:#log_b matrix
            ls = []
            for i in range(n_states):
                ls.append(math.log(em[i][int(s)-1]))
            log_b.append(ls)
        self.initialization(log_initial, log_stm, log_b, input, last_line)

    def initialization(self, log_initial, log_stm, log_b, input, last_line):#initialization step
        n_states = len(log_stm)
        dl = []
        phi = []

        for i in range(n_states):#creating initial list of deltas and phis
            phi.append(0)
            dl.append(log_initial[i]+log_b[0][i])
        self.recursion(log_initial, log_stm, log_b, input, dl, phi, last_line)

    def recursion(self, log_initial, log_stm, log_b, input, dl, phi, last_line):#recursion step
        n_states = len(log_stm)
        input_size = len(input)
        dls = []
        phis = []
        dls.append(dl)
        phis.append(phi)
        for j in range(1, input_size):#creating a list of deltas and phis using the initial delta and phi values
            d = []
            p = []
            for i in range(n_states):
                m = []
                for k in range(n_states):
                    m.append(dls[-1][k] + log_stm[k][i])
                d.append(max(m)+log_b[j][i])
                p.append(m.index(max(m))+1)
            phis.append(p)
            dls.append(d)
        self.termination(dls, phis, last_line)

    def termination(self, dls, phis, last_line):#termination
        p_star = max(dls[-1])
        q_star = dls[-1].index(p_star)+1
        self.backtrack(phis, p_star, q_star, last_line)

    def backtrack(self, phis, p_star, q_star, last_line):#backtracking
        dic = {1:'F', 2:'L'}
        l = len(phis)-1
        q = [q_star]
        for i in range(l, 0, -1):
            a = phis[i][q[-1]-1]
            q.append(a)
        q.reverse()
        for a in q:
            res.write(dic[a])
        if not last_line:
            res.write("\n\n")

v = Viterbi()
stm = [[0.95, 0.05], [0.1, 0.9]]#state transition matrix
em = [[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], [1/10, 1/10, 1/10, 1/10, 1/10, 1/2]]#emission matrix
initial = [1/2, 1/2]#initial states

last_line = False
with open('input.txt', 'r') as f:
    lines = f.readlines()
with open('results.txt', 'w') as res:
    for i in range(0, 10, 2):
        res.write("For Rolls Set " + str(int((i / 2) + 1)) + ":\n")
        res.write("Rolls   : "+ lines[i])
        res.write("Die     : "+ lines[i + 1])
        res.write("Viterbi : ")
        if i == 8:
            last_line = True
        v.preprocessing(initial, stm, em, lines[i], last_line)
