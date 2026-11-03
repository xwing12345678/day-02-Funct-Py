#E1
def format_receipt(items:list[tuple[str,int|float]])->str:
    
    def line(name:str, price:[int|float]):