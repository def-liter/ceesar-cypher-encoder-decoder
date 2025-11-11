import pyperclip


au = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
al = list("abcdefghijklmnopqrstuvwxyz")
print("to stop press ctrl+c")
while True:
    try:
        inp1 = input("input text to cypher: ")
        while True:
            try:
                inp2 = int(input("input the amount you want to shift your text by: "))
                if inp2 > 26:
                    print("can only shift by 26")
                else:
                    break
            except KeyboardInterrupt:
                exit()
            except ValueError:
                print("use intagers")

        ttl = list(inp1)
        shift = inp2
        result = ""

        for char in ttl:
            if char in au:
                pos = au.index(char)
                pos_shift = (pos + shift) % 26
                result += au[pos_shift]
            elif char in al:
                pos = al.index(char)
                pos_shift = (pos + shift) % 26
                result += al[pos_shift]
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
    except KeyboardInterrupt:
        exit()
    except:
        print("error")