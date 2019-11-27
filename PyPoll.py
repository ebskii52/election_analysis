#Open the data file.
#Write down the names of all the candidates.
#Add a vote count for each candidate.
#Get the total votes for each candidate.
#Get the total votes cast for the election.

testList = ["Something",True,None,1,10.0,["Something"],{"test" : 1}]
# for i in range(0, len(testList)):
#     print(f"""

# The item: {testList[i]} is of type {type(testList[i])}.
# ------------------------------------------------------
#     """)


def listTypeChecker(listToCheck: list) -> None:
    for i in range(0, len(listToCheck)):
        print(f"""
The item: {listToCheck[i]} is of type {type(listToCheck[i])}.
------------------------------------------------------
        """)


listTypeChecker(testList)