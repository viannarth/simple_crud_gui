import re
from datetime import datetime


def format_text(text:str | None) -> str | None:
    if text is None:
        return None
    
    pattern_spaces = r'\s+'
    text = re.sub(pattern_spaces, ' ', text)
    return text.upper().strip()

def format_num(num:str | None) -> str | None:
    if num is None:
        return None
    
    pattern = r'[\D]'
    return re.sub(pattern, '', num)

def format_cpf_cnpj(cpf_cnpj: str | None) -> str | None:
    if cpf_cnpj is None:
        return None

    num = format_num(cpf_cnpj)

    if len(num) == 11:
        cpf_formatted = f"{num[:3]}.{num[3:6]}.{num[6:9]}-{num[-2:]}"
        return cpf_formatted

    else:
        cnpj_formatted = f"{num[:2]}.{num[2:5]}.{num[5:8]}/{num[8:12]}-{num[-2:]}"
        return cnpj_formatted  
    
def format_data_nascimento(data_nascimento:str | None) -> str | None:
    if data_nascimento is None:
        return None
    
    num = format_num(data_nascimento)

    data_nascimento_formatted = f"{num[:2]}/{num[2:4]}/{num[-4:]}"
    return data_nascimento_formatted

def format_cep(cep:str | None) -> str | None:
    if cep is None:
        return None
    
    num = format_num(cep)

    cep_formatted = f"{num[:5]}-{num[-3:]}"
    return cep_formatted

def format_contato(contato:str | None) -> str | None:
    if contato is None:
        return None
    
    num = format_num(contato)

    contact_formatted = f"({num[:2]}) {num[2:7]}-{num[-4:]}"
    return contact_formatted

def is_valid_text(text:str) -> bool:
    pattern = r'[^A-Za-zÀ-ÖØ-öø-ÿ\s0-9]'
    return False if re.search(pattern, text) else True

def is_valid_num(num:str) -> bool:
    pattern = r'[\D]'
    return False if re.search(pattern, num) else True

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

    if len(num_data) != 8:
        return False

    year = int(num_data[-4:])

    if year < 1900 or year > 2026:
        return False

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

def is_valid_cep(cep:str) -> bool:
    num_cep = format_num(cep)

    if len(num_cep) != 8:
        return False
    
    return True

# Example of usage
def main():
    # Formatting CPF
    cpf = "12345678901"
    print("Unformatted CPF:", cpf)
    print("Formatted CPF:", format_cpf_cnpj(cpf))

    # Formatting birth date
    data_nascimento = "01012000"
    print("Unformatted birth date:", data_nascimento)
    print("Formatted birth date:", format_data_nascimento(data_nascimento))

    # Formatting CEP
    cep = "12345678"
    print("Unformatted CEP:", cep)
    print("Formatted CEP:", format_cep(cep))

    # Formatting contact
    contato = "12987654321"
    print("Unformatted contact:", contato)
    print("Formatted contact:", format_contato(contato))

    # Validating text
    print("Validating text:")
    print(is_valid_text("Abóbora"))
    print(is_valid_text("Example@"))

    # Validating CPF/CNPJ
    print("Validating CPF/CNPJ:")
    print(is_valid_cpf_cnpj("81.303.380/0001-34"))
    print(is_valid_cpf_cnpj("81.303.380/0001-35"))

    # Validating birth date
    print("Validating birth date:")
    print(is_valid_data_nascimento("29/02/2006"))
    print(is_valid_data_nascimento("29/02/2020"))

if __name__ == "__main__":
    main()