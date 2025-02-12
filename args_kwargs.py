def func(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(f"{key} is my {value}")


normal = "My name is Vishal and thanks for coming to this program."
names = ["Vishal","Vayu", "Mayank", "Vishesh", "Sumit"]
relation = {"Anurag":"best friend","Madhu ma'am":"Tutor","Anil sir":"HOD"}
func(normal,*names,**relation)