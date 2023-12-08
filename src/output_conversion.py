def output_converter(puzzle_output):
    formatted_output = ""
    for i in range(9):
        row = puzzle_output[i]
        formatted_row = f"{row[0:3]} | {row[3:6]} | {row[6:9]}"
        formatted_row = (
            str(formatted_row).replace("[", "").replace("]", "").replace(" ", "")
        )
        formatted_output += formatted_row + "\n"
        if (i % 3 == 2) and (i != 8):
            formatted_output += "---+---+---" + "\n"
    return formatted_output
