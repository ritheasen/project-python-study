def writeUseDetails(userName, password):
    f = open("userdetails.text", "w")


    f.write(userName)
    f.write(f"\n{password}")

writeUseDetails("vuth","vuthloveoun")