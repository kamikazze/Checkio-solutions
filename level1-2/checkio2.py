#! /usr/bin/python

def checkio(data):
    newlist = []
    for item in data:
 	    if data.count(item) > 1:
        	newlist.append(item)

    print newlist
    return newlist


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"






        



			

	


