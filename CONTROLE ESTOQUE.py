from PyQt5 import uic,QtWidgets
import mysql.connector
from mysql.connector import cursor
from mysql.connector.errors import custom_error_exception
from reportlab.pdfgen import canvas


banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "cadastro_produto"
)

def relatorio_nome():

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos ORDER BY descricao"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("relatorio_nome.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(150,800, "PRODUTOS CADASTRADOS:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110,750, "CODIGO")
    pdf.drawString(210,750, "PRODUTO")
    pdf.drawString(310,750, "PREÇO")
    pdf.drawString(410,750, "CATEGORIA")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

    pdf.save()
    print("RELATORIO FOI GERADO COM SUCESSO!")

def relatorio_preco():

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos ORDER BY preco"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("relatorio_preco.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(150,800, "PRODUTOS CADASTRADOS:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110,750, "CODIGO")
    pdf.drawString(210,750, "PRODUTO")
    pdf.drawString(310,750, "PREÇO")
    pdf.drawString(410,750, "CATEGORIA")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

    pdf.save()
    print("RELATORIO FOI GERADO COM SUCESSO!")

def relatorio_categoria():
    
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos ORDER BY categoria"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("relatorio_categoria.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(150,800, "PRODUTOS CADASTRADOS:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110,750, "CODIGO")
    pdf.drawString(210,750, "PRODUTO")
    pdf.drawString(310,750, "PREÇO")
    pdf.drawString(410,750, "CATEGORIA")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

    pdf.save()
    print("RELATORIO FOI GERADO COM SUCESSO!")

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ""

    if formulario.radioButton.isChecked():
        print ("CATEGORIA INFORMÁTICA FOI SELECIONADO!")
        categoria = "informatica"
    if formulario.radioButton_2.isChecked():
        print ("CATEGORIA ALIMENTOS FOI SELECIONADO!")
        categoria = "alimentos"
    if formulario.radioButton_3.isChecked():
        print ("CATEGORIA ELETRÔNICOS FOI SELECIONADO!")
        categoria = "eletronicos"

    print("CÓDIGO: ", linha1)
    print("DESCRIÇÃO: ", linha2)
    print("PREÇO: ", linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    #Limpando os componentes
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")

def fechar_primeira_tela():
    formulario.close()

def gerar_pdf():
    
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(150,800, "PRODUTOS CADASTRADOS:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110,750, "CODIGO")
    pdf.drawString(210,750, "PRODUTO")
    pdf.drawString(310,750, "PREÇO")
    pdf.drawString(410,750, "CATEGORIA")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

    pdf.save()
    print("RELATORIO FOI GERADO CO SUCESSO!")


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ""

    if formulario.radioButton.isChecked():
        print ("CATEGORIA INFORMÁTICA FOI SELECIONADO!")
        categoria = "informatica"
    if formulario.radioButton_2.isChecked():
        print ("CATEGORIA ALIMENTOS FOI SELECIONADO!")
        categoria = "alimentos"
    if formulario.radioButton_3.isChecked():
        print ("CATEGORIA ELETRÔNICOS FOI SELECIONADO!")
        categoria = "eletronicos"

    print("CÓDIGO: ", linha1)
    print("DESCRIÇÃO: ", linha2)
    print("PREÇO: ", linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    #Limpando os componentes
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")


def chama_segunda_tela():

    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)
    
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id=" + str(valor_id))
    banco.commit()

def editar_dados() :
    #Pega o número do ID
    global numero_id
    #Armazena a linha selecionada do objeto
    linha = segunda_tela.tableWidget.currentRow()
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    #Conecta no BD

    #Navega no BD
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE id="+ str(valor_id))
    produto = cursor.fetchall()
    tela_editar.show()

    tela_editar.lineEdit.setText(str(produto[0][0]))
    tela_editar.lineEdit_2.setText(str(produto[0][1]))
    tela_editar.lineEdit_3.setText(str(produto[0][2]))
    tela_editar.lineEdit_4.setText(str(produto[0][3]))
    tela_editar.lineEdit_5.setText(str(produto[0][4]))
    numero_id = valor_id





def salvar_valor_editado() :
    global numero_id
    #Ler dados do lineEdit
    codigo = tela_editar.lineEdit_2.text()
    descricao = tela_editar.lineEdit_3.text()
    preco = tela_editar.lineEdit_4.text()
    categoria = tela_editar.lineEdit_5.text()
    #Atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE produtos SET codigo = '{}', descricao = '{}', preco = '{}', categoria = '{}'  WHERE id = {}".format(codigo,descricao,preco,categoria,numero_id))
    banco.commit()
    #Atualizar as janelas
    tela_editar.close()
    segunda_tela.close()
    chama_segunda_tela()


def filtrar_nome():

    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos ORDER BY descricao"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def filtrar_preco():
    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos ORDER BY preco"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def filtrar_categoria():
    segunda_tela.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos ORDER BY categoria"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
def ordem_categoria():
    segunda_tela.show()
    cursor = banco.cursor()

    if segunda_tela.radioButton.isChecked():
        comando_SQL = "SELECT * FROM produtos WHERE categoria = 'alimentos'"
    if segunda_tela.radioButton_2.isChecked():
        comando_SQL = "SELECT * FROM produtos WHERE categoria = 'informatica'"
    if segunda_tela.radioButton_3.isChecked():
        comando_SQL = "SELECT * FROM produtos WHERE categoria = 'eletronicos'"

    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def filtro_pdf():
    
    cursor = banco.cursor()
    if segunda_tela.radioButton.isChecked():
        comando_SQL = "SELECT * FROM produtos WHERE categoria = 'alimentos'"
    if segunda_tela.radioButton_2.isChecked():
        comando_SQL = "SELECT * FROM produtos WHERE categoria = 'informatica'"
    if segunda_tela.radioButton_3.isChecked():
        comando_SQL = "SELECT * FROM produtos WHERE categoria = 'eletronicos'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastro_produtos_Filtro.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(150,800, "PRODUTOS CADASTRADOS:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110,750, "CODIGO")
    pdf.drawString(210,750, "PRODUTO")
    pdf.drawString(310,750, "PREÇO")
    pdf.drawString(410,750, "CATEGORIA")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

    pdf.save()
    print("RELATORIO FOI GERADO CO SUCESSO!")

def relatorio_combo():
    cursor = banco.cursor()
    categoria = segunda_tela.comboBox.currentText()
    segunda_tela.label_7.setText("categoria: "+categoria)

    segunda_tela.comboBox.currentIndex() == 0
    comando_SQL = ("SELECT * FROM produtos ORDER BY descricao")
    cursor.execute(comando_SQL) 
    dados_lidos = cursor.fetchall()
        
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumCounts(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    y = 0
    pdf = canvas.Canvas("Relatorio_Ordenado.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(150,800, "PRODUTOS CADASTRADOS:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110,750, "CODIGO")
    pdf.drawString(210,750, "PRODUTO")
    pdf.drawString(310,750, "PREÇO")
    pdf.drawString(410,750, "CATEGORIA")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

        pdf.save()
        print("RELATORIO FOI GERADO COM SUCESSO!")

def fechar_segunda_tela():
    segunda_tela.close()

def chama_tela_principal():
    primeira_tela.label_4.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    if nome_usuario == "123" and senha == "123":
        primeira_tela.close()
        segunda_tela2.show()
    else:
        primeira_tela.label_4.setText("Dados de Login Incorretos")

def logout():
    segunda_tela2.close()
    primeira_tela.show()

#CADASTRO DE PESSOAS

numero_id = 0
banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "cadastro_pessoas"
)

def funcao_sair():
    cadastro.close()

def lista_pessoas():
    lista_de_pessoas.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM tbpessoas"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    lista_de_pessoas.tableWidget.setRowCount(len(dados_lidos))
    lista_de_pessoas.tableWidget.setColumnCount(10)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 10):
            lista_de_pessoas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def excluir_dados():
    linha=lista_de_pessoas.tableWidget.currentRow()
    lista_de_pessoas.tableWidget.removeRow(linha)
    cursor = banco.cursor()
    cursor.execute("SELECT codigo FROM tbpessoas")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    print(valor_id)
    cursor.execute("DELETE FROM tbpessoas WHERE codigo ="+str(valor_id))
    banco.commit()

def gerar_relatorio():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM tbpessoas"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0 
    pdf = canvas.Canvas("cadastro_pessoas.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Pessoas Cadastradas:")
    pdf.setFont("Times-Bold", 18)
    pdf.drawString(10,750, "CODIGO")
    pdf.drawString(10,750, "CPF / CNPJ")
    pdf.drawString(110,750, "TIPO")
    pdf.drawString(210,750, "NOME")
    pdf.drawString(310,750, "ENDEREÇO")
    pdf.drawString(520,750, "BAIRRO")
    pdf.drawString(520,750, "CIDADE")
    pdf.drawString(520,750, "ESTADO")
    pdf.drawString(520,750, "TELEFONE")
    pdf.drawString(520,750, "EMAIL")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y,str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y,str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y,str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y,str(dados_lidos[i][3]))
        pdf.drawString(510,750 - y,str(dados_lidos[i][4]))
        pdf.drawString(510,750 - y,str(dados_lidos[i][5]))
        pdf.drawString(510,750 - y,str(dados_lidos[i][6]))
        pdf.drawString(510,750 - y,str(dados_lidos[i][7]))
        pdf.drawString(510,750 - y,str(dados_lidos[i][8]))
        pdf.drawString(510,750 - y,str(dados_lidos[i][9]))

    pdf.save()
    print ("RELATÓRIO FOI GERADO COM SUCESSO")

def editar_dados():
    global numero_id
    linha = lista_de_pessoas.tableWidget.currentRow()
    cursor = banco.cursor()
    cursor.execute("SELECT codigo FROM tbpessoas")
    dados_lidos = cursor.fetchall() 
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM tbpessoas WHERE codigo="+ str(valor_id))
    produto = cursor.fetchall()
    tela_editar_dados.show()
    tela_editar_dados.lineEdit.setText(str(produto[0][0]))
    tela_editar_dados.lineEdit_2.setText(str(produto[0][1]))
    tela_editar_dados.lineEdit_3.setText(str(produto[0][2]))
    tela_editar_dados.lineEdit_4.setText(str(produto[0][3]))
    tela_editar_dados.lineEdit_5.setText(str(produto[0][4]))
    tela_editar_dados.lineEdit_6.setText(str(produto[0][5]))
    tela_editar_dados.lineEdit_7.setText(str(produto[0][6]))
    tela_editar_dados.lineEdit_8.setText(str(produto[0][7]))
    tela_editar_dados.lineEdit_9.setText(str(produto[0][8]))
    tela_editar_dados.lineEdit_10.setText(str(produto[0][9]))
    numero_id = valor_id

def funcao_principal():
    cpf_cnpj = cadastro.le_cpf_cnpj.text()
    nome_pessoa = cadastro.le_nome.text()
    endereco_pessoa = cadastro.le_endereco.text()
    telefone_pessoa = cadastro.le_telefone.text()
    email_pessoa = cadastro.le_email.text()
    bairro_pessoa = cadastro.le_bairro.text()
    cidade_pessoa = cadastro.le_cidade.text()
    tipo_pessoa = cadastro.combo_tipo.currentText()
    estado_pessoa = cadastro.combo_estado.currentText()

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO tbpessoas (cpf_cnpj,tipo,nome,endereco,bairro,cidade,estado,telefone,email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(cpf_cnpj), str(tipo_pessoa), str(nome_pessoa), str(endereco_pessoa), str(bairro_pessoa), str(cidade_pessoa), str(estado_pessoa), str(telefone_pessoa), str(email_pessoa))
    cursor.execute(comando_SQL, dados)
    banco.commit()

    cadastro.le_cpf_cnpj.setText("")
    cadastro.le_nome.setText("")
    cadastro.le_endereco.setText("")
    cadastro.le_telefone.setText("")
    cadastro.le_email.setText("")
    cadastro.le_bairro.setText("")
    cadastro.le_cidade.setText("")
    
def salvar_valor_editado():
    global numero_id
    cpf_cnpj = tela_editar_dados.lineEdit_2.text()
    tipo = tela_editar_dados.lineEdit_3.text()
    nome = tela_editar_dados.lineEdit_4.text()
    endereco = tela_editar_dados.lineEdit_5.text()
    bairro = tela_editar_dados.lineEdit_6.text()
    cidade = tela_editar_dados.lineEdit_7.text()
    estado = tela_editar_dados.lineEdit_8.text()
    telefone = tela_editar_dados.lineEdit_9.text()
    email = tela_editar_dados.lineEdit_10.text()
    cursor = banco.cursor()
    cursor.execute("UPDATE tbpessoas SET cpf_cnpj = '{}' ,tipo = '{}' ,nome = '{}' ,endereco = '{}' ,bairro = '{}',cidade = '{}',estado = '{}',telefone = '{}',email = '{}'WHERE codigo = {}".format(cpf_cnpj,tipo,nome,endereco,bairro,cidade,estado,telefone,email,numero_id))
    banco.commit()
    tela_editar_dados.close()
    lista_de_pessoas.close()
    
app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar_dados.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton_4.clicked.connect(excluir_dados)
formulario.pushButton_3.clicked.connect(fechar_primeira_tela)
segunda_tela.pushButton.clicked.connect(fechar_segunda_tela)
segunda_tela.pushButton_5.clicked.connect(editar_dados)
segunda_tela.pushButton_6.clicked.connect(filtrar_nome)
segunda_tela.pushButton_7.clicked.connect(filtrar_preco)
segunda_tela.pushButton_8.clicked.connect(filtrar_categoria)
segunda_tela.pushButton_9.clicked.connect(filtro_pdf)
segunda_tela.pushButton_10.clicked.connect(relatorio_nome)
segunda_tela.pushButton_11.clicked.connect(relatorio_preco)
segunda_tela.pushButton_12.clicked.connect(relatorio_categoria)
tela_editar=uic.loadUi("menu_editar_produto.ui")
tela_editar.btn_salvar.clicked.connect(salvar_valor_editado)
segunda_tela.radioButton.clicked.connect(ordem_categoria)
segunda_tela.radioButton_2.clicked.connect(ordem_categoria)
segunda_tela.radioButton_3.clicked.connect(ordem_categoria)
segunda_tela.pushButton_13.clicked.connect(relatorio_combo)
segunda_tela.comboBox.addItems(["Descricao", "Preco", "Alimentos", "Eletronicos", "Informatica"])

cadastro=uic.loadUi("formulario_pessoas.ui")
lista_de_pessoas=uic.loadUi("lista_pessoas.ui")
tela_editar_dados=uic.loadUi("menu_editar_cliente.ui")
lista_de_pessoas.btn_excluir.clicked.connect(excluir_dados)
cadastro.btn_sair.clicked.connect(funcao_sair)
cadastro.combo_estado.addItems(["Selecione", "MG", "SP", "RJ", "ES", "BA", "AC", "DF"])
cadastro.combo_tipo.addItems(["Selecione", "Cliente", "Funcionario", "Fornecedor"])
cadastro.btn_lista.clicked.connect(lista_pessoas)
lista_de_pessoas.btn_editar.clicked.connect(editar_dados)
cadastro.btn_enviar.clicked.connect(funcao_principal)
lista_de_pessoas.btn_relatorio.clicked.connect(gerar_relatorio)
tela_editar_dados.btn_salvar.clicked.connect(salvar_valor_editado)  

#TELA LOGIN
primeira_tela=uic.loadUi("primeira_tela.ui")
primeira_tela.pushButton.clicked.connect(chama_tela_principal)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
primeira_tela.pushButton_21.clicked.connect(cadastro.show)

#TELA PRINCIPAL
segunda_tela2=uic.loadUi("segunda_tela2.ui")
segunda_tela2.pushButton.clicked.connect(logout)
segunda_tela2.pushButton_20.clicked.connect(formulario.show)
segunda_tela2.pushButton_21.clicked.connect(cadastro.show)


primeira_tela.show()

app.exec()