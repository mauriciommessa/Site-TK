import win32com.client as win32

# Criar a integração com o outlook
outlook = win32.Dispatch('Outlook.Application')

# Criar um email
email = outlook.CreateItem(0)

# Configurar as informações do seu E-mail
email.To = "messammauricio@gmail.com"; "stottim.steam@gmail.com"
email.Subject = "TK2"
email.HTMLBody = """
<style>

        * {
            margin: 0px;
            padding: 0px;
            font-family: Arial, Helvetica, sans-serif;
        }
        
        body {

        }

        h1 {
            padding-top: 10px;
        }

        header {
            background-color: #2f2f2f;
            color: white;
            text-align: center;
            width: 50vw;
            margin: auto;
        }

        main {
            background-color: lightgray;
            width: 50vw;
            margin: auto;
            display: block;
            height: 60vh;
        }

        p {
            padding: 2px;
            text-align: center;
            font-size: 1.1em;
        }

        p#usu {
            display: block;
            text-align: center;
            border: 2px solid black;
            padding: 10px;
            margin: 0px;
            width: 250px;
            height: auto;
            margin: auto;
            font-size: 1.1em;
            background-color: white;
        }

        p#atenciosamente {
            text-decoration: underline;
            font-size: 1.3em;
        }
    </style>
    <header>
        <h1> A sua conta do TikTok chegou!!!</h1><br>
    </header>
    <main>  
        <p>Obrigado por comprar em nosso site! <br>Aqui estão seus dados: </p>
        <p id="usu">Usúario: usuario321 <br><br> Senha:chineleiroana123</p>
        <p><br>Fique a vontade para responder em caso de dúvidas</p>
        <p id="atenciosamente"><br><br>Atenciosamente: <a href="#">TK2-store</a></p>
    </main>
"""

email.Send()
print("Email enviado")
