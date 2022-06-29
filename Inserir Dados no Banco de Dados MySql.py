import mysql.connector
import PySimpleGUI as sg

while True:
    layout_1 = [
        [sg.Text('Digite o host:', size=(20, 1)),
         sg.InputText(key='host', size=(25, 1))],
        [sg.Text('Digite seu usuário:', size=(20, 1)),
         sg.InputText(key='user', size=(25, 1))],
        [sg.Text('Digite sua senha:', size=(20, 1)),
         sg.InputText(key='pass', size=(25, 1))],
        [sg.Text('Digite o nome do banco:', size=(20, 1)),
         sg.InputText(key='banco', size=(25, 1))],
        [sg.Button('Conectar')]
    ]

    window = sg.Window('Editor MySql', layout_1)
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        window.close()
        break

    if event == 'Conectar':
        host = values['host']
        user = values['user']
        password = values['pass']
        batabase = values['banco']
        window.hide()

        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=batabase
        )
         
        mycursor = mydb.cursor()
         
        if mydb.is_connected():
             informacao_banco = mydb.get_server_info()
             query = mydb.cursor()
             sg.Popup('Conectado ao servidor MySQL versão: ', informacao_banco, keep_on_top=True)
             window.hide()
             mycursor.execute("show tables") 
             myresult = mycursor.fetchall() 
             for tabelas in myresult: 
               sg.Popup('Lista de tabelas presentes nesse banco de dados:',tabelas, keep_on_top=True)
             
    layout_2 = [
        [sg.Text('Insira o nome: ', size=(20, 1)),
         sg.InputText(key = 'nome', size=(25, 1))],
        [sg.Text('Insira o email: ', size = (20 ,1)),
         sg.InputText(key = 'email', size=(25, 1))],
        [sg.Text('Insira o usuário: ', size= (20, 1)),
         sg.InputText(key = 'usuario', size = (25 ,1))],
        [sg.Text('Insira a senha: ', size = (20, 1)),
         sg.InputText(key = 'senha', size = (25, 1))],
        [sg.Text('Insira o nome da tabela: ', size = (20, 1)),
         sg.InputText(key = 'tabela', size = (25, 1))],
        [sg.Button('Inserir dados no banco')]
    ]
    
    window_2 = sg.Window('Inserir Dados no Banco de Dados', layout_2)
    event_1, values_1 = window_2.read()
    
    if event_1 == sg.WINDOW_CLOSED:
        window_2.close()
        break
    
    if event_1 == 'Inserir dados no banco':
        window_2.hide()
        nome = values_1['nome']
        email = values_1['email']
        usuario = values_1['usuario']
        senha = values_1['senha']
        table = values_1['tabela']
        
        sql = "insert into {} (nome, email, usuario, senha) values ('{}', '{}', '{}', '{}');".format(table, nome, email, usuario, senha) 
        mycursor.execute(sql)
        mydb.commit()  
        sg.Popup("Dados inseridos!", keep_on_top=True)
        break


        
        