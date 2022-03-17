#Written by Esrah Zahid
#email: israh.zahid@ozu.edu.tr
#My solution to Maximum sum of Triangle Problem
#Python IDE version 3.9

class MaximumSum:
    
    def CreateListFromFile(self):
        file = open("C:/Users/Israh/Desktop/University/InternshipCodes/Triangle.txt", "r")
        file_to_list = [ file_to_list.split() for file_to_list in file.read().split('\n') if file_to_list != '' ] #Make a list of lists from the file
        this_list = [[int(element) for element in sublist] for sublist in file_to_list] #converted string list to integer
        return this_list

    def PrimeCheck(self, num):
        if num > 1:  
            for x in range(2, int(num/2) + 1):  
                if (num % x) == 0:
                    return True #not prime
                    break  
            else:
                return False #prime
        else:
            return True

    def MoveDiagnol(self, my_list, i, j): #Compare which prime is bigger when moving diagnoally and then move to that path
        if my_list[i+1][j+1] > my_list[i+1][j-1]:
            return (j+1)
        else:
            return (j-1)

    def MoveDownward(self, my_list, i, j, status): #Compare which prime is bigger when moving downwards and then move to that path
        if status == True:
            if my_list[i+1][j+1] > my_list[i+1][j]:
                return (j+1)
        else:
            if my_list[i+1][j-1] > my_list[i+1][j]:
                return (j-1)
        return j

    def MainCalculation(self, my_list):
        size_of_list=len(my_list)
        print("Adding: ", end="")
        max_sum = 0
        i = 0 #right vertex of 2D list
        j = 0 #left vertex of 2D List
        while i < size_of_list:
            if self.PrimeCheck(my_list[i][j]):
                print(str(my_list[i][j]), end="")
                max_sum += my_list[i][j]
                if i != size_of_list-1:
                    if self.PrimeCheck(my_list[i+1][j]): #Downwards is not prime
                        if (self.PrimeCheck(my_list[i+1][j+1])): #Right-diagnol is not prime
                            if j > 1 and (self.PrimeCheck(my_list[i+1][j-1])): #Left-diagnol exists and is not prime
                                if my_list[i+1][j] > my_list[i+1][j+1]:
                                    if my_list[i+1][j-1] > my_list[i+1][j]:
                                        j = self.MoveDiagnol(my_list, i, j)
                                else:
                                    j = self.MoveDiagnol(my_list, i, j)
                            else:
                                j = self.MoveDownward(my_list, i, j, True)
                        else:
                            if j >= 1 and (self.PrimeCheck(my_list[i+1][j-1])):
                                    j = self.MoveDownward(my_list, i, j, False)
                    elif (self.PrimeCheck(my_list[i+1][j+1])):
                        if j > 1 and self.PrimeCheck(my_list[i+1][j-1]):
                            j = self.MoveDiagnol(my_list, i, j)
                        else:
                            j += 1
                    else:
                        j -= 1
                          
                    i += 1 #move next line after each iteration
                    print(" + ", end="")
                else:
                    i += 1 #exit while loop
                    
        print("\n"+"Maximum sum of triangle = " + str(max_sum))

if __name__ == '__main__':
    Test = MaximumSum()
    my_list = Test.CreateListFromFile()
    Test.MainCalculation(my_list)
