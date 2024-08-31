memory_list = [0]*65536

registers = {
    "A" : 12,
    "B" : 0,
    "C" : 0,
    "D" : 0,
    "E" : 0,
    "H" : 0,
    "L" : 0
}

#Data transfer instructions

def mov(dest, src):
    registers[dest] = registers[src]

def mvn(dest, src):
    registers[dest] = ~registers[src]
    print(registers)

def mvi(dest,src):
    registers[dest] = src

def sta(location):
    registers["A"] = memory_list[location]

def lhld(location):
    registers["L"] = memory_list[location]
    location+=16
    registers["H"] = memory_list[location]

