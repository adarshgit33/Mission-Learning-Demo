import time

count=int(input("Enter the starting number for counting : "))

print("\nThe countdown starts now : ")

for i in range(count,0,-1) :
    print(i)

    time.sleep(1)
time.sleep(2)
print("Wohoo! Happy new Year")