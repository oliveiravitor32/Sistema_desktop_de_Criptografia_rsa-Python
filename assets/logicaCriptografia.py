import random

from assets import tabelaValoresCaracteres


def criarNumeroPrimoAleatorio():
    # Função para gerar um número primo aleátorio de acordo com o range estipulado
    numeroPrimoAleatorio = 0
    verificador = False
    while (verificador == False):
        numeroPrimoAleatorio = random.randint(10, 100)
        for i in range(2, numeroPrimoAleatorio):
            if numeroPrimoAleatorio % i == 0:
                verificador = False
                break
            else:
                verificador = True

    return numeroPrimoAleatorio


def calcularMdc(a, b):
    # Cálculo do MDC, encerra o loop quando "B" for igual à 0
    while b:
        a, b = b, a % b
    return a


def calcularE(phiN):
    # Função para gerar "E" que seja primo e que o resultado do mdc(phiN,"E") seja == 1
    eAleatorio = 0
    verificador = False
    while (verificador == False):
        eAleatorio = criarNumeroPrimoAleatorio()
        if (eAleatorio <= 1 or eAleatorio >= phiN):
            continue
        else:
            calcularMdcE = calcularMdc(phiN, eAleatorio)
            if calcularMdcE == 1:
                verificador = True
            else:
                verificador = False
    return eAleatorio


def interfaceCriptografar(interfaceTextoDigitado):
    # Inicio gerando dois números primos e calculando as demais variáveis para o algoritmo RSA
    p = criarNumeroPrimoAleatorio()
    q = criarNumeroPrimoAleatorio()
    n = p * q
    phin = (p - 1) * (q - 1)
    # Calculando E  E == primo and mdc(phiN, e) == 1
    e = calcularE(phin)

    # Recebendo texto da interface
    textoUsuario = interfaceTextoDigitado

    # Array para salvar valores dos caractres criptografados
    arrayCaracteresCriptografados = []

    # Loop para verificar igualdade dos caracteres com os caracteres da tabela
    # e pegar o valor respectivo de cada caractere
    for caractere in textoUsuario:
        for itemTabela in tabelaValoresCaracteres.tabela:
            if (caractere == itemTabela[0]):
                valorLetra = itemTabela[1]
                caractereCodificado = (valorLetra ** e) % n
                arrayCaracteresCriptografados.append(caractereCodificado)
                break

    # Loop para descobrir o valor de "D" de acordo com a fórmula (d * e % phin == 1)
    loopD = 0
    calc = 0
    while calc != 1:
        loopD += 1
        calc = loopD * e % phin
    d = loopD

    # Objeto para salvar e transmitir dados importantes com fácil manuseamento
    class criptografia:
        def __init__(self, d, n, textoCriptografado):
            self.d = d
            self.n = n
            self.textoCriptografado = textoCriptografado

    resultadoRsa = criptografia(d, n, arrayCaracteresCriptografados)

    return resultadoRsa


def interfaceDescriptografar(interfaceChaves, interfaceCaracteresCriptografados):
    # Separar os valores "D" e "N" da chave privada
    chaves = interfaceChaves.strip().replace(" ", '').split("-")
    d = int(chaves[0])
    n = int(chaves[1])

    # Array para salvar valores dos caractres já descriptografados
    array_descriptografado = []

    # Loop calculo de descriptografia para cada valor de caractere criptografado
    for caractereCriptografado in interfaceCaracteresCriptografados:
        caractereDescriptografado = int(caractereCriptografado) ** d % n
        array_descriptografado.append(caractereDescriptografado)

    # String para salvar caractres já descriptografados em formato de texto
    mensagemFinalDescriptografada = ''

    # Loop para transformar os valores de caracteres descriptografados em texto
    for caractere in array_descriptografado:
        for itemTabela in tabelaValoresCaracteres.tabela:
            if (caractere == itemTabela[1]):
                mensagemFinalDescriptografada += itemTabela[0]

    return mensagemFinalDescriptografada
