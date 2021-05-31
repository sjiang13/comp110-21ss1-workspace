"""An example of a procedure.""" 

def print_repeat(line: str, repeats: int) -> None:
    """Print something multiple times"""
    i : int = 0
    while i < repeats:
        print(line)
        i += 1 
