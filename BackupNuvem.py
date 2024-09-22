# Importação das bibliotecas necessárias para o funcionamento do projeto
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

def enviar_email(destinatario, assunto, mensagem, caminho_arquivo):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    remetente = "Aqui deve ser inserido o e-mail do remetente. Geralmente, utiliza-se um e-mail pessoal para enviar os arquivos ao destinatário (e-mail empresarial)."
    senha = "A senha deve ser configurada na aba de gestão de senhas da sua conta Google. Recomenda-se utilizar uma senha de aplicativo para garantir que sua senha principal não fique exposta."

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    msg.attach(MIMEText(mensagem, 'plain'))

# Anexando os arquivos ao e-mail
    try:
        with open(caminho_arquivo, "rb") as arquivo:
            parte = MIMEBase('application', 'octet-stream')
            parte.set_payload(arquivo.read())
            encoders.encode_base64(parte)
            parte.add_header('Content-Disposition', f'attachment; filename={caminho_arquivo.split("/")[-1]}')
            msg.attach(parte)

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(remetente, senha)

        server.sendmail(remetente, destinatario, msg.as_string())
# Mensagem de confirmação após o envio do e-mail
        print("Email enviado com sucesso")

    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

    finally:
        server.quit()
# Formatação da data e hora atuais
data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Formatação da mensagem a ser enviada
assunto = f"BACKUP do dia {datetime.now().strftime('%d/%m/%Y')} às {datetime.now().strftime('%H:%M:%S')}"
mensagem = f"Backup efetuado com sucesso em {data_hora_atual}!"
enviar_email("aqui deve conter o email de quem deve receber a mensagem exemplo: fulano@gmail.com", assunto, mensagem, "nome do arquivo ou caminho a ser enviado")
