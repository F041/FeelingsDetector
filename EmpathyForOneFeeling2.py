# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:01:38 2016

@author: F041
"""
from __future__ import division
import random as rnd
import csv
import time

start = time.clock()

#def feelingsList
list_hopeless=["Do you think no matter what you could do, you're not going to solve the situation you're thinking?",
          "Do you see zero options to solve the situation you're thinking?",
          "Do you feel hopeless?"]
list_torment=["Are you having the same thought for more time than you'd like?",
         "Do you have a persistent thought?",
         "Do you have a thought that is stuck in your mind?",
         "Do you feel torment?"]
list_repulsion=["Do you prefer to be in another place instead of meeting the person you're thinking about?",
           "Do you prefer to do another thing instead of the one you're thinking?",
           "Do you feel repulsion?"]
list_apprehensive=["Do you anticipate something unpleasant will happen?",
              "Do you think you're going to experience a stressful situation in the near future?",
              "Do you feel apprehensive?"]
list_worried=["Do you think something unpleasant will happen in the near future?",
              "Do you feel worried?"]
list_sad=["Do you feel sad?"]
list_anxious=["Do you feel anxious?",
              "Do you have the perception you aren't able to wait for the event?"]
list_discouraged=["Do you feel discouraged?",
                  "You don't have the will to continue the action because of the results you had till now with it?"]
list_terrified=["Do you feel terrified?"]     
list_panicked=["Do you feel panicked?"]   
list_confused=["You can not understand why you're in the situation?","Do you feel confused?"]  
list_lonely=["Do you feel lonely?"]
list_agony=["Do you feel agony?"]     
list_shocked=["You can't believe what the other person said?","Are you shocked?"]


inventory=[listname for listname in dir() if listname.startswith("list_") ]
inventory = [globals()[listname] for listname in inventory]
dim_inv=len(inventory)

questions=[]
for lst in inventory:    
    questions+=lst
questions.sort()
last_label="user_feeling"
legend=questions+[last_label]
legend.sort()
iteration=0
answers_file=csv.writer(open('Answers.csv', "wb"),delimiter=',')

all_answers=[]
all_data=[]
intruder=0
#Writing question header
answers_file.writerows([legend])
all_questions_indexes=[]
bug=0
bug_list=[]
while iteration<10**4:#The 3 instead of 4 reduces the probability to have answers that have a lenght >len(row)-1
    user_feeling=""
    random_feeling=rnd.sample(range(dim_inv),dim_inv)
    rnd.shuffle(random_feeling)
    inventory_position=random_feeling.pop()
    feeling_list=inventory[inventory_position]
    dim_feel=len(feeling_list)
    random_question=rnd.sample(range(dim_feel),dim_feel)
    rnd.shuffle(random_question)
    question_position=random_question.pop()
    questions_asked=[]
    
    #def getEmpathy
    feeling_found=False
    dunno=0
    no=0
    answers=[]
    questions_indexes=[]
    
    while feeling_found==False:   
        if questions.index(feeling_list[question_position]) not in questions_indexes:#New add avoid bugs
            question=feeling_list[question_position]
            questions_asked.append(question) 
            questions_indexes.append(questions.index(question))
            #print  question+" Y/N/DUNNO"
            answer=rnd.randint(0,3)
            if answer==0:
                answer='y'
            elif answer==1:
                answer='n'
            else:
                answer='dunno'
            answers.append((int(questions.index(question)),answer))#from question to questions.index(question)
        else:
                bug_list.append(questions.index(question))
                question_position=random_question.pop()
        if question in questions:
            if questions.index(question) not in questions_indexes:#New add to spot the duplicates
                questions_indexes.append(questions.index(question))
            
        
        #Answer section
        if answer.upper()=="Y":
            pick_feeling=[listname for listname in dir() if listname.startswith("list_") ]
            #print "Your feeling: "+pick_feeling[inventory_position].replace("list_","")
            user_feeling=pick_feeling[inventory_position].replace("list_","")
            feeling_found=True
        elif answer.upper()=="N":
            no+=1
        elif answer.upper()=="DUNNO":
            dunno+=1       
                 
        if no>0 and len(random_feeling)>0:
               try:#Inserted try to see if some list>21 elements
                   inventory_position=random_feeling.pop()  
               except IndexError:
                   if len(random_feeling)==0:                       
                       print "No more feelings from which we can ask questions"
                   feeling_found=True  
                   user_feeling='none'#added to try to resolve the index out of range
               feeling_list=inventory[inventory_position]
               dim_feel=len(feeling_list)
               random_question=rnd.sample(range(dim_feel),dim_feel)
               rnd.shuffle(random_question)
               try:
                   question_position=random_question.pop()
               except IndexError:
                   #print "No more questions for the feeling"
                   feeling_found=True
               dunno=0 #to avoid the sum of not linked dunno
               no=0 #to avoid to enter here after a dunno
               
        elif len(random_feeling)==0 and len(random_question)==0:
            #print "No more feelings from which we can ask questions",
            feeling_found=True
            
        elif dunno>0 and dunno<dim_feel:  
            try:
               question_position=random_question.pop()
               dim_feel=len(feeling_list)
            except IndexError:
               #print "No more questions for the feeling"
               feeling_found=True
        
        elif len(questions_indexes)==len(inventory):#NewAdd
            feeling_found=True
        elif dunno==dim_feel: 
           inventory_position=random_feeling.pop()  
           feeling_list=inventory[inventory_position]
           dim_feel=len(feeling_list)
           random_question=rnd.sample(range(dim_feel),dim_feel)
           rnd.shuffle(random_question)
           try:
               question_position=random_question.pop()           
           except IndexError:
               print "No more questions for the feeling"
               feeling_found=True
           dunno=0
           no=0
           
    for question_element in questions:#New add #from element to question_element
        if question_element not in questions_asked:#from element to question_element
            answers.append((int(questions.index(question_element)),'empty'))#from element to question.index(question_element)
            questions_asked.append(question_element)
            
    answers.sort()
    if len(answers)>len(legend):
        bug+=1
    answers.append(user_feeling)      
    temporary_drawer=[]
    for element in answers:        
        if type(element) is tuple:
            temporary_drawer.append(element[1])
        else:
            temporary_drawer.append(element)
    if len(temporary_drawer)>len(legend):
        intruder+=1
    all_data.append(temporary_drawer)
    for lst in all_data:
        if lst[-1]=='': 
            lst[-1]='none' 
    iteration+=1
    all_answers.append(answers)
    all_questions_indexes.append(questions_indexes)
    #ordering the answers giving its position according to the position of the question
#all_answers.sort()
"""for line in all_answers:
    line.sort()#Feeling in the first position instead of the last"""

"""for lst in all_questions_indexes:
    for QA in lst: #numero posizione
        for Q in legend:
            if QA in legend.index(Q):
                answers_file.writerows([all_answers[all_questions_indexes.index(lst)][all_questions_indexes.index(position)][1]])
                pointer+=1"""

def divideset(rows,column,value):#about 0.82 average
   # Make a function that tells us if a row is in the first group (true) or the second group (false)
   split_function=None
   if isinstance(value,int) or isinstance(value,float): # check if the value is a number i.e int or float
      split_function=lambda row:row[column]>=value#Tuple problem solved with the [1]
   else:
      split_function=lambda row:row[column]==value
   
   # Divide the rows into two sets and return them
   set1=[row for row in rows if split_function(row)]
   set2=[row for row in rows if not split_function(row)]
   return (set1,set2)

"""def dividedata(data, col_num, test=None):#0.79 average
    "Doc string placeholder"

    # if no test function was passed, return (quite arbitrarily)
    # a shallow copy of the original list and an empty list
    if test==None: return data[:], []

    set0, set1 = [], []
    for row in data:
        if test(row[col_num]):
            set0.append(row)
        else:
            set1.append(row)

    return set0, set1"""
 
set1,set2=divideset(all_data,1,'dunno')

# Create counts of possible results (the last column of each row is the result)
def uniquecounts(rows):
   results={}
   for row in rows:
      # The result is the last column
      r=row[len(row)-1]
      if r not in results: results[r]=0
      results[r]+=1
   return results
          
set3=uniquecounts(all_data)
          
def entropy(rows):
   from math import log
   log2=lambda x:log(x)/log(2)  
   results=uniquecounts(rows)
   # Now calculate the entropy
   ent=0.0
   for r in results.keys():
      p=float(results[r])/len(rows)
      ent=ent-p*log2(p)
   return ent

class decisionnode:
  def __init__(self,col=-1,value=None,results=None,tb=None,fb=None):
    self.col=col
    self.value=value
    self.results=results
    self.tb=tb
    self.fb=fb

def buildtree(rows,scoref=entropy): #rows is the set, either whole dataset or part of it in the recursive call, 
                                    #scoref is the method to measure heterogeneity. By default it's entropy.
  if len(rows)==0: return decisionnode() #len(rows) is the number of units in a set
  current_score=scoref(rows)
  #print 'current score'
  #print current_score
  # Set up some variables to track the best criteria
  best_gain=0.0
  best_criteria=None
  best_sets=None
  
  column_count=len(rows[0])-1   #count the # of attributes/columns. It's -1 because the last one is the target attribute and it does not count.
  for col in range(0,column_count):
    # Generate the list of all possible different values in the considered column
    global column_values        #Added for debugging
    column_values={}  
    for row in rows:
       if col>len(row)-1:
           print 'problem: '+str(col)+" row lenght: "+str(len(row)-1) 
       column_values[row[col]]=1  
       
    # Now try dividing the rows up for each value in this column
    for value in column_values.keys(): #the 'values' here are the keys of the dictionnary        
        (set1,set2)=divideset(rows,col,value) #define set1 and set2 as the 2 children set of a division #with the [1] there is a list index out or range. Because of the '' it finds?         
  
        # Information gain
        p=float((len(set1))/len(rows)) #p is the size of a child set relative to its parent
        gain=current_score-p*scoref(set1)-(1-p)*scoref(set2) #cf. formula information gain
        #print 'gain is '+str(gain)
        if gain>best_gain and len(set1)>0 and len(set2)>0: #set must not be empty
          best_gain=gain
          best_criteria=(col,value)
          best_sets=(set1,set2)
  #print 'best gain: '
  #print best_gain     
  # Create the sub branches   
  if best_gain>0:
    #print 'entered in the if best_gain>0'
    trueBranch=buildtree(best_sets[0])
    falseBranch=buildtree(best_sets[1])

    return decisionnode(col=best_criteria[0],value=best_criteria[1],
                        tb=trueBranch,fb=falseBranch)
  else:
    return decisionnode(results=uniquecounts(rows))             
    
tree=buildtree(all_data) #IndexError: list index out of range

def getwidth(tree):
  if tree.tb==None and tree.fb==None: return 1
  return getwidth(tree.tb)+getwidth(tree.fb)

def getdepth(tree):
  if tree.tb==None and tree.fb==None: return 0
  return max(getdepth(tree.tb),getdepth(tree.fb))+1


from PIL import Image,ImageDraw

def drawtree(tree,jpeg='tree.jpg'):
  w=getwidth(tree)*100
  h=getdepth(tree)*100+120

  img=Image.new('RGB',(w,h),(255,255,255))
  draw=ImageDraw.Draw(img)

  drawnode(draw,tree,w/2,20)
  img.save(jpeg,'JPEG')
  
def drawnode(draw,tree,x,y):
  if tree.results==None:
    # Get the width of each branch
    w1=getwidth(tree.fb)*100
    w2=getwidth(tree.tb)*100

    # Determine the total space required by this node
    left=x-(w1+w2)/2
    right=x+(w1+w2)/2

    # Draw the condition string
    draw.text((x-20,y-10),str(tree.col)+':'+str(tree.value),(0,0,0))

    # Draw links to the branches
    draw.line((x,y,left+w1/2,y+100),fill=(255,0,0))
    draw.line((x,y,right-w2/2,y+100),fill=(255,0,0))
    
    # Draw the branch nodes
    drawnode(draw,tree.fb,left+w1/2,y+100)
    drawnode(draw,tree.tb,right-w2/2,y+100)
  else:
    txt=' \n'.join(['%s:%d'%v for v in tree.results.items()])
    draw.text((x-20,y),txt,(0,0,0))
    
drawtree(tree,jpeg='treeview.jpg')

def classify(observation,tree):#The classify wants the len-1 to work
  if tree.results!=None:
    return tree.results
  else:
    v=observation[tree.col]
    branch=None
    if isinstance(v,int) or isinstance(v,float):
      if v>=tree.value: 
          branch=tree.tb
      else: 
          branch=tree.fb
    else:
      if v==tree.value: 
          branch=tree.tb
      else: 
          branch=tree.fb
    return classify(observation,branch)
    
print classify(['empty','empty','empty','empty','empty','empty','y',
                'n','empty','empty','empty','empty','empty','empty',
                'empty','empty','empty','empty','empty','empty',
                'empty','empty','empty',
                'empty','empty','empty',
                'empty','empty'],tree)

end = time.clock()
print 'time passed: '+str(end - start)

#Some lists are longer than 21
#The problem is the answers creation. Some question indexes repeat themselves. Why?
#With 1000 cycles and 4 bugs, it still work. Why?