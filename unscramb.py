import pyperclip

an = list("0123456789")
au = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
al = list("abcdefghijklmnopqrstuvwxyz")

print("to stop press ctrl+c")
while True:
    try:
        inp1 = input("input text to decypher: ")
        while True:
            try:
                main = int(input("do you know what the shift on the text is 1-Yes 2-No: "))
                if main == 1:
                    inp2 = int(input("input the range the text was shifted by: "))
                    shift = -inp2
                elif main == 2:
                    shift = 1
                    pass
                break
            except KeyboardInterrupt:
                exit()
            except:
                print("use integers")

        ttl = list(inp1)
        lor = []
        result = ""

        if main == 1:
            for char in ttl:
                if char in au:
                    pos = au.index(char)
                    new_pos = (pos + shift) % 26
                    result += au[new_pos]
                elif char in al:
                    pos = al.index(char)
                    new_pos = (pos + shift) % 26
                    result += al[new_pos]
                else:
                    result += char
            print(result)
            last = input("1-copy else-continue: ")
            if last == "1":
                pyperclip.copy(result)
                print(f"copied: {result}")
                result = ""
            else:
                result = ""
                pass

        elif main == 2:
            for i in range(26 + 1):
                result = ""
                for char in ttl:
                    if char in au:
                        pos = au.index(char)
                        new_pos = (pos - i) % 26
                        result += au[new_pos]
                    elif char in al:
                        pos = al.index(char)
                        new_pos = (pos - i) % 26
                        result += al[new_pos]
                    else:
                        result += char
                g = f"shift {i}: {result}"
                lor.append(g)
                print(g)
            inpl1 = input("1-copy else-continue: ")
            if inpl1 == "1":
                while True:
                    try:
                        print("select the cypher number from the list above")
                        inpl2 = int(input(": "))
                        pyperclip.copy(lor[inpl2])
                        print(f"copied: {lor[inpl2]}")
                        lor = []
                        break
                    except KeyboardInterrupt:
                        exit()
                    except:
                        print("select a number from the list")
            else:
                pass
    except KeyboardInterrupt:
        exit()
    except:
        print("error")