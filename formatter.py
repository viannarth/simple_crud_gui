import re
from datetime import datetime


def format_str(str_:str) -> str:
    return str_.upper().strip()

def format_num(num:str) -> str:
    pattern = r'[^\d]'
    return re.sub(pattern, '', num)

def is_valid_cpf_cnpj(num:str) -> bool:
    num = format_num(num)

    if len(num) != 11 and len(num) != 14:
        return False
        
    if len(num) == 11:
        cpf_sequence1 = [x for x in range(10, 1, -1)]
        sum_dv1 = sum([x * int(y) for x, y in zip(cpf_sequence1, num[:-2])])
        dv1 = 11 - (sum_dv1 % 11) if (sum_dv1 % 11 >= 2) else 0
        if int(num[-2]) != dv1: 
            return False
        
        cpf_sequence2 = [11] + cpf_sequence1
        sum_dv2 = sum([x * int(y) for x, y in zip(cpf_sequence2, num[:-1])])
        dv2 = 11 - (sum_dv2 % 11) if (sum_dv2 % 11 >= 2) else 0
        if int(num[-1]) != dv2: 
            return False
        
    else:
        cnpj_sequence1 = [x for x in range(5, 1, -1)] + [x for x in range(9, 1, -1)]
        sum_dv1 = sum([x * int(y) for x, y in zip(cnpj_sequence1, num[:-2])])
        dv1 = 11 - (sum_dv1 % 11) if (sum_dv1 % 11 >= 2) else 0
        if int(num[-2]) != dv1: 
            return False
        
        cnpj_sequence2 = [6] + cnpj_sequence1
        sum_dv2 = sum([x * int(y) for x, y in zip(cnpj_sequence2, num[:-1])])
        dv2 = 11 - (sum_dv2 % 11) if (sum_dv2 % 11 >= 2) else 0
        if int(num[-1]) != dv2: 
            return False

    return True

def is_valid_data_nascimento(data_nascimento:str) -> bool:
    num_data = format_num(data_nascimento)
    format = "%d%m%Y"

    try:
        datetime.strptime(num_data, format)
        return True
    except ValueError:
        return False

def is_valid_contato(contato:str) -> bool:
    num_contato = format_num(contato)

    if len(num_contato) != 11:
        return False
    
    return True


# Example of usage
def main():
    print("CPF/CNPJ:")
    print(is_valid_cpf_cnpj("81.303.380/0001-34"))
    print(is_valid_cpf_cnpj("81.303.380/0001-35\n"))

    print("Data de nascimento:")
    print(is_valid_data_nascimento("29/02/2006"))
    print(is_valid_data_nascimento("29-02-2020"))

if __name__ == "__main__":
    main()