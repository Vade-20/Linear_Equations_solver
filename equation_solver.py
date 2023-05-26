import numpy as np
import re
from fractions import Fraction

num_var = int(input("Please enter the number of different variable each equation should have:"))

print('Please note that the quantity of equations must match the number of variables provided.\n')

def isequation(eq):
    global var
    if '=' not in eq:
        raise Exception ('Please enter a proper equation using "="')
    for i in eq:
        if i.isalpha() and i not in var:
            var.append(i)
    if len(var)>num_var:
        raise Exception ('Please provide a formal equation with an equal number of variables and equations as specified')
    
def adding_one(x):
    if x[0]=='':
        return (1,x[1])
    elif x[0]=='-':
        return (-1,x[1])
    else:
        return (int(x[0]),x[1])

def right_eq(eq):
    d = ''
    for i in eq:
        if i in ['+','-']:
            d+=f' {i}'
        elif i=='=':
            d+=' = '
        elif i!=' ':
            d+=i
    return d
    
var = []
constant = np.zeros((num_var,1))
number = np.zeros((num_var,num_var))

for i in range(num_var):
    eq = input(f'Please enter the equation number {i+1} here:').lower()
    eq = right_eq(eq)
    isequation(eq)
    data = re.findall(r'([-]?[\d]*)([a-z])',eq)
    con_data = re.findall(r"[-]?[\d]+(?![a-z])\b",eq)
    con_data = list(map(int,con_data))
    constant[i] = [sum(con_data)]
    data = list(map(adding_one,data))
    d = {}
    for j in data:
        d.setdefault(j[1],0)
        d[j[1]] = d[j[1]]+j[0]
    
    for j in range(num_var):
        try:
            number[i,j] = d.get(var[j],0)
        except IndexError:
            pass

try:
    inverse_number = np.linalg.inv(number)
except np.linalg.LinAlgError:
    print("There is no solution for given set of equation")
    quit()
    
ans = np.matmul(inverse_number,constant)
for i in range(num_var):
    print(f'The value of {var[i]}:{Fraction(ans[i,0])}')



