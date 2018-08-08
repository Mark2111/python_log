import time

def print_calc(x, operation, y, result):
    print x, operation, y, "=", result

def log(x, operation, y, result):
    tim = time.ctime()
    print_calc(x, operation, y, result)
    f = open("log.txt", "a")
    f.write("New Log %s\n%s %s %s = %.2f\n" % (tim, x, operation, y, result))



def main():
    unos = False
    try:
        while unos != True:
            f = open("log.txt","a")
            print "Input numbers with operation ('x + y') !"
            try:
                x, operation, y = raw_input().split(' ')
            except ValueError:
                print "Input format: '<num> <operation> <num>'"
                continue
            if operation == "+":
                try:
                    result = float(x) + float(y)
                except ValueError:
                    print "Wrong input"
                    continue
                log(x, operation, y, result)
                unos = True
            elif operation == "-":
                try:
                    result = float(x) - float(y)
                except ValueError:
                    print "Wrong input"
                    continue
                log(x, operation, y, result)
                unos = True
            elif operation == "*" or operation == "x":
                try:
                    result = float(x) * float(y)
                except ValueError:
                    print "Wrong input"
                    continue
                log(x, operation, y, result)
                unos = True
            elif operation == "/":
                try:
                    result = float(x) / float(y)
                except ValueError:
                    print "Wrong input"
                    continue
                log(x, operation, y, result)
                unos = True
            else:
                print "Unknown input !!"
    except KeyboardInterrupt:
        print "\nGoodbye !!!"

if __name__ == "__main__":
    main()
