"""
    Ceci est un fichier représentant les mails que nous envoyons.
"""


def msg_inscription(username, password):

    message_welcome = f"""
    <body style="width:100%; height:100%; color:black;">
        <div class="page" style="position: relative; box-sizing: border-box; max-width:500px; font-family: cursive; font-size: 20px; border-radius: 10px; background: #fff; background-image: linear-gradient(#f5f5f0 1.1rem, #ccc 1.2rem); background-size: 100% 1.2rem; line-height: 1.2rem; padding: 1.4rem 1.5rem 0.2rem 1.5rem;">
            <div style="display: flex; width: 100%; justify-content: center">
                <img src="https://raw.githubusercontent.com/RolandRKT/SAE-3.05/develop/flask/tuto-flask/tuto/static/images/wade-title.png" alt="Image" style="max-width: auto; height: 70px; display: block; margin-left:auto; margin-right:auto;">
            </div>
            <div class="margin"></div>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                Bienvenue {username} chez Wade !
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                Nous sommes ravis de vous accueillir parmi nous.
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                Votre compte a été créé avec succès.
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700" style="background-color:white; text-align:center; font-weight:bold; height:25px; font-size:20px;">
                Votre mot de passe : {password}
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                Connectez-vous à votre compte en utilisant votre pseudo et votre mot de passe.
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                Merci de faire partie de notre communauté.
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                Cordialement,
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                L'équipe de Wade
            </p>
            <div style="display: flex; width: 100%; justify-content: center">
                <img src="https://raw.githubusercontent.com/RolandRKT/SAE-3.05/develop/flask/tuto-flask/tuto/static/images/logo.png" alt="Image" style="max-width: 70px; height: auto; display: block; margin-left:auto; margin-right:auto;">
            </div>
        </div>
    </body>
    """

    return message_welcome


def msg_forget_password(password):
    message_reset_password = """
    <body style="width:100%; height:100%; color:black;">
        <div class="page" style="position: relative; box-sizing: border-box; max-width:500px; font-family: cursive; font-size: 20px; border-radius: 10px; background: #fff; background-image: linear-gradient(#f5f5f0 1.1rem, #ccc 1.2rem); background-size: 100% 1.2rem; line-height: 1.2rem; padding: 1.4rem 1.5rem 0.2rem 1.5rem;">
            <div style="display: flex; width: 100%; justify-content: center">
                <img src="https://raw.githubusercontent.com/RolandRKT/SAE-3.05/develop/flask/tuto-flask/tuto/static/images/wade-title.png" alt="Image" style="max-width: auto; height: 70px; display: block; margin-left:auto; margin-right:auto;">
            </div>
            <div class="margin"></div>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                Cher utilisateur,
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                Nous avons reçu une demande de réinitialisation du mot de passe associé à cette adresse e-mail. Si vous n'avez pas fait cette demande, veuillez ignorer cet e-mail.
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                Pour rappel, votre mot de passe est :
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700" style="background-color:white; text-align:center; font-weight:bold; height:25px; font-size:20px;">
                {}
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                Veuillez vous connecter à votre compte avec ce mot de passe.
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                Merci de faire partie de notre communauté.
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                Cordialement,
            </p>
            <p class="px-10 text-[10px] sm:text-[12px] text-gray-700">
                L'équipe de Wade
            </p>
            <div style="display: flex; width: 100%; justify-content: center">
                <img src="https://raw.githubusercontent.com/RolandRKT/SAE-3.05/develop/flask/tuto-flask/tuto/static/images/logo.png" alt="Image" style="max-width: 70px; height: auto; display: block; margin-left:auto; margin-right:auto;">
            </div>
        </div>
    </body>
    """.format(password)
    return message_reset_password
