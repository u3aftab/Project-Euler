total=1
to_next=2
run=1
at_number=1
while to_next<=1000:
    if run%4==0:
        at_number+=to_next
        total+=at_number
        to_next+=2
        run=1
    else:
        at_number+=to_next
        total+=at_number
        run+=1
print total
