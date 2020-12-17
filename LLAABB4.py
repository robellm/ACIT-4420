import wmi
from reportlab.pdfgen import canvas

# Initializing the wmi constructor
f = wmi.WMI()
c = canvas.Canvas("hello.pdf")
list = []

# Iterating through all the running processes
for process in f.Win32_Process():
    # Displaying the P_ID and P_Name of the process
    list.append(process.Name +" : " +str(process.ProcessId))
print(list)
list = sorted(list)

y = 700
for i in list:
    if y > 20:
        c.drawString(72, y, i)
        y -= 20
    else:
        break

c.showPage()
c.save()