class RomanType:
    def __init__(self, user_input):
        self.rom_num = user_input.upper()
        self.int_val = self.int_conversion(user_input)

    def int_conversion(self, rom_num):
        rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_val = 0

        for numeral in reversed(rom_num):
            if numeral not in rom_dict:
                raise ValueError("Invalid Roman Numeral or INPUT. Please enter a valid Roman Numeral.")
            current_val = rom_dict[numeral]
            if current_val < prev_val:
                result -= current_val
            else:
                result += current_val
            prev_val = current_val

        return result

    def print_as_rom(self):
        print(f"The Roman numeral representation: {self.rom_num}")

    def print_as_int(self):
        print(f"The positive integer representation: {self.int_val}")


if __name__ == "__main__":
    while True:
        user_input = input("Enter a Roman numeral (Use ALL CAPS) or type 'exit' to quit: ")

        if user_input.lower() == 'exit':
            break

        rom_obj = RomanType(user_input)
        rom_obj.print_as_rom()
        rom_obj.print_as_int()
