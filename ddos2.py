import socket

def check_connection(ip_address, port):
    try:
        #Create socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        #Establish connection
            s.connect((ip_address, port))
        
            print(f"Successfully connected with {ip_address}:{port}")
        #Connection failed
            s.close()
    except Exception as e:
            print(f"Error connecting to {ip_address}:{port}: {e}")

if __name__ == "__main__":
    ip_address = "http://192.168.178.58/"  #Your IP
    port = 8080

check_connection(ip_address, port)
