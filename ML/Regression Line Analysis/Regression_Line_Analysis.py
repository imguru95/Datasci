class Solution:
    def output_quantities(self, ls):#method for calulating all given quantities
        lt = len(ls)
        x_bar = sum([i[0] for i in ls])/lt
        y_bar = sum([i[1] for i in ls])/lt
        x_1 = [(i[0]-x_bar)**2 for i in ls]#(x_i-x_bar)**2
        y_1 = [(i[1]-y_bar)**2 for i in ls]#(y_i-y_bar)**2
        x_y = [(i[0]-x_bar)*(i[1]-y_bar) for i in ls]#(x_i-x_bar)*(y_i-y_bar)
        s_x2 = sum(x_1)/lt
        s_y2 = sum(y_1)/lt
        s_xy = sum(x_y)/lt
        r = s_xy/((s_x2*s_y2)**0.5)#calculation of r using the formula given
        r_2 = r**2#r**2
        b = s_xy/s_x2
        a = y_bar - b*x_bar# regression line parameters a and b
        b_1 = round(b, 4)#rounding off b to 4 decimal places
        a_1 = round(a, 5)#rounding off a to 5 decimal places
        E = lt*s_y2*(1-r_2)#calculation of E using the formula given
        y_pred_ls = [a+b*i[0] for i in ls]#list containing predictions
        e_ls = [p[1]-q for (p,q) in zip(ls, y_pred_ls)]#list containing errors
        sum_errors = sum(e_ls)#sum of all the errors
        print("----------------------------------------------------")
        print("-----------Printing the given quantities---------")
        print("----------------------------------------------------")
        print("x_bar = ", x_bar)
        print("y_bar = ", y_bar)
        print("s_x2 = ", s_x2)
        print("s_y2 = ", round(s_y2, 4))
        print("s_xy = ", round(s_xy, 4))
        print("r = ", round(r, 4))
        print("r_2 = ", round(r_2, 4))
        print("E = ", round(E, 4))
        print("a = ", a_1)
        print("b = ", b_1)
        print("Regression line equation : y = {} + {}x".format(a_1, b_1))
        for i in y_pred_ls:
            print("y_{}_hat = ".format(y_pred_ls.index(i)+1), round(i, 7))
        for i in e_ls:
            print("e_{} = ".format(e_ls.index(i)+1), round(i, 6))
        print("sum of all the error values = ", sum_errors)

if __name__ == '__main__':
    ls = [(2,2),(4,6),(5,4),(7,8),(8,10),(10,12)]#Given data points
    s = Solution()
    s.output_quantities(ls)
