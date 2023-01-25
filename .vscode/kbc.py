questions=[
    ["which language was used to create facsbook?","pyhon","french","html","php","none",4],
    ["which language was used to create facsbook?","pyhon","french","html","php","none",4],
    ["which language was used to create facsbook?","pyhon","french","html","php","none",4],
    ["which language was used to create facsbook?","pyhon","french","html","php","none",4],
    ["which language was used to create facsbook?","pyhon","french","html","php","none",4],
    ["which language was used to create facsbook?","pyhon","french","html","php","none",4],
    ["which language was used to create facsbook?","pyhon","french","html","php","none",4],
    ["which language was used to create facsbook?","pyhon","french","html","php","none",4],
    ["which language was used to create facsbook?","pyhon","french","html","php","none",4],
    ["which language was used to create facsbook?","pyhon","french","html","php","none",4],
    ["which language was used to create facsbook?","pyhon","french","html","php","none",4],
    ["which language was used to create facsbook?","pyhon","french","html","php","none",4]
   
]
print("kaun banega road pati....")

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,4000000,10000000]
i=0
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n question for RS. {levels[i]}")
    print(f"a.{question[1]}               b.{question[2]}")
    print(f"c.{question[3]}               d.{question[4]}")
    reply=int(input("Enter your answer(1-4) or 0 to quit"))
    if(reply==0):
        money=levels[i-1]  
        break
    if(reply==question[-1]):
          print(f"correct answer, you have won RS. {levels[i]}")
          if(i==4):
            money=10000
          elif(i==9):
                money=320000
          elif (i==14):
                  money=10000000
          
    else:
           print("wrong answer!")
           break
print(f"your take home money is", money)


          
       
          
      
         
    

















                                                                                             