#QuizP.py
#Tye Borden

"""
This is a simple program that can be used to create an empty quiz/
questionnaire. This class is used to show the understanding of objects, 
dictionary, and lists. This shows the importance of using global lists or
dictionaries in objects, and that even though new objects are created they are 
added to same list or dictionary, and new one is not created.    
"""
class QuizP (object):
    #These are the class varibles 
    title = None
    li = {}
    quizNum = None
    
    """
    The  nested class to create a question objected to be properly inserted 
    into the QuizP object.
    """
    class QAndA(object) : 
        """
        This is the __init__ that takes in five parameters.
        question which is question the user wants
        choice1 the first choice noted as opiton A
        choice2 the second choice  noted as option B
        choice3 the third  choice noted as option C
        answer the correct choice denoted by letter vaule of A, B, and C. 
        
        """
        def __init__(
                self,
                question = "There is no question",
                choice1 = None,
                choice2 = None,
                choice3 = None,
                answer = None):
            
            self.question = question
            self.choice1 = choice1
            self.choice2 = choice2
            self.choice3 = choice3
            self.answer = answer
        """
        The function to override how the object is written out as a string
        """
        def __str__(self):
            return ("\n{} \n A.{}\n B.{}\n C.{}".format(
                    self.question,
                    self.choice1,
                    self.choice2,
                    self.choice3))  
            
    
    #The empty plain QAndA object
    stock = QAndA()
    """
    This init for the QuizP it takes in a string for the title and it takes in
    and integer as for what quiz number it is. If none are entered default 
    title are supplied. This will hold multiple quiz's in the dictionary of 
    quiz.
    """
    def __init__(self, title = "Empty questionnaire", quizNum = 1):
        
        self.title = title
        table = []
        table.append(self.title)
        table.append(self.stock)
        self.quizNum = quizNum
        self.li[self.quizNum] = table
        

    """
    This function adds the QAndA object in to the Quiz list in the QuizP 
    dictionary.
    """
    def addQuestion(self,q,c1,c2, c3,ans):
        quest = self.QAndA(q,c1,c2, c3,ans)
        
       
            
        if  self.li[self.quizNum][1] == self.stock :
            self.li[self.quizNum][1] = quest
        else:
            self.li[self.quizNum].append(quest)
    
    """
    This function display's the quiz the user wants to see, and checks to see
    if the answers given are correct.
    """    
    def display(self, quizNum = 1):
        count = 0
        print("\n" + self.li[quizNum][0])
        
        for i in range(1,len(self.li[quizNum])):
            print(self.li[quizNum][i])
            correct = self.li[quizNum][i]
            if self.getAnswer() == correct.answer :
                count += 1
        
        length = len(self.li[quizNum]) - 1
        print("\nQuiz complete: ")
        print("Your score was " + str(count) + "/" + str(length) + ".\n" )
    
    """
    This function for getting the users answer.
    """
    def getAnswer(self):
        ans = input("Which answer is correct ? ")
        return ans
    
    """
    This how you can check see what in the global dictionary
    """
    def disDict(self):
        print(self.li)

#To show how the program works. 
def main() :
    
    Test2 = QuizP('Simple Quiz',2)
    Test2.addQuestion(
            'What is 1 + 2 ?',
            '3',
            '4',
            '5',
            'A')
    
    Test2.addQuestion(
            'What is 4 - 2 ?',
            '3',
            '2',
            '5',
            'B')
    
    Test2.addQuestion(
            'What is 1 x 4 ?',
            '3',
            '9',
            '4',
            'C')
    
    Test2.addQuestion(
            'What is 10 / 5 ?',
            '3',
            '4',
            '2',
            'C')
    
    Test2.display(2)
    
    print("Take a break=============",end="\n\n")
    
    Test = QuizP()
    Test.display()

    print("Take a break================",end="\n\n")
    
    Test2.display(2)
    
#Testing the main above to show the functionality of the program.
if __name__ == "__main__":
    main()
        
    