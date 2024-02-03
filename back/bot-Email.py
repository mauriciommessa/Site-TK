import win32com.client as win32

# Criar a integração com o outlook
outlook = win32.Dispatch('Outlook.Application')

# Criar um email
email = outlook.CreateItem(0)

# Configurar as informações do seu E-mail
email.To = "stottim.steam@gmail.com"
email.Subject = "TK2"
email.HTMLBody = """
<h1> A sua conta do TikTok chegou!!!</h1>
"""

email.Send()
print("Email enviado")
