#Solve Tower of Hanoi problem
def tower_of_hanoi(n, source, helper, destination):
   if n == 1:
       print(f"Move disk 1 from {source} → {destination}")
       return
   tower_of_hanoi(n - 1, source, destination, helper)
   print(f"Move disk {n} from {source} → {destination}")
   tower_of_hanoi(n - 1, helper, source, destination)

# Taking input from user
n = int(input("Enter number of disks: "))
tower_of_hanoi(n, 'A', 'B', 'C')
