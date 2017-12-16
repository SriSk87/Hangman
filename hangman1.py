import os
import random
import copy
ques = ["encyclopedia" , "elephant", "dictionary", "python", "halucination", "social Media", "octopus"]
appre = ["BonGo!!" , "Wippiee!!" , "Lucky Champ!!" ,"Hawk Eye!!", "Son of a gun!!", "Sweet!!"]
wrong = ["OOPs!!", "Think !!", "OMG!!", "Dafuq!!", "Darn!!"]
b = 1
while b == 1:
    und_count = 0
    empty_count = 0
    ans_count = 0
    try_count = 1
    disp_ques = random.choice(ques)
    disp_ques_list = list(disp_ques)
    disp_ques_list_copy = copy.deepcopy(disp_ques_list)
    for i in range(len(disp_ques_list)):
        rand_val = random.choice(disp_ques_list)
        und_index = list.index(disp_ques_list,rand_val)
        if rand_val != " ":
            disp_ques_list[und_index] = " _ "
    for i in disp_ques_list:
            if i == " _ ":
                und_count = und_count + 1
    empty_count = und_count
    try_count = 0
    while try_count <= (und_count + 5 ):
        ans_count = 0
        print("\n\n\t\t\t\tAttempt ",try_count ," of ", und_count + 5)
        print("\n\n\n\t\t\t")
        for i in range(len(disp_ques_list)):
             print(disp_ques_list[i], end = "")
        user_guess = input("\n\n\n\t\tAlphabet guessed - > ")
        try_count = try_count + 1
        for i in range(len(disp_ques_list)):
            if disp_ques_list_copy[i] == user_guess:
                disp_ques_list[i] = disp_ques_list[i].replace(disp_ques_list[i],user_guess)
                empty_count = empty_count - 1
                ans_count = ans_count + 1
        os.system('cls')        
        if ans_count == 0:
            print("\n\n\t\t",random.choice(wrong))
        else:
            print("\n\n\t\t",random.choice(appre))
        if empty_count > 0 and try_count == (und_count + 5):
            print("\n\n\t\tSorry .. The word was ",disp_ques)  
            break
        if empty_count == 0:
            print("\n\n\t\tCongrats .. You got it right")
            break
        
