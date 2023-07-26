

spelling = raw_input('Enter spelling  ')


def correct():
    print ("Great job that is correct")
def wrong():
    print("Opps try agian that is wrong")
    
    
if spelling=='bean':
    correct()
elif spelling=='Bean':
    correct()
elif spelling=='beans':
    correct()
elif spelling=='Beans':
    correct()
else:
    wrong()
    