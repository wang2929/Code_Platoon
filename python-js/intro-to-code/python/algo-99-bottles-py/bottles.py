'''
Docstring for python-js.python.algo-99-bottles-py.bottles
INPUT:
- none

OUTPUTS:
- all 99 bottle lines in descending order

EDGE CASES / GOTCHAS:
1 bottle vs n bottles, n > 1
zero bottles: no more bottles of beer, go to the store and buy 99 more

DATA:
- For 3-99 bottles, they follow a formula
- 2 bottles does not because 1 bottle (singular)
- 1 bottle does not because 1 bottle (singular) and no more bottles
- No more bottles has a special line.
 
LOGIC:
- Loop counting down from 99

Lines from 99 bottles down to 3 bottles are the same, so for-loop
Then bottles 2, 1, and 0 are special
'''
    

#99 bottles of beer on the wall, 99 bottles of beer.
#Take one down and pass it around, 98 bottles of beer on the wall.
def bottle_song():
	# write your code here!
	for i in range(99, 1, -1):
		print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
		print(f"Take one down and pass it around, {i-1} bottles of beer on the wall")
	print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.")
	print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.")
	print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")

bottle_song()

