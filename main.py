class Calc_Handler():
    def input_handler(self, operation_dict):
        print(operation_dict)
        if operation_dict["operation_type"] == "+":
            return str(float(operation_dict["a_value"]) + float(operation_dict["b_value"]))
        if operation_dict["operation_type"] == "-":
            return str(float(operation_dict["a_value"]) - float(operation_dict["b_value"]))
        if operation_dict["operation_type"] == "/":
            return str(float(operation_dict["a_value"]) / float(operation_dict["b_value"]))
        if operation_dict["operation_type"] == "x":
            print(float(operation_dict["a_value"])
                  * float(operation_dict["b_value"]))
            return str(float(operation_dict["a_value"]) * float(operation_dict["b_value"]))
