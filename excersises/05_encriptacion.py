# Encriptar y desencriptar frases usando la clave MURCIELAGO. Cada letra de la frase que coincida con alguna letra de la clave se sustituye por un número siguiendo el orden 0123456789.

def get_encrypted(msg):
    SECRET = 'MURCIELAGO'
    CODE = {value: key for (key, value) in enumerate(SECRET)}

    encripted_msg = ''.join((list(map(lambda letter: str(CODE.get(
        letter)) if letter in CODE else letter, msg))))
    print(f'Message encrypted: \t{encripted_msg}')
    return encripted_msg


def run():
    inputs = ['MURCIELAGO', 'ABECEDARIO', 'HOLA',
              'HOTEL CALIFORNIA', input('GIVE A MESSAGE: ').upper()]
    res = list(map(lambda x: get_encrypted(x), inputs))
    print(res)


if __name__ == "__main__":
    run()
