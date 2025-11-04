import matplotlib.pyplot as plt
import numpy as np
# style=dict(marker="*",
#          markersize=15,
#          markerfacecolor="green",
#          markeredgecolor="red",
#          linestyle="dashed",
#          linewidth=5)
# x=np.array([2023,2024,2025,2030])
# y1=np.array([15,25,30,20])
# y2=y=np.array([25,35,40,35])
# y3=y=np.array([10,45,19,25])
# label_style=dict(fontsize=25,
#           family="Arial",
#           fontweight="bold")
# plt.title("class size",**label_style,color="blue") #adding title
# plt.xlabel("year",**label_style,color="black") #adding title to x_axis
# plt.ylabel("students",**label_style,color="black")
#
#
# plt.tick_params(axis="both",colors="purple")
#
# plt.plot(x,y1,**style,color="yellow")
# plt.plot(x,y2,**style,color="black")
# plt.plot(x,y3)
# plt.xticks(x)
#
# plt.show()


 # grid lines
# x=[1,2,3,4,5]
# y=[10,11,13,15,17,20]
# plt.grid(axis="y",linewidth=2,# inserting grid
#          color="lightgray",linestyle="dotted")
# plt.plot(x)
# plt.show()



# barchart

x=np.array(["chem","math","physics","programming"])
y=np.array([85,100,95,80])

plt.bar(x,y,color="skyblue")
plt.title("my class perfomance")
plt.xlabel("subjects")
plt.ylabel("percentage marks")
plt.show()


# piechart


