import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
print("Numpy Version:",np.__version__)
print("Pandas Version:",pd.__version__)
print("Scikit-learn Version:",sklearn.__version__)
print("Hello, Data Science!")


import numpy as np
a=np.array([10,20,30,40])
print(a)


import pandas as pd
data={
    "Name":["Ram","Sita","Gita"],
    "Age":[20,21,22]
}
df=pd.DataFrame(data)
print(df)


import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,30,40]
plt.plot(x,y)
plt.show()


A=" KONERU LAKSHMAIAH EDUCATIONAL FOUNDATION "
print("Capitalize():",A.capitalize())
print("casefold():",A.casefold())
print("center():",A.center(60,"*"))
print("count():",A.count("A"))
print("Find():",A.find("EDUCATIONAL"))
print("Index():",A.index("FOUNDATION"))
print("islower():",A.islower())
print("isupper():",A.isupper())
print("Join():","-".join(A))
print("Lower():",A.lower())
print("Replace():",A.replace("FOUNDATION","UNIVERSITY"))
print("Swapcase():",A.swapcase())
print("Title():",A.title())
print("Upper():",A.upper())
print("Zfill():",A.zfill(50))


name = "KLH"
print("{:<10}".format(name)) #left Alignment
print("{:>10}".format(name)) #left Alignment
print("{:^10}".format(name)) #Center Alignment
num = -250
print("{:=8}".format(num)) #Sign Alignment: Spaces are inserted between the sign and the number.
print("{:+}".format(45))
print("{:+}".format(-45)) #Always Show Sign
print("{:-}".format(-45))
num = 45.6789 
print("{:f}".format(num)) #Fixed-Point Format: automatically displays 6 digits after the decimal point.
