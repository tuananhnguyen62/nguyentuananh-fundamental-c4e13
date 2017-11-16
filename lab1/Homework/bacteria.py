n = int(input("How many B bacterias are there? "))
time = int(input("How much time in minutes will we wait? "))
replicate_time = 0

# số vi khuẩn = n nhân 2 nhân time lần
for i in range(1, time, 2):
    replicate_time += 1
    
if replicate_time == 0:
    total = n
else:
    total = n*2*replicate_time
print("After {0} minutes, we would have {1} bacterias".format(time, total))
