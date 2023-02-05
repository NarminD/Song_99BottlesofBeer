def bottles_of_beer():
    for i in range(99, -1, -1): #range from 99 to 0, counting down by 1
        if i == 0:
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print("Go to the store and buy some more, 99 bottles of beer on the wall.")
            

        else: 
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
        print("")


bottles_of_beer()
