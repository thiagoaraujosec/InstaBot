from instabot import Bot
import time

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
bot = Bot()
user = str(input(Blue+"\nPon tu nombre de usuario = "+Reset))
#Login Bot
passwd = str(input(Blue+"\nPon tu contraseña = "+Reset))
try:
    bot.login(username=user, password=passwd)
    print(Blue+"\n[+]Sesion iniciada correctamente"+Reset)
except:
    print(Red+"\n[-]No se pudo iniciar sesion,intentelo de nuevo"+Reset)
   
def opcion():
    print(Blue+"Que quieres hacer? :"+Reset)
    print(Blue+"\n1-Dejar de seguir a los que no me siguen "+Reset)
    time.sleep(0.6)
    print(Blue+"\n2-Seguir a tus seguidores "+Reset)
    time.sleep(0.6)
    print(Blue+"\n3-Seguir a las personas que sigue una cuenta "+Reset)  
    time.sleep(0.6)
    print(Blue+"\n4-Dejar de seguir a todos "+Reset)
    time.sleep(0.6)
    print(Blue+"\n5-Mandar mensaje a una persona "+Reset)
    time.sleep(0.6)
    print(Blue+"\n6-Comentar una publicacion"+Reset)
    time.sleep(0.6)
    print(Blue+"\n7-Sacar informacion de un usuario de Instagram"+Reset )
    time.sleep(0.6)
    print(Blue+"\nIngrese la opcion a elegir"+Reset)
    time.sleep(0.2)
    opc = input(Blue+"\n==>> "+Reset)
    if opc == "1":
        unfollownon()
    elif opc == "2":
        seguirseg()
    elif opc == "3":
        seguirper()
    elif opc == "4":
        unfollow()
    elif opc == "5":
        mensaje()
    elif opc == "6":
        comentar()
    elif opc == "7":
        info()  
    else:
        print(Blue+"Opcion invalida")
        opcion()
def unfollownon():
    print(Blue+"Estas seguro que quieres hacer esto?\n1-SI\n2-NO"+Reset)
    opc = str(input(Blue+"==>> "+Reset))
    if opc == "1":
        bot.unfollow_non_followers()
    elif opc == "2":
        opcion()
def seguirseg():
    print(Blue+"Estas seguro que quieres hacer esto?\n1-SI\n2-NO"+Reset)
    opc = str(input(Blue+"==>> "+Reset))
    if opc == "1":
        bot.follow_followers(user)
    elif opc == "2":
        opcion()
def seguirper():
    print(Blue+"Estas seguro que quieres hacer esto?\n1-SI\n2-NO"+Reset)
    opc = str(input(Blue+"==>> "+Reset))
    if opc == "1":
        persona = str(input(Blue+"A la cuenta de quien quieres seguir a los seguidos? = "+Reset))
        bot.follow_following(persona)
    elif opc == "2":
        opcion()
def unfollow():
    print(Blue+"Estas seguro que quieres hacer esto?\n1-SI\n2-NO"+Reset)
    opc = str(input(Blue+"==>> "+Reset))
    if opc == "1":
        bot.unfollow_everyone()
    elif opc == "2":
        opcion()
def mensaje():
    print(Blue+"A que cuenta le quieres mandar el mensaje?"+Reset)
    persona = str(input(Blue+"==>>"+Reset))
    print(Blue+"Que mensaje quieres enviar"+Reset) 
    mensaje = input(Blue+"==>>"+Reset)
    bot.send_message(mensaje,persona)
def comentar():
    link = str(input(Blue+"\nPon el link de la publicacion a comentar = "+Reset))
    id_media = bot.get_media_id_from_link(link)
    comentario = str(input(Blue+"\nQue quieres comentar? = "+Reset))
    comentarios = int(input(Blue+"\nPon la cantidad de comentarios que quieres hacer = "+Reset))
    count = 0
    while True:
        bot.comment(id_media,comentario)
        count += 1
        if count >= comentarios:
            break
def info():
    print(Blue+"A que cuenta le quieres sacar informacion?"+Reset)
    persona = str(input(Blue+"==>>"+Reset))
    info = bot.get_user_info(persona)
    nombre = info['username']
    full_name = info['full_name']
    bio = info['biography']
    seguidores = info['follower_count']
    seguidos = info['following_count']
    profile = info['hd_profile_pic_versions']
    publicaciones = info['media_count']
    url = info['external_url']
    try:
        email = info['public_email']
    except:
        pass
    account_id = info['pk']
    privada = info['is_private']
    verificado = info['is_verified']
    try:
        numero = info['public_phone_number']
        ciudad = info['city_name']
    except:
        pass
    print(Blue+f"\nNombre de usuario:{nombre}"+Reset)
    print(Blue+f"\nNombre completo:{full_name}"+Reset)
    print(Blue+f"\nBiografia:{bio}"+Reset)
    print(Blue+f"\nSeguidores:{seguidores}"+Reset)
    print(Blue+f"\nSeguidos:{seguidos}"+Reset)
    print(Blue+f"\nFoto de perfil:{profile}"+Reset)
    print(Blue+f"\nPublicaciones:{publicaciones}"+Reset)
    print(Blue+f"\nUrl del perfil:{url}"+Reset)
    try:
        print(Blue+f"\nEmail de la cuenta:{email}"+Reset)
    except:
        pass
    print(Blue+f"\nId de la cuenta:{account_id}"+Reset)
    print(Blue+f"\nEs privada:{privada}"+Reset)
    print(Blue+f"\nVerificado:{verificado}"+Reset)
    try:
        print(Blue+f"\nNumero de telefono:{numero}"+Reset)
        print(Blue+f"\nCiudad:{ciudad}"+Reset)    
    except:
        pass
if __name__ == "__main__":
    opcion()