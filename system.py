class CalculatorSystem():
    def __init__(self, display):
        self.operation = ''
        self.display = display

    def set_operation(self, operation):
        if self.display.get_text():
            self.operation = operation
            self.first = self.parse_display()
            self.display.clear()

    def reset(self):
        self.operation = ''
        self.display.clear()

    def operate(self):
        first = list(map(int, self.first))
        second = list(map(int, self.parse_display()))
        if self.operation:
            try:
                if self.operation == '+':
                    total = list(map(sum, zip(first, second)))
                elif self.operation == '-':
                    total = first[0] - second[0],  first[1] + second[1]
                elif self.operation == '*':
                    total = first[0] * second[0], second[0]*first[1]+first[0]*second[1]
                elif self.operation == '/':
                    total = first[0]/second[0], (second[0]**-1)*first[1]+(first[0]/(second[0])**2)*second[1]
            except ZeroDivisionError:
                total_str = 'err'
            else:
                total_str = '{}±{}'.format(total[0], total[1])
            self.display.set_text(total_str)
            self.operation = ''
    
    def parse_display(self):
        txt_display = self.display.get_text()
        parsed = txt_display.split('±')
        if len(parsed) < 2:
            return parsed[0], '0'
        return parsed
