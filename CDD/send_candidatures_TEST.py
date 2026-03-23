import smtplib
import ssl
import time
import csv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
import random

# ============================================================
# ⚙️ НАЛАШТУВАННЯ — змінюй тільки цей блок
# ============================================================

YOUR_EMAIL = "nikita.chumak@insa-lyon.fr"     # Твій email INSA
YOUR_PASSWORD = "AmNCV391@Nikita"            # Пароль від email INSA
YOUR_NAME = "Nikita Chumak"                   # Твоє повне ім'я
YOUR_PHONE = "+33 7 68 75 99 63"              # Твій номер телефону

CV_PATH = "/media/tuktuk/Shared1/cours_S2_A1/Project1_G1/CDD/CV_Nikita.pdf"                     # Шлях до CV (PDF)
LM_PATH = "/media/tuktuk/Shared1/cours_S2_A1/Project1_G1/CDD/LM_Nikita.pdf"                     # Шлях до LM (PDF)
LOG_FILE = "log_envois.csv"                   # Лог-файл

SMTP_SERVER = "partage.insa-lyon.fr"          # SMTP сервер INSA Lyon (Zimbra)
SMTP_PORT = 587                               # Port TLS

# Затримка між мейлами (в секундах) — рандомна щоб не потрапити в спам
DELAY_MIN = 45
DELAY_MAX = 120

# ============================================================
# 📋 СПИСОК АГЕНТСТВ
# ============================================================

agencies = [
    {
        "name": "RAS Intérim Toulouse",
        "email": "toulouse@ras-interim.fr",
        "intro": "Votre agence RAS Intérim, reconnue pour ses missions dans le transport et la logistique à Toulouse, correspond exactement à mon profil et à ma recherche."
    },
    {
        "name": "Manpower Toulouse Industrie",
        "email": "toulouse-industrie-services@manpower.fr",
        "intro": "Votre agence Manpower Toulouse Industrie, active dans les secteurs de la logistique, de la production et de l'aéronautique à Colomiers et en région toulousaine, me semble idéale pour ma recherche."
    },
    {
        "name": "PROMAN Toulouse",
        "email": "toulouse.2@proman-interim.com",
        "intro": "Votre agence PROMAN, spécialisée notamment dans les missions en entrepôt et manutention à Toulouse, me semble tout à fait adaptée à ma recherche de CDD ou mission d'intérim cet été."
    },
    {
        "name": "Network Intérim Toulouse",
        "email": "toulouse@network-interim.com",
        "intro": "Votre agence Network Intérim, implantée localement à Toulouse et active dans le secteur de la logistique et de l'industrie, correspond parfaitement à mon profil."
    },
    {
        "name": "Supplay Toulouse Logistique",
        "email": "toulouse@supplay.fr",
        "intro": "Votre agence Supplay, spécialisée dans la logistique, les commerces et l'agroalimentaire à Toulouse, correspond tout à fait au type de poste d'exécution en équipe que je recherche pour cet été."
    },
    {
        "name": "Randstad Toulouse Industrie",
        "email": "toulouse.001v91@randstad.fr",
        "intro": "Votre agence Randstad Toulouse, active dans les secteurs de l'industrie et de la logistique, me semble particulièrement adaptée à ma recherche de mission de manutentionnaire ou opérateur de production."
    },
    {
        "name": "Morgan Services Toulouse Jean-Jaurès",
        "email": "toulouse-jeanjaures@morganservices.fr",
        "intro": "Votre agence Morgan Services Toulouse Jean-Jaurès, couvrant de nombreux secteurs dont la logistique, la manutention et l'aéronautique, correspond parfaitement à mon profil et à ma recherche de mission cet été."
    },
    {
        "name": "Morgan Services Toulouse L'Union",
        "email": "toulouse-lunion@morganservices.fr",
        "intro": "Votre agence Morgan Services Toulouse L'Union, implantée dans le bassin d'emploi toulousain et active dans les secteurs industriels et logistiques, me semble tout à fait adaptée à ma recherche de CDD ou mission d'intérim."
    },
]

# ============================================================
# ✉️ ШАБЛОН МЕЙЛУ
# ============================================================

SUBJECT = "Recherche de CDD / Mission d'intérim – Manutentionnaire / Magasinier – 29 juin au 31 juillet 2026"

def build_body(agency_intro):
    return f"""Madame, Monsieur,

{agency_intro}

Étudiant en première année à l'INSA Lyon (cycle ingénieur, filière FIMI), je suis actuellement à la recherche d'un CDD ou d'une mission d'intérim dans le secteur de la logistique ou de la production sur la région de Toulouse, pour la période du 29 juin au 31 juillet 2026.

Dans le cadre de ma formation, je dois effectuer un stage ouvrier d'au minimum quatre semaines, axé sur des travaux d'exécution en équipe. Je suis disponible pour les postes suivants :

- Manutentionnaire
- Préparateur de commandes
- Magasinier
- Opérateur de production
- Cariste (sans CACES pour l'instant)

Sportif de Haut Niveau en handball, je suis habitué aux environnements exigeants, au travail en équipe et aux cadences soutenues. Je suis rigoureux, ponctuel et pleinement disponible sur toute la période.

Je joins à ce message mon CV ainsi qu'une lettre de motivation. Je reste disponible pour tout entretien téléphonique ou physique à votre convenance.

Dans l'attente de votre retour, je vous adresse mes cordiales salutations.

{YOUR_NAME}
Étudiant à l'INSA Lyon & 42 Lyon
{YOUR_PHONE}
{YOUR_EMAIL}
"""

# ============================================================
# 📎 ФУНКЦІЯ ПРИКРІПЛЕННЯ PDF
# ============================================================

def attach_pdf(msg, filepath):
    if not os.path.exists(filepath):
        print(f"  ⚠️  Файл не знайдено: {filepath}")
        return
    with open(filepath, "rb") as f:
        part = MIMEApplication(f.read(), _subtype="pdf")
        part.add_header("Content-Disposition", "attachment", filename=os.path.basename(filepath))
        msg.attach(part)

# ============================================================
# 📝 ФУНКЦІЯ ЛОГУВАННЯ
# ============================================================

def log_result(agency_name, email, status, error=""):
    file_exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Heure", "Agence", "Email", "Statut", "Erreur"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            datetime.now().strftime("%H:%M:%S"),
            agency_name,
            email,
            status,
            error
        ])

# ============================================================
# 🚀 ГОЛОВНА ФУНКЦІЯ
# ============================================================

def send_all():
    print("=" * 55)
    print("  📬 Démarrage de l'envoi automatique des candidatures")
    print("=" * 55)

    # Перевірка PDF файлів
    for path in [CV_PATH, LM_PATH]:
        if not os.path.exists(path):
            print(f"\n❌ ERREUR : Fichier introuvable → {path}")
            print("   Place tes fichiers PDF dans le même dossier que ce script.")
            return

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            server.starttls(context=context)
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            print(f"\n✅ Connecté à {SMTP_SERVER}\n")

            for i, agency in enumerate(agencies):
                print(f"[{i+1}/{len(agencies)}] Envoi à : {agency['name']} ({agency['email']})")

                try:
                    msg = MIMEMultipart()
                    msg["From"] = f"{YOUR_NAME} <{YOUR_EMAIL}>"
                    msg["To"] = agency["email"]
                    msg["Subject"] = SUBJECT

                    body = build_body(agency["intro"])
                    msg.attach(MIMEText(body, "plain", "utf-8"))

                    attach_pdf(msg, CV_PATH)
                    attach_pdf(msg, LM_PATH)

                    server.sendmail(YOUR_EMAIL, agency["email"], msg.as_string())

                    print(f"  ✅ Envoyé avec succès !")
                    log_result(agency["name"], agency["email"], "✅ Envoyé")

                except Exception as e:
                    print(f"  ❌ Erreur : {e}")
                    log_result(agency["name"], agency["email"], "❌ Erreur", str(e))

                # Затримка між мейлами (крім останнього)
                if i < len(agencies) - 1:
                    delay = random.randint(DELAY_MIN, DELAY_MAX)
                    print(f"  ⏳ Pause de {delay} secondes...\n")
                    time.sleep(delay)

    except smtplib.SMTPAuthenticationError:
        print("\n❌ Erreur d'authentification — vérifie ton email et mot de passe INSA.")
    except Exception as e:
        print(f"\n❌ Erreur de connexion : {e}")

    print("\n" + "=" * 55)
    print(f"  📊 Résultats enregistrés dans : {LOG_FILE}")
    print("=" * 55)

# ============================================================
if __name__ == "__main__":
    send_all()