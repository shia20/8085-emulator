class CPU8085:
    def __init__(self):
        # Initialize the registers with zero
        self.registers = {
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0,
            'H': 0,
            'L': 0,
            'W': 0,
            'A': 0
        }

    def mov(self, dest, src):
        """
        Move the contents of the source register to the destination register.

        :param dest: The destination register (e.g., 'A', 'B', 'C', 'D', 'E', 'H', 'L')
        :param src: The source register (e.g., 'A', 'B', 'C', 'D', 'E', 'H', 'L')
        """
        if dest in self.registers and src in self.registers:
            self.registers[dest] = self.registers[src]
        else:
            raise ValueError("Invalid register name")

    def mvi(self, dest, data):

        if dest in self.registers:
            self.registers[dest] = data

    def lda(self, src):
        self.registers['A'] = src

    def lhld(self, src):

    def __str__(self):
        """
        Return the state of the CPU registers.
        """
        return str(self.registers)


