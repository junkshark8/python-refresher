#echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    while repetitions > 0: #loop through repetitions
        i = -abs(repetitions) #negative count
        echo = text[i:] #echo starts with last 3 indices
        print(echo) 
        repetitions -= 1 #decrement repetitions left
    return "."


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))