import paho.mqtt.client as mqtt

# --- Configurações do MQTT ---
# O endereço IP do broker Mosquitto rodando no seu computador.
# "localhost" funciona se o broker estiver na sua máquina.
# Se o broker estiver em outra máquina, substitua por seu IP.
mqtt_broker_address = "test.mosquitto.org" 
mqtt_port = 1883
mqtt_topic = "sensores/loraALGUMACOISADAMINHACABEÇA3005"

# --- Funções de callback ---
def on_connect(client, userdata, flags, rc):
    """
    Função chamada quando o cliente se conecta ao broker.
    rc=0 significa sucesso.
    """
    if rc == 0:
        print("Conectado ao broker MQTT com sucesso!")
        # Inscreve-se no tópico assim que a conexão é estabelecida
        client.subscribe(mqtt_topic)
        print(f"Inscrito no tópico: '{mqtt_topic}'")
    else:
        print(f"Falha na conexão. Código de retorno: {rc}")

def on_message(client, userdata, msg):
    """
    Função chamada quando uma mensagem é recebida do broker.
    """
    # Decodifica o payload (conteúdo da mensagem) para string
    mensagem_recebida = msg.payload.decode()
    print(f"--- Nova mensagem recebida ---")
    print(f"Tópico: {msg.topic}")
    print(f"Payload: {mensagem_recebida}")
    print(f"----------------------------")

# --- Lógica principal ---
# Cria uma instância do cliente MQTT
client = mqtt.Client()

# Associa as funções de callback ao cliente
client.on_connect = on_connect
client.on_message = on_message

try:
    # Conecta-se ao broker MQTT
    client.connect(mqtt_broker_address, mqtt_port, 60)
    
    # Inicia o loop para processar callbacks e manter a conexão
    # Este loop irá rodar indefinidamente até o programa ser encerrado
    client.loop_forever()

except ConnectionRefusedError:
    print(f"Erro: Conexão recusada. Verifique se o broker Mosquitto está rodando em '{mqtt_broker_address}'.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
