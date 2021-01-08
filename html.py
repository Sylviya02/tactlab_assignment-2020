import webbrowser
new=2 #open in a new tab, if possible
'''To open a public URL, in this case, the webbrowser docs
url=''
webbrowser.open(url,new=new)'''
print("\nTOP 10 WORDS OF THE DECADE IN:\n")
print("1.USA\n2.UK\n3.India\n4.Canada\n")
a=1
while(a==1):
    choice=int(input("\nEnter Your choice:\n"))
    if (choice==1):
        url = "file:///C:/Users/sylvi/Desktop/html%20files/USA.html"
        webbrowser.open(url,new=new)
    if (choice==2):
        url = "file:///C:/Users/sylvi/Desktop/html%20files/UK.html"
        webbrowser.open(url,new=new)
    if (choice==3):
        url = "file:///C:/Users/sylvi/Desktop/html%20files/India.html"
        webbrowser.open(url,new=new)
    if (choice==4):
        url = "file:///C:/Users/sylvi/Desktop/html%20files/Canada.html"
        webbrowser.open(url,new=new)
    a=int(input("\nDo you want to continue:Yes(1)/No(0):\n"))
'''url = "file://d/testdata.html"
webbrowser.open(url,new=new)'''
