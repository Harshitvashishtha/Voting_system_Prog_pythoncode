nominee1 = input("Enter the name of 1st nominee")
nominee2 = input("Enter the name of 2nd nominee")

# intianlly the voter count must be 0 

nm1_voltes = 0
nm2_voltes = 0 
voter_id= [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)

while True:
    if voter_id == []: # to check when the list is completed.
        print("voting session is over !!!")
        if nm1_voltes > nm2_voltes:
            percent = (nm1_voltes/no_of_voter)*100
            print(nominee1, "has won the election with", percent, "% of votes")
            break 
        elif nm2_voltes > nm1_voltes:
            percent = (nm2_voltes/no_of_voter)*100
            print(nominee2," has won the election with", percent,"% of votes")
            break
        else:
            print("both have equal number of votes")
            break


    voter = int(input("Enter your voter_id :"))
    if voter in voter_id:
        print("you are a voter")
        voter_id.remove(voter) # we will remove the voter for further
        print("to give vote to",nominee1, "press 1")
        print("to give vote to",nominee2, "press 2")
        print("-------------------------------------")
        vote= int(input("Enter your precious vote :"))
        if vote == 1 :
            nm1_voltes +=1
            print(nominee1,"Thanks for give me important vote to me ")
        elif vote ==2 :
            nm2_voltes +=1
            print(nominee2, "Thanks for given me your Precious vote")
        else :
            print("Checked your pressed key !!")
else :
    print("you are not a Voter or You have already voted")





