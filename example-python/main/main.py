from town import Town

#test2

def main():
    t = Town("Dresden", 556780)
    print(t.toString())
    t.residents = -1
    print(t.toString())
    #t.name = ""
    #print(t.toString())

if __name__ == "__main__":
    main()