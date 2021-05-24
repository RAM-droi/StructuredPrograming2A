setpricehour = 0
gethours = 0
salary = 0
hourextra = 0
minhour= 40

setpricehour = int( input("Enter you price for hour:" ))
gethours = int( input("Enter your hours of work:" ))

if(gethours>40){
    hourextra = gethours-minhour
    salary = (minhour*setpricehour)+(hourextra*setpricehour*1.5)
    print("This is your salary", salary)
}
else{
      
}






