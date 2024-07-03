# Multiplefunction 
class multiplefunction():
    def add():
        Num1= 10
        Num2= 30
        Add= Num1+Num2
        print("Num1=", Num1)
        print("Num2=", Num2)
        print("Add=", Add)

    def BMI():
        BMI=int(input("Enter the BMI Index: "))
        if BMI < 18.5:
            print("Underweight")
        elif BMI < 25:
            print("Normal weight")
        elif BMI < 30:
            print("Very Overweight")
        else:
            print("Obese")
        
    def Subfields():
        SubfieldsInAI=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")  
        for list in SubfieldsInAI:
            print(list)
              
    def oddeven():
        num=int(input("Enter a number to check odd or even:"))
        remainder = num%2
        if(remainder == 0):
            print(num,"is Even Number")
        else:
            print(num,"is Odd Number")
    
    def elegibility():
        Gender=input("Enter your Gender:").lower()
        Age=int(input("Enter your Age:"))
        if (Gender=="male" and Age> 21) or (Gender=="female" and Age>18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
        
    def percentage():
        sub=["Subject1","Subject2","Subject3","Subject4","Subject5"]
        mark1=int(input("Subject1 ="))
        mark2=int(input("Subject2 ="))
        mark3=int(input("Subject3 ="))
        mark4=int(input("Subject4 ="))
        mark5=int(input("Subject5 ="))
        total=mark1+mark2+mark3+mark4+mark5
        count=len(sub)
        print("Total :",total)
        percentage=total/count
        print(f"Percentage: {percentage:.13f}")

    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        area=(height*breadth)/2
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle:",area)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        perimeter=height1+height2+breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",perimeter)



            


        