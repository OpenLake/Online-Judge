import socket # pip等からインストール必要
import time

PORT = 10001 #10001 # 鍵管理機制御用ポート
BUFFER_SIZE = 2048 # 通常はこのままでよい。

while True: # 繰り返し用
    code = input('エンターで履歴1行読み出し：press enter SM => RA => ED ：') # SM000801000000
    if code == "exit":
        print("終了します")
        break

    code = "SM000801000000"
    code2 = list(code) # 入力された文字列を1文字ずつのリストに分解
    code3 = []
    for i in code2:
        bytec = ord(i) # 文字をASCIIの対応数字に変更、pythonでは10進数のまま扱う
        code3.append(bytec)

    crc = code3[0] ^ code3[1] # 10進数を2進数として処理してくれます。crc初期値として1バイト目と2バイト目のXOR
    for j in range(2, len(code3)):
        crc = crc ^ code3[j] # 前のXOR値に対して3バイト目以降のXORを繰り返す。戻り値は10進数
    if len(hex(crc).replace('0x',"")) == 1: # 戻り値が15以内の時、一桁になってしまうので回避
    	crc = "0" + hex(crc).replace('0x',"")
    else: # 戻り値が16以上の時はそのまま16進数文字列に
    	crc = hex(crc).replace('0x',"")
    #print(crc)
    codeA = "RA002301000000000000000000000"
    code2 = list(codeA) # 入力された文字列を1文字ずつのリストに分解
    code3 = []
    for i in code2:
        bytec = ord(i) # 文字をASCIIの対応数字に変更、pythonでは10進数のまま扱う
        code3.append(bytec)

    crcA = code3[0] ^ code3[1] # 10進数を2進数として処理してくれます。crc初期値として1バイト目と2バイト目のXOR
    for j in range(2, len(code3)):
        crcA = crcA ^ code3[j] # 前のXOR値に対して3バイト目以降のXORを繰り返す。戻り値は10進数
    if len(hex(crcA).replace('0x',"")) == 1: # 戻り値が15以内の時、一桁になってしまうので回避
        crcA = "0" + hex(crcA).replace('0x',"")
    else: # 戻り値が16以上の時はそのまま16進数文字列に
        crcA = hex(crcA).replace('0x',"")

    codeB = "ED000201"
    code2 = list(codeB) # 入力された文字列を1文字ずつのリストに分解
    code3 = []
    for i in code2:
        bytec = ord(i) # 文字をASCIIの対応数字に変更、pythonでは10進数のまま扱う
        code3.append(bytec)

    crcB = code3[0] ^ code3[1] # 10進数を2進数として処理してくれます。crc初期値として1バイト目と2バイト目のXOR
    for j in range(2, len(code3)):
        crcB = crcB ^ code3[j] # 前のXOR値に対して3バイト目以降のXORを繰り返す。戻り値は10進数
    if len(hex(crcB).replace('0x',"")) == 1: # 戻り値が15以内の時、一桁になってしまうので回避
        crcB = "0" + hex(crcB).replace('0x',"")
    else: # 戻り値が16以上の時はそのまま16進数文字列に
        crcB = hex(crcB).replace('0x',"")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('172.26.0.52', PORT)) # 鍵管理機のIP情報とポート情報
        data = code + crc # 平文入力に対して算出したCRCを16進数として付加
        s.send(data.encode()) # ASCII(utf-8範囲内なので同義)にエンコードして鍵管理機へ送信
        time.sleep(0.5)
        print(s.recv(BUFFER_SIZE).decode() + " <=") # 応答コードを表示、応答が早すぎて拾いきれない時がある。
        data = codeA + crcA # 平文入力に対して算出したCRCを16進数として付加
        s.send(data.encode()) # ASCII(utf-8範囲内なので同義)にエンコードして鍵管理機へ送信
        time.sleep(0.5)
        print(s.recv(BUFFER_SIZE).decode() + " <=") # 応答コードを表示、応答が早すぎて拾いきれない時がある。
        data = codeB + crcB # 平文入力に対して算出したCRCを16進数として付加
        s.send(data.encode()) # ASCII(utf-8範囲内なので同義)にエンコードして鍵管理機へ送信
        time.sleep(0.5)
        print(s.recv(BUFFER_SIZE).decode() + " <=") # 応答コードを表示、応答が早すぎて拾いきれない時がある。

"""with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('172.26.0.2', 5000)) # 自PCのIP情報とポート情報
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                print('data : {}'.format(data))
                if data == b'RN0002011F':
                    conn.sendall(b'SM00080100000017')
                    time.sleep(0.5)
                    recv = conn.recv(BUFFER_SIZE)
                    print(recv.decode())
                    if recv == b'RM000401001A':
                        while recv.decode().startswith('RR'):
                            conn.sendall(b'RA00230100000000000000000000023')
                            time.sleep(0.5)
                            recv = conn.recv(BUFFER_SIZE)
                            print(recv.decode())
                        conn.sendall(b'ED00020102')
                        time.sleep(0.5)
                        recv = conn.recv(BUFFER_SIZE)
                        print(recv.decode())
                    else:
                        print("RMがこない")
                
                if data == b'SM00080100000017':
                    conn.sendall(b'RM000401001A')
                elif data == b'SM0008\xff\xff\xff\xff\xff\xff\xff\xff16':
                    conn.sendall(b'RM000403111A')
                elif data == b'HZ0010010000000012':
                    conn.sendall(b'HR00020102')
                elif data == b'ZZ000901000000038':
                    conn.sendall(b'ZR00030103A')
                elif data == b'SM00080200000014':
                    conn.sendall(b'RM000402001A')
                elif data == b'HZ0010020000000011':
                    conn.sendall(b'HR00020202')
                else:
                    conn.sendall(b'\x15')
"""

"""
例文や応答例

SM000801000000 をTCP/IPにて送信
機器からの応答 RM000401001A
CN001401200702180000 をTCP/IPにて送信
機器からの応答 ・ 機器の時刻が変更される
ED000201 をTCP/IPにて送信
機器からの応答 ・

"""