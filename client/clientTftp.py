from cgi import print_form, test
import sys

from client.pypoller import poller
from client.protobuf import msg_pb2
from socket import *
import os


class ClientTFTP(poller.Callback):
    """Construtor do Cliente TFTP

    @param ip: String contendo o ip do Cliente
    @param port: Inteiro contendo porta do Cliente
    @param tout: Valor do Timeout
    """
    def __init__(self, ip: str, port: int, tout: float):
        self.__ip = ip
        self.__port = port
        self.__tout = tout

        self.__socket = socket(AF_INET, SOCK_DGRAM)
        poller.Callback.__init__(self, self.__socket, self.__tout)

        self.__n = 0

        self.__max_n = 0
        self.__msg_size = 0
        self.__mode = "NetAscii"
        self.__fname = None

    """Requisição de leitura do TFTP
    
    @param fname: Nome do Arquivo
    @param mode: contém o modo de formato, onde pode ser as Strings "netascii", "octet", or "mail"
    """
    def get(self, fname: str, mode: str):
        # Envia mensagem de RRQ
        # fazer codificação de mensagem RRQ
        m = msg_pb2.Mensagem()
        msg = m.rrq
        self.__fname = fname
        msg.fname = fname
        if (mode.lower() == 'netascii'):
            msg.mode = msg_pb2.Mode.netascii
        elif (mode.lower() == 'octet'):
            msg.mode = msg_pb2.Mode.octet
        else:
            msg.mode = msg_pb2.Mode.mail
        
        self.__n = 1
        # cria o arquivo para escrita de bytes
        self.__file = open("./" + self.__fname, "wb" )
        print("Mensagem Get = ", m.SerializeToString())
        self.__socket.sendto(m.SerializeToString(), (self.__ip, self.__port))

        # Instancia Poller
        self.enable()
        self.enable_timeout()
        sched = poller.Poller()

        # Despache e mudança de estado
        self.__state = self.__handle_connect
        sched.adiciona(self)
        sched.despache()

    """Requisição de escrita do TFTP

    @param fname: Nome do Arquivo
    @param mode: contém o modo de formato, onde pode ser as Strings "netascii", "octet", or "mail"
    """
    def put(self, fname: str, mode: str):
        # fazer codificação de mensagem WRQ
        m = msg_pb2.Mensagem()
        msg = m.wrq
        self.__fname = fname
        msg.fname = fname
        if (mode.lower() == 'netascii'):
            msg.mode = msg_pb2.Mode.netascii
        elif (mode.lower() == 'octet'):
            msg.mode = msg_pb2.Mode.octet
        else:
            msg.mode = msg_pb2.Mode.mail
        
        self.__n = 1
        # cria o arquivo para leitura de bytes
        self.__file = open("./" + self.__fname, "rb")
        size = os.path.getsize("./" + self.__fname)
        self.__max_n = 1 + (size/512)  # Qtd de vezes q será feito a o enviado
        print("Mensagem Put = ", m.SerializeToString())
        self.__socket.sendto(m.SerializeToString(), (self.__ip, self.__port))

        # Instancia Poller
        self.enable()
        self.enable_timeout()
        sched = poller.Poller()

        # Despache e mudança de estado
        self.__state = self.__handle_connect
        sched.adiciona(self)
        sched.despache()

    """Requisição de listagem de Diretorios e Arquivos do TFTP 2.0

    @param path: Caminho do Arquivo
    """
    def list(self, path: str):
        m = msg_pb2.Mensagem()
        msg = m.list
        self.__listPath = path
        msg.path = self.__listPath

        
        print("Mensagem List = ", m.SerializeToString())
        self.__socket.sendto(m.SerializeToString(), (self.__ip, self.__port))

        # Instancia Poller
        self.enable()
        self.enable_timeout()
        sched = poller.Poller()

        # Despache e mudança de estado
        self.__state = self.__handle_connect_new
        sched.adiciona(self)
        sched.despache()

    """Requisição para criar de Diretorios do TFTP 2.0

    @param path: Caminho do Arquivo
    """
    def mkdir(self, path:str):
        m = msg_pb2.Mensagem()
        msg = m.mkdir
        self.__mkdirPath = path
        msg.path = self.__mkdirPath

        
        print("Mensagem Mkdir = ", m.SerializeToString())
        self.__socket.sendto(m.SerializeToString(), (self.__ip, self.__port))

        # Instancia Poller
        self.enable()
        self.enable_timeout()
        sched = poller.Poller()

        # Despache e mudança de estado
        self.__state = self.__handle_connect_new
        sched.adiciona(self)
        sched.despache()

    """Requisição para renomar Arquivos do TFTP 2.0

    @param origName: Nome original do Arquivo
    @param newName: Novo nome do Arquivo
    """
    def move(self, origName: str, newName: str):
        m = msg_pb2.Mensagem()
        msg = m.move
        self.__origName = origName
        self.__newName = newName
        msg.nome_orig = self.__origName
        msg.nome_novo = self.__newName

        print("Mensagem Move = ", m.SerializeToString())
        self.__socket.sendto(m.SerializeToString(), (self.__ip, self.__port))

        # Instancia Poller
        self.enable()
        self.enable_timeout()
        sched = poller.Poller()

        # Despache e mudança de estado
        self.__state = self.__handle_connect_new
        sched.adiciona(self)
        sched.despache()

    """Mudança de Estado para Conectando

    @param msg: Messagem utilizadas durante a troca de messagem
    """
    def __handle_connect(self, msg):
        # fazer decodificação de mensagem 
        # Se for ERROR
        #verificar agora o tipo de msg se é Error
        if (msg.WhichOneof('msg') == 'error'):
            error = msg.error.errorcode
            print(self.ErrorMsg(error))   
            sys.exit()

        # Se Receber um DATA (Significa que é RX)
        #verificar agora o tipo de msg se é DATA
        if (msg.WhichOneof('msg') == 'data'):
            data = msg.data.message
            #verificar tamanho do msg.data.block_n < 512
            if (len(data) < 512):
                block_n = self.__n
                sendMsg = msg_pb2.Mensagem()
                sendMsg.ack.block_n = block_n
                print('Ack = ', sendMsg.SerializeToString())
                self.__socket.sendto(sendMsg.SerializeToString(), (self.__ip, self.__port))
                # do Byte 4 em diante é o Data do arquivo
                self.__file.write(data)
                self.__state = self.__handle_end
            #verificar tamanho do msg.data.block_n < 512    
            if (len(data) == 512):
                block_n = self.__n
                sendMsg = msg_pb2.Mensagem()
                sendMsg.ack.block_n = block_n
                print('Ack = ', sendMsg.SerializeToString())
                self.__socket.sendto(sendMsg.SerializeToString(), (self.__ip, self.__port))
                self.__n += 1
                self.__file.write(data)
                self.__state = self.__handle_rx
        # Se Receber um ACK (Significa que é TX)
        #verificar agora o tipo de msg é ACK
        if (msg.WhichOneof('msg') == 'ack'):
            print("ACK")
            #ler msg.ack.block_n
            ack_n = msg.ack.block_n
            #ack_n = int.from_bytes(ack_n, 'big')
            # caso tamanho de msg.ack.block_n == 0
            if (ack_n == 0):
                sentData = self.__file.read(512)
                block_n = self.__n
                dataMsg = msg_pb2.Mensagem()
                dataMsg.data.message = sentData
                dataMsg.data.block_n = block_n
                print('Data = ', dataMsg.SerializeToString())
                self.__socket.sendto(dataMsg.SerializeToString(), (self.__ip, self.__port))
                self.__state = self.__handle_tx

    """Mudança de Estado para Conectando para Novas Mensagens TFTP. 
        Obs: Criado com inuito de diferenciar o ACK do WRQ do ACK do MKDIR

    @param msg: Messagem utilizadas durante a troca de messagem
    """
    def __handle_connect_new(self, msg):
        # fazer decodificação de mensagem 
        # Se for ERROR
        #verificar agora o tipo de msg se é Error
        if (msg.WhichOneof('msg') == 'error'):
            error = msg.error.errorcode
            print(self.ErrorMsg(error))   
            sys.exit()

        # Se for ACK, Houve Sucesso
        # Então fecha o programa.
        if (msg.WhichOneof('msg') == 'ack'):
            sys.exit()

        if (msg.WhichOneof('msg') == 'list_resp'):
            resp = msg.list_resp.items
            if(len(resp)>0):
                for item in resp:
                    print("Item a ser Listado: ", item)
            else:
                print("Nada a ser listado.")        
            sys.exit()

    """Mudança de Estado para Recepção

    @param msg: Messagem utilizadas durante a troca de messagem
    """
    def __handle_rx(self, msg ):
        # fazer decodificação de mensagem
        # Se for ERROR
        # verificar agora o tipo de msg se é Error e verificar enum recebido igual a 5
        if (msg.WhichOneof('msg') == 'error'):
            error = msg.error.errorcode
            print(self.ErrorMsg(error))
            sys.exit()

        # Recebe Msg do socket
        # Se len do Data == 512, continua neste estado
        # envia Ack, incrementa n
        if ( (msg.WhichOneof('msg') == 'data') ):
            data = msg.data.message
            data_block_m = msg.data.block_n
            if((len(data) == 512)):
                # verificar se msg é DATA e setar block_n em msg.data 
                block_n = self.__n
                sendMsg = msg_pb2.Mensagem()
                sendMsg.ack.block_n = block_n
                print('Ack = ', sendMsg.SerializeToString())
                self.__socket.sendto(sendMsg.SerializeToString(), (self.__ip, self.__port))
                self.__n += 1
                self.__file.write(data)
                self.__state = self.__handle_rx
            elif (data_block_m != self.__n):
                block_n = data_block_m
                sendMsg = msg_pb2.Mensagem()
                sendMsg.ack.block_n = block_n
                print('Ack = ', sendMsg.SerializeToString())
                self.__socket.sendto(sendMsg.SerializeToString(), (self.__ip, self.__port))
                self.__file.write(data)
                self.__state = self.__handle_rx
            elif ( (len(data) < 512) ):
                # verificar se msg é DATA e setar block_n em msg.data 
                block_n = self.__n
                sendMsg = msg_pb2.Mensagem()
                sendMsg.ack.block_n = block_n
                print('Ack = ', sendMsg.SerializeToString())
                self.__socket.sendto(sendMsg.SerializeToString(), (self.__ip, self.__port))
                self.__file.write(data)
                print("Transferencia Concluida")
                self.__file.close()
                sys.exit()

    """Mudança de Estado para Transmissão

    @param msg: Messagem utilizadas durante a troca de messagem
    """
    def __handle_tx(self, msg ):
        # fazer decodificação de mensagem
        if((msg.WhichOneof('msg') == 'ack') ):
            ack_n = msg.ack.block_n
            #ack_n = int.from_bytes(ack_n, "big")
        else:
            print('Não é Ack, abortando transferencia')
            sys.exit()

        if ((ack_n == self.__n) and (self.__n < (self.__max_n - 1))):
            self.__n += 1
            sendData = self.__file.read(512)
            block_n = self.__n
            dataMsg = msg_pb2.Mensagem()
            dataMsg.data.message = sendData
            dataMsg.data.block_n = block_n
            print('Data = ', dataMsg.SerializeToString())
            self.__socket.sendto(dataMsg.SerializeToString(), (self.__ip, self.__port))
            self.__state = self.__handle_tx
        elif (ack_n and (self.__n == (self.__max_n - 1))):
            self.__n += 1
            sendData = self.__file.read(512)
            block_n = self.__n
            dataMsg = msg_pb2.Mensagem()
            dataMsg.data.message = sendData
            dataMsg.data.block_n = block_n
            print('Data = ', dataMsg.SerializeToString())
            self.__socket.sendto(dataMsg.SerializeToString(), (self.__ip, self.__port))
            self.__state = self.__handle_end

    """Mudança de Estado para Fim

    @param msg: Messagem utilizadas durante a troca de messagem
    """
    def __handle_end(self, msg ):
        # deve-se fazer decodificação
        # Se for ERROR
        # verificar agora o tipo de msg se é Error e verificar enum recebido igual a 5
        if (msg.WhichOneof('msg') == 'error'):
            error = msg.error.errorcode
            print(self.ErrorMsg(error))
            sys.exit()

        if ((msg.WhichOneof('msg') == 'data') and (len(msg.data.message))):
            block_n = self.__n
            sendMsg = msg_pb2.Mensagem()
            sendMsg.ack.block_n = block_n
            print('Ack = ', sendMsg.SerializeToString())
            self.__socket.sendto(sendMsg.SerializeToString(), (self.__ip, self.__port))
            self.__file.close()
            sys.exit()
        elif ((msg.WhichOneof('msg') == 'ack') and (msg.ack.block_n() != None)):
            self.__n += 1
            sendData = self.__file.read(512)
            block_n = self.__n
            dataMsg = msg_pb2.Mensagem()
            dataMsg.data.message = sendData
            dataMsg.data.block_n = block_n
            print('Data = ', dataMsg.SerializeToString())
            self.__socket.sendto(dataMsg.SerializeToString(), (self.__ip, self.__port))
            sys.exit()

    def handle(self):
        # fazer decodificação de mensagem

        data, (addr, port) = self.__socket.recvfrom(1024)
        self.__port = port
        # transformar data em objeto mensagem
        # verificar mensagem se é do tipo DATA e chamar SerializeToString
        if type(data) is bytes:
            
            print("Recebido Mensagem do " + str(addr) + ":" + str(port) + " = ", data)
            recvMsg = msg_pb2.Mensagem()
            recvMsg.ParseFromString(data) 
              
        else:
            print("Mensagem recebida não esta em bytes: " + str(data))
            print("Abortanto execução do Cliente")
            sys.exit()

        # maquina de Estados
        self.__state(recvMsg)

    def handle_timeout(self):
        print("Timeout")
        self.disable_timeout()
        self.disable()
        # maquina de estado passar para ociso

    """Retorna uma Mensagem de Erro, apartir de seu código

    @param code: Código da Messagem de Erro utilizadas na troca de mensagens
    """    
    def ErrorMsg(self, code:int):
        if code == 0:
            return "" #Sucesso
        if code == 1:
            return "File not found."
        if code == 2:
            return "Access violation."
        if code == 3:
            return "Disk full or allocation exceeded."
        if code == 4:
            return "Illegal TFTP operation."
        if code == 5:
            return "Unknown transfer ID."
        if code == 6:
            return "File already exists." 
        if code == 7:
            return "No such user."
        return "Not defined, see error message (if any)."