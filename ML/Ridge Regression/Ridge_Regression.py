import matplotlib.pyplot as plt
import os.path
import csv
import shutil

class RidgeRegression:
    def matrix_addition(self, a, b):#method to add two matrices
        c = []
        for i in range(len(a)):
            s = [p+q for (p, q) in zip(a[i], b[i])]
            c.append(s)
        return c

    def matrix_subtraction(self, a, b):#method to subtract one matrix from the other
        c = []
        for i in range(len(a)):
            d = [p - q for (p, q) in zip(a[i], b[i])]
            c.append(d)
        return c

    def matrix_multiplication(self, a, b):#method to multiply two matrices
        c = []
        for row in a:
            ls = []
            for i in range(len(b[0])):
                p = [r[i] for r in b]
                l = sum([x*y for (x,y) in zip(row, p)])
                ls.append(l)
            c.append(ls)
        return c

    def matrix_inverse(self, a):#method to get the inverse of a matrix
        det_a = self.matrix_determinant(a) #inverse of a matrix is given by transpose of its cofactor matrix divided by its determinant
        cofactor_mat_a = []
        for i in range(len(a)):#indexes rows
            ls = []
            for j in range(len(a)):#indexes columns
                mat = [b[:j] + b[j+1:] for b in a[:i] + a[i+1:]]
                minor_ij = self.matrix_determinant(mat)
                cofactor_ij = ((-1)**(i+j))*minor_ij#cofactor calculation
                cofactor_ij_2 = cofactor_ij/det_a
                ls.append(cofactor_ij_2)
            cofactor_mat_a.append(ls)
        return self.matrix_transpose(cofactor_mat_a)

    def matrix_determinant(self, a):#finding matrix determinant using recursion
        if len(a)==1:
            return a[0][0]
        else:
            det = 0
            for i in range(len(a)):
                ls = []
                for j in range(1, len(a)):
                    ls.append(a[j][:i]+a[j][i+1:])
                det += ((-1)**i)*a[0][i]*self.matrix_determinant(ls)
            return det

    def matrix_transpose(self, a):#method to get the transpose of a matrix
        c = []
        for i in range(len(a[0])):
            ls = []
            for row in a:
                ls.append(row[i])
            c.append(ls)
        return c

    def generate_lambda_indentity_matrix(self, n, l):#method to get the identity matrix*lambda
        identity_matrix_nxn = []
        for i in range(n):
            ls = [0] * n
            ls[i] = l
            identity_matrix_nxn.append(ls)
        return identity_matrix_nxn

r = RidgeRegression()
lambdas = [0.00001, -0.00001, 0.0001, -0.0001, 0.001, -0.001, 0.01, -0.01, 0.1, -0.1]#list of given lambda values
x_1, x_2, x_3 = (1,2), (2,4), (-3,-6)
y_1, y_2, y_3 = 1, 2, -3
x_1, x_2, x_3 = list(x_1), list(x_2), list(x_3)
x_1.insert(0, 1)
x_2.insert(0, 1)
x_3.insert(0, 1)
X= [x_1, x_2, x_3] #X matrix
Y = [[y_1], [y_2], [y_3]]#Y matrix
X_T = r.matrix_transpose(X)#X transpose matrix
#Multilinear regression
det_value = r.matrix_determinant(r.matrix_multiplication(X_T, X))#determinant of X_T*X
print("Determinant of X_T*X = ", det_value)
print("Determinant of X_T*X is zero. So, multilinear regression analysis cannot be performed on the given X and Ys")
#Ridge Regression
results = []
column_names = ['Lambda', 'β-0', 'β-1', 'β-2', 'E']
for l in lambdas:#iterating over the lambdas
    identity_matrix_3x3_l = r.generate_lambda_indentity_matrix(3, l)
    t_1 = r.matrix_addition(r.matrix_multiplication(X_T, X), identity_matrix_3x3_l)#term 1
    t_2 = r.matrix_multiplication(X_T, Y)#term 2
    betas = r.matrix_multiplication(r.matrix_inverse(t_1), t_2)#betas
    e = sum([p[0]**2 for p in r.matrix_subtraction(Y, r.matrix_multiplication(X, betas))])#calculation of E
    result = [l, betas[0][0], betas[1][0], betas[2][0], e]
    results.append(result)

dir = "Results"
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)

with open("Results/results.csv", "w") as file:#writing results to file
    writer = csv.writer(file)
    writer.writerow(column_names)
    writer.writerows(results)

list_l, list_e_p, list_e_n = [], [], []
for result in results:#populating lists list_l, list_e_p and list_e_n
    if result[0] > 0:
        list_l.append(result[0])
        list_e_p.append(result[-1])
    else:
        list_e_n.append(result[-1])

fig, (a1, a2) = plt.subplots(1, 2, figsize =(12, 5))#loglog graph plotting
fig.suptitle('E vs |λ| on log-log scale', color = "blue", fontsize = "16")
p1 = a1.loglog(list_l, list_e_p, "-g", marker=".")
p2 = a2.loglog(list_l, list_e_n, "-r", marker=".")
fig.legend([p1, p2], labels = ["λ>0", "λ<0"])
for a in [a1, a2]:
    a.set_xlabel('log(|λ|)---->', color = 'blue')
    a.set_ylabel('log(E)---->', color = 'blue')
plt.savefig('Results/results.png')