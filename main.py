import cv2
import speech_recognition as sr
import database
import ftp_connection
import random
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Speak')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        if text == "help":
            name = hex(random.randrange(1, 999))
            print(text)
            camera = cv2.VideoCapture(0)
            return_value, image = camera.read()
            cv2.imwrite(name + '.png', image)
            details = ('https://www.google.com/maps/@30.1384505,77.2875395,19.91z', name + '.png')
            try:
                with database.con.cursor() as cur:
                    cur.execute('INSERT INTO test_table(name,image) VALUES(%s, %s)',
                                (details[0], details[1]))
                    database.con.commit()
                    print('data sent successfully')

            finally:
                database.con.close()
            del camera
            try:
                print("Logging in...")
                ftp_connection.ftp.login("project@webmaze.in", "Project@2021")
                file = open(name + ".png", "rb")
                ftp_connection.ftp.storbinary("STOR {0}.png".format(name), file)
                ftp_connection.ftp.close()
            except:
                "failed to login"
        else:
            print("Other Keyword")
    except:
        print('not found')
