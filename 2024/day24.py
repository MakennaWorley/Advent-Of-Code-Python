# day 24
import re

def parse_input(inputs):
    initial_values = {}
    gate_instructions = []

    for line in inputs.splitlines():
        if ":" in line:
            wire, value = line.split(": ")
            initial_values[wire] = int(value)

        elif "->" in line:
            gate_instructions.append(line)

    return initial_values, gate_instructions


def evaluate_gate(op, val1, val2):
    if op == "AND":
        return val1 & val2

    elif op == "OR":
        return val1 | val2

    elif op == "XOR":
        return val1 ^ val2


def simulate_circuit(initial_values, gate_instructions):
    wire_values = initial_values.copy()
    unresolved = gate_instructions[:]

    while unresolved:
        next_unresolved = []

        for instruction in unresolved:
            match = re.match(r"(\w+) (AND|OR|XOR) (\w+) -> (\w+)", instruction)
            if match:
                input1, op, input2, output = match.groups()
                if input1 in wire_values and input2 in wire_values:
                    wire_values[output] = evaluate_gate(op, wire_values[input1], wire_values[input2])

                else:
                    next_unresolved.append(instruction)

        unresolved = next_unresolved

    return wire_values


def compute_decimal_from_z(wire_values):
    z_wires = {k: v for k, v in wire_values.items() if k.startswith("z")}
    sorted_z_bits = [z_wires[f"z{str(i).zfill(2)}"] for i in range(len(z_wires))]
    binary_string = "".join(map(str, sorted_z_bits[::-1]))

    return int(binary_string, 2)


text = open('inputs/day24_input.txt').read().strip()

initial_values, gate_instructions = parse_input(text)
wire_values = simulate_circuit(initial_values, gate_instructions)
count = compute_decimal_from_z(wire_values)

print(count)

class CrossedWires:
    def __init__(self, filename: str):
        self.wires = {}
        self.gates = {}
        self._initialize_from_file(filename)


    def _initialize_from_file(self, filename: str):
        text = open(filename, encoding='utf-8').read().strip()
        for line in text.splitlines():
            if ":" in line:
                wire, value = line.split(": ")
                self.wires[wire] = int(value)

            elif "->" in line:
                if match := re.match(r'(\w+) (AND|OR|XOR) (\w+) -> (\w+)', line):
                    input1, operation, input2, output = match.groups()
                    self.gates[output] = (input1, operation, input2)


    def simulate(self):
        while True:
            progress = False

            for output, (input1, operation, input2) in self.gates.items():
                if output in self.wires:
                    continue

                if input1 in self.wires and input2 in self.wires:
                    value1 = self.wires[input1]
                    value2 = self.wires[input2]
                    self.wires[output] = self.compute_gate(value1, value2, operation)
                    progress = True

            if not progress:
                break


    @staticmethod
    def compute_gate(input1: int, input2: int, operation: str) -> int:
        if operation == 'AND':
            return input1 & input2

        elif operation == 'OR':
            return input1 | input2

        elif operation == 'XOR':
            return input1 ^ input2


    def find_swapped_wires(self) -> str:
        wrong = []
        highest_z = max((key for key in self.gates if key.startswith('z')), default='')

        for output, (input1, operation, input2) in self.gates.items():
            if (
                (output.startswith('z') and operation != 'XOR' and output != highest_z) or
                (operation == 'XOR' and not self.valid_xor_inputs(output, input1, input2)) or
                (operation == 'AND' and self.invalid_and_inputs(output, input1, input2)) or
                (operation == 'XOR' and self.xor_feeds_or(output))
            ):
                wrong.append(output)

        return ','.join(sorted(set(wrong)))


    def valid_xor_inputs(self, output: str, input1: str, input2: str) -> bool:
        prefixes = ('x', 'y', 'z')
        return output.startswith(prefixes) or input1.startswith(prefixes) or input2.startswith(prefixes)


    def invalid_and_inputs(self, output: str, input1: str, input2: str) -> bool:
        if input1 == 'x00' or input2 == 'x00':
            return False

        for sub_input1, sub_op, sub_input2 in self.gates.values():
            if (output == sub_input1 or output == sub_input2) and sub_op != 'OR':
                return True

        return False


    def xor_feeds_or(self, output: str) -> bool:
        for sub_input1, sub_op, sub_input2 in self.gates.values():
            if (output == sub_input1 or output == sub_input2) and sub_op == 'OR':
                return True

        return False


if __name__ == "__main__":
    input_file = 'inputs/day24_input.txt'

    try:
        crossed_wires = CrossedWires(input_file)
        crossed_wires.simulate()
        print(crossed_wires.find_swapped_wires())
    except RuntimeError as e:
        print(f"Error: {e}")