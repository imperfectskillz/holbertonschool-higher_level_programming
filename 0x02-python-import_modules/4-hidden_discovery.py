#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    hidden = dir(hidden_4)
    for i in len(hidden):
        if hidden[i][0:1] != "_":
            print("{}".format(hidden[i]))
