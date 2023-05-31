def has_line(file_path: str) -> bool:
    with open(file_path, "r") as file:
        first_line = file.readline()
        if first_line:
            return True
        return False
        
def sum_values_in_file(file_path: str, category_especific:list=[]) -> float:
    total = 0.0
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                values = line.split(";")
                category = values[0]
                if category in category_especific:
                    try:
                        amountCategory = float(values[1])
                        total += amountCategory
                    except ValueError:
                        pass
                if len(category_especific) == 0:
                    amountCategory = float(values[1])
                    total += amountCategory
    return total