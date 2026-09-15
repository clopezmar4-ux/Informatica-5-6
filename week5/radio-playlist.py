import time
def main():

    playlist= ["Boston", "Dracula", "I Knew It, I Knew You", "hate that i made you love me", "Risk It All"]

    playlist.append("Be By You")
    print(playlist)

    playlist.insert(0,"Bohemian Rhapsody") # Add an element to the list
    print(playlist)

    playlist.pop(4) #take off an element
    print(playlist)

    print(playlist.index("Risk It All")) #find the elment in the list

    print("Number of songs in playlist:", len(playlist)) #count an element of the list

    playlist.reverse() #change the order
    print(playlist)

    playlist.sort() #Alphabetical order
    print(playlist)

    #Challenge
    repeat = len(playlist)
    while repeat > 0:
        print(playlist)
        song = playlist[0]
        playlist.pop(0)
        playlist.append(song)
        repeat -= 1
        time.sleep(3)




if __name__=="__main__":
    main()
