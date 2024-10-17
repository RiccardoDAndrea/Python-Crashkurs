
# Im folgenden Arbeitsblatt geht es darum den Umgang mit IF ELIF und ELSE statements umzugehen. 
# Die essentziell sind bei jeder Programmiersprache.
# Aufgabe: Entwickelt ein Szenario, eine Geschichte oder eine Situtation wo ihr ein User Input erwartet 

# Erklärung: input("Hier kommt irgendein text z.B. eine Frage") 
#             ermöglicht es den User im Terminal eine eingabe zu betätigen
#
# .lower() verwandelt jeden String ob groß oder klein geschrieben in klein buchstaben das verhindert fehlerhafte eingaben.

# Beispiel Code:

# Benutzer nach Name und Alter fragen

user_name = input("Wie heißt du: ")
user_age = int(input("Wie alt bist du: "))
age_req = int(18)
healt = 10

# Überprüfen, ob der Benutzer volljährig ist
if user_age >= 18:
    print(f"Willkommen, {user_name}!")
    print("Du bist volljährig und kannst dich auf die Reise ins Horror-Haus begeben.")
    
    # Benutzer fragen, ob er bereit ist
    user_ready = input("Bist du bereit für die Reise? [j/n]: ").lower()

    if user_ready == "j":
        print("Dann lass uns loslegen!")
        print("Es war ein mal... ")
        enter_house = input(f"{user_name} sieht ein Verlassenes Haus willst du es betreten [j/n]").lower()

    else:
        print("Schade, vielleicht ein andermal!")
else:
    print(f"Es tut mir leid, {user_name}, du bist noch nicht 18.")
    print(f"Du bist erst {user_age} bitte komm wieder in {age_req - user_age} Jahren, wenn du alt genug bist!")







