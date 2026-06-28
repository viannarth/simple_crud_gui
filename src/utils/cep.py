import requests


def get_cep(cep:str) -> dict[str, str]:

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        request = requests.get(url)

        request.raise_for_status()
    
        data = request.json()

        return data
    
    except requests.exceptions.RequestException as e:
        raise e

# Example of usage
def main():
    # Valid correct CEP
    data1 = get_cep("01001000")
    print(data1)

    # Valid, but incorrect CEP
    data2 = get_cep("12345678")
    print(data2)

    # Invalid CEP (raises a bad request error)
    data3 = get_cep("123")
    print(data3)

if __name__ == "__main__":
    main()