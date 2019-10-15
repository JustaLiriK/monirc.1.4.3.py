# -*- coding: utf-8 -*-
#version 1.4.3
import socket, sys , string , re
from string import Template
#qpy:console
global server, recu, envoi, done, soc, buff, connect, data
global pseudo , nick
#choisissons nous un pseudo
pseudo = raw_input('Entrez votre pseudo: ')
#pseudo = i + "\r"
if pseudo == 'exit()':
    sys.exit()
else:
    nick = pseudo
print ('pseudo=' + nick)

#entrons le serveur à joindre
y = raw_input('Entrez un nom de serveur: ')
#valid = y + "\r"
valid = y


print ('hostname=' + valid)
if valid == 'exit()':
    sys.exit()
#else : print hostindex, nick
else:
    hostname = valid

#recuperons le nom de l'hote
server = valid, 6667
buff = 1024
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def  reach(server, nick):
    soc.connect(server)
    soc.send("NICK " + nick + "\r")
    user = "USER " + nick + " jlk@192.168.1.1 192.168.1.1 debiel \r"
    print user
    soc.send(user)


#def  recept(buff):
 #   recu = soc.recv(buff)
  #  return recu
def  recept(buff):
    recu = soc.recv(buff)
    return recu


def  send(done):
    soc.send(done + "\r")


def  pingpong(data):
    data
    p= re.compile('PING')
    m=p.sub('PONG',data)
    print(m)
    soc.send(m)

connect = reach(server, nick)
data=recept(buff)
pingpong(data)
while True:
    data=recept(buff)
    pingpong(data)
    if len (data) > 0 :
       print  (data)
    done = raw_input('Tapez ici :')
    if done == 'exit()':
            soc.close()
            print 'connection fermee'
            sys.exit()
    if done == "\r ":
        continue
    else :
        send(done)
