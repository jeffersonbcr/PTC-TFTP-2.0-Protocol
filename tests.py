import sys
import logging as logger
from client import clientTftp

if len(sys.argv) == 0:
    print('No argument was passed, exiting test program.')
    sys.exit()

# Capture os argumentos necessários para usar o programa de teste TFTP.
try:
    IP_ = sys.argv[1]
    print('IP obtained by argument successfully') 
except Exception as Argument:
    print('Error. There is no IP passed by argument: \n', Argument)
    sys.exit()

try:
    PORT_ = int(sys.argv[2])
    print('PORT obtained by argument successfully') 
except Exception as Argument:
    print('Error. There is no PORT passed by argument: \n', Argument)
    sys.exit()

try:
    TIMEOUT_ = int(sys.argv[3])
    print('TIMEOUT obtained by argument successfully') 
except Exception as Argument:
    print('Error. There is no TIMEOUT passed by argument: \n', Argument)
    sys.exit()

# try:
#     FILENAME_ = sys.argv[5]
#     print('FILENAME obtained by argument successfully') 
# except Exception as Argument:
#     print('Error. There is no FILENAME passed by argument: \n', Argument)
#     sys.exit()

try:
    REQUEST_ = int(sys.argv[4])
    print('REQUEST obtained by argument successfully') 
except Exception as Argument:
    print('Error. There is no REQUEST passed by argument: \n', Argument)
    sys.exit()

MODE_ = "NetAscii"

# Inicia a classe do cliente TFTP com os argumentos obtidos. 
# Se REQUEST_ tem seu opcode = 1 é um RRQ, ou se REQUEST_ tem seu opcode = 2 é um WRQ.
# Se REQUEST_ tem seu opcode = 10 é um LIST, ou se REQUEST_ tem seu opcode = 12 é um MKDIR, ou se REQUEST_ tem seu opcode = 13 é um MOVE.
# Qualquer outra coisa é um argumento REQUEST_ inválido, então o Cliente TFTP deve lançar uma mensagem de erro se outro opcode diferente de 1 ou 2 estiver na solicitação.
CLIENT = clientTftp.ClientTFTP(IP_, PORT_, TIMEOUT_)

if REQUEST_ == 1:
    try:
        FILENAME_ = sys.argv[5]
        print('FILENAME obtained by argument successfully') 
    except Exception as Argument:
        print('Error. There is no FILENAME passed by argument: \n', Argument)
        sys.exit()
    try:
        CLIENT.get(FILENAME_, MODE_)
    except Exception as Argument:
        print('Error. Error got while reading using TFTP: \n', Argument)
        sys.exit()  
elif REQUEST_ == 2:
    try:
        FILENAME_ = sys.argv[5]
        print('FILENAME obtained by argument successfully') 
    except Exception as Argument:
        print('Error. There is no FILENAME passed by argument: \n', Argument)
        sys.exit()
    try:
        CLIENT.put(FILENAME_, MODE_)
    except Exception as Argument:
        print('Error. Error got while writing using TFTP: \n', Argument)
        sys.exit()
elif REQUEST_ == 10:
    try:
        PATH_ = sys.argv[5]
        print('PATH obtained by argument successfully') 
    except Exception as Argument:
        print('Error. There is no FILENAME passed by argument: \n', Argument)
        sys.exit()
    try:
        CLIENT.list(PATH_)
    except Exception as Argument:
        print('Error. Error got while writing using TFTP: \n', Argument)
        sys.exit()

elif REQUEST_ == 12:
    try:
        PATH_ = sys.argv[5]
        print('PATH obtained by argument successfully') 
    except Exception as Argument:
        print('Error. There is no FILENAME passed by argument: \n', Argument)
        sys.exit()
    try:
        CLIENT.mkdir(PATH_)
    except Exception as Argument:
        print('Error. Error got while writing using TFTP: \n', Argument)
        sys.exit()

elif REQUEST_ == 13:
    try:
        ORIGNAME_ = sys.argv[5]
        print('ORIGNAME obtained by argument successfully') 
    except Exception as Argument:
        print('Error. There is no FILENAME passed by argument: \n', Argument)
        sys.exit()
    try:
        NEWNAME__ = sys.argv[6]
        print('NEWNAME_ obtained by argument successfully') 
    except Exception as Argument:
        print('Error. There is no FILENAME passed by argument: \n', Argument)
        sys.exit()    
    try:
        CLIENT.move(ORIGNAME_, NEWNAME__)
    except Exception as Argument:
        print('Error. Error got while writing using TFTP: \n', Argument)
        sys.exit()                        
else:
    print('This is an invalid opcode for the TFTP request, the expected response is an error on both types of requests.') 
    