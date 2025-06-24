import datetime
import psutil
import time

######### IMPORTANTE #########
### Precisamos baixar o psutil para o computador antes de executar.
### Para isso, executar o seguinte comando no terminal:
### pip install psutil
######### IMPORTANTE #########

class SistemaLogger:
    def __init__(self, nome_arquivo="log_sistema.txt"):
        self.nome_arquivo = nome_arquivo
        self.hora_inicio = datetime.datetime.now()
        self.escrever_log("Iniciando o registro de logs.\n")

    def escrever_log(self, mensagem):
        with open(self.nome_arquivo, "a") as arquivo:
            arquivo.write(mensagem)

    def registrar(self):
        agora = datetime.datetime.now()
        data_hora_atual = agora.strftime("%d/%m/%Y %H:%M:%S")
        uso_cpu = psutil.cpu_percent(interval=1)
        tempo_decorrido = (agora - self.hora_inicio).total_seconds()
        log_info = (f"Data e Hora: {data_hora_atual} - "
                    f"Uso de CPU: {uso_cpu}% - "
                    f"Tempo Decorrido: {tempo_decorrido} segundos\n")
        self.escrever_log(log_info)
        print(log_info)


# Uso da classe
logger = SistemaLogger()

print(f"Iniciando o registro de logs às {logger.hora_inicio.strftime('%H:%M:%S')}")
for _ in range(5):
    logger.registrar()
    time.sleep(1)  # Atraso para simular trabalho entre os registros

print("Registro de logs concluído.")