print("Hey ... I'm Emmanuel")

count = 0

while 100 > count:# Repeating Questions 100 times, until answer(Yes) is found
 
 print("Would you like to see my code")
 answer = input().lower()
 if answer == "no":
    print("Common ... I Know you would love see it")
    print("Just type YES\n pleeeaaaaasse")
    count = count + 1
 else:
   print("Good ... Now we are good to go")
   print("Move to the next Repository")
   break
 
if count == 100:
 print("Common i don't think you fill like seeing my code, would love to see you later\nBye")
