from TextVexMicro import textVex
import micropython
keypadTimerFreq = 60
def vex():
    global keypadTimerFreq
    micropython.alloc_emergency_exception_buf(100)
    app = textVex("Calculator Vex", keypadTimerFreq)
    app.mainLoop()

#if __name__ == "__main__":
#    vex()

def test():
    global keypadTimerFreq
    from Keypad import *
    print("test(): start")

    micropython.alloc_emergency_exception_buf(100)
    keys = [
            '1', '2', '3', 'A',
            '4', '5', '6', 'B',
            '*', '0', '#', 'D',
            '7', '8', '9', 'C',
           ]

    keypad = Keypad(['PE10', 'PE9', 'PE8', 'PE7'], \
            ['PE14', 'PE13', 'PE12', 'PE11'], keypadTimerFreq)
    hstry = None
    try:
        #for i in range(10000):
        while True:
            key = keypad.get_key()
            if key != None:
                key = keys[key]
                print(key, end='')
                if hstry == '*' and key == '*':
                    break
                hstry = key
            delay(1)
    except Exception as ex:
        pass

