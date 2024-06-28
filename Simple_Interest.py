# This application calculates simple intrest

def simple_int(P, N, R):
    I = (P*N*R)/100
    A = P + I
    return I, A

# Take Principal Period and Rate of Intrest as input from user
P = float(input("Please enter Principal in INR : "))
N = float(input("Please enter years : "))
R = float(input("Please enter Rate of Intrest in %p.a."))

# Print the intrest and amout
I, A = simple_int(P, N, R)
print(f'The Simple Intrest is : {I:.2f} INR')
print(f'The Total amount is : {A:.2f} INR')
