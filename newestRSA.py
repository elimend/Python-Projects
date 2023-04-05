import math
 
print("RSA Encryption/Decryption Learn-Along Game")
print("-----------------------------------------------------")
 
# Input starting prime numbers
print("Please input 'p' and 'q' values below, they must be prime or will ask you to input again:")
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
print("-----------------------------------------------------")

 
# Checks to see if inputs (p and q) are prime
def check_prime(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return false
    return True
 
check_p = check_prime(p)
check_q = check_prime(q)

# If inputs are not prime, it will ask the user to enter p and q again
while(((check_p==False)or(check_q==False))):
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    check_p = check_prime(p)
    check_q = check_prime(q)
 
# RSA Modulus
print("n is found by multiplying p and q (the inputs chosen above)")
print("Follow along and calculate n by yourself to make sure you get the same answer")
n = p * q
print("RSA Modulus(n) is:",n)
 
# Eulers Toitent or phi(n)
print("Eulers Totient is found by taking (p-1) and multiply (q-1)")
print("This is also called phi(n). Calculate the totient and check if you got the same answer")
r= (p-1)*(q-1)
print("Eulers Toitent(r) is:",r)
print("-----------------------------------------------------")
 
#GCD
# Calculation of GCD for e 
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e
 
# Euclid's Algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                print("%d = %d*(%d) + %d"%(r,a,e,b))
            r=e
            e=b
 
# Extended Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
# Multiplicative inverse - used to calculate d later on
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
        elif(s>0):
            print("s=%d."%(s))
        return s%r

 
# e value calculation
print("e is calculated by finding any number coprime to r")
print("In this case, we calculate the highest e coprime to r")
for i in range(1,r):
    if(egcd(i,r)==1):
        e=i
print("The value of e is:",e)
print("-----------------------------------------------------")

 
# d, Private and Public Keys
# Calculation of d which is part of the private key
# Printing private key and public key
print("Euclid's Extended Algorithm:")
d = mult_inv(e,r)
print("To find d or the private key part, you take the modular multiplicative inverse")
print("To do this inverse, take e(mod phi(n)), you can use a calulator...")
print("or you might need a 3rd party program to help if the numbers are too big")

print("The value of d is:",d)
print("-----------------------------------------------------")
public = (n,e)
private = (n,d)
print("Private Key is:",private)
print("Public Key is:",public)
print("-----------------------------------------------------")
 
# Encryption algorithm
def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x
     
 
# Decryption algorithm
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(',')
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x
 
# Message to be decrypted or encrypted
message = input("What would you like encrypted or decrypted?(Input a letter message or numbers separated by commas):")
print("Your message is:",message)
 
# Choosing whether to encrypt or decrypt, results are printed
choose = input("Type '1' for encryption and '2' for decrytion.")
if(choose=='1'):
    enc_msg=encrypt(public, message)
    print("Your encrypted message is:", enc_msg)
    print("Thank you for learning and playing!")
elif(choose=='2'):
    print("Your decrypted message is:",decrypt(private,message))
    print("Thank you for learning and playing!")
else:
    print("You entered the wrong option.")
    print("Thank you for learning and playing!")
