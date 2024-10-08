import os
f= open("demo.txt", "w")

# data =f.write("hello i am rajendra rauta i am doing  java now")
data = f.read()
new_data=data.replace("java", "python")
print(new_data)
      


      
      
print(data)
print(type(data))
f.close()

