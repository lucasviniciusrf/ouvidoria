from operacoesbd import *

#listagem ok
def listagemManifestacoes(conn):
    print("=" * 15, "\033[34mLISTA\033[m", "=" * 15)
    consultaListagem = 'select * from tabelaOuvidoria'
    listaBanco = listarBancoDados(conn, consultaListagem)
    if len(listaBanco) == 0:
        print(f'\033[31mLista de manifestações vazia!\033[m')
    else:
        for item in range(len(listaBanco)):
            print(f'\033[34mManifestação {item + 1})\033[m {listaBanco[item][0]} - {listaBanco[item][1]} - {listaBanco[item][2]} - {listaBanco[item][3]}')
            print()

#listagemTipo ok
def listagemTipo(conn):
    print("=" * 15, "\033[34mPESQUISA POR TIPO\033[m", "=" * 15)
    try:
        print("[ 1 ] Reclamação [ 2 ] Sugestão [ 3 ] Elogio")
        tipo = input("Digite o codigo do tipo da manifestação: ")

        if not tipo:
            print('\033[31mErro: Este campo pode estar vazio. Por favor, preencha corretamente!\033[m')
            return
        
        elif tipo == '1':
            print("=" * 15, "\033[34mRECLAMAÇÃO\033[m", "=" * 15)

        elif tipo == '2':
            print("=" * 15, "\033[34mSUGESTÃO\033[m", "=" * 15)

        elif tipo == '3':
            print("=" * 15, "\033[34mELOGIO\033[m", "=" * 15)

        else:
            print('Opção inválida.')

    except Exception as e:
        print(f'Erro {e}. Tente novamente.')

    consultalistagem = "select * from tabelaOuvidoria where tipo = %s"
    opcao = [tipo]
    listaBanco = listarBancoDados(conn, consultalistagem, opcao)
    if len(listaBanco) == 0:
        print(f'\033[31mLista de manifestações vazia!\033[m')
    else:
        for item in range(len(listaBanco)):
            print(
                f'Manifestação - {item+1})\033[32m {listaBanco[item][0]} - {listaBanco[item][1]} - {listaBanco[item][2]} - {listaBanco[item][3]}\033[m')
            print()

# DESCRIÇÃO ok
def adicionarManifestacao(conn):
    try:
        print("=" * 15, "\033[34mADICIONAR\033[m", "=" * 15)
        cpf = input('Digite seu CPF: ').strip()
        nome = input('Digite seu nome: ').strip()
        print("[ 1 ] Reclamação [ 2 ] Sugestão [ 3 ] Elogio ")
        tipo = int(input("Qual é o tipo da manifestação: "))
        reclamacao = input('Digite sua reclamação: ').strip()


        # Verifica se algum campo está vazio antes de enviar ao banco
        if not cpf or not nome or not tipo or not reclamacao:
            print('\033[31mErro: Nenhum campo pode estar vazio. Por favor, preencha todos os campos corretamente!\033[m')
            return

        consultaReclamacao = 'INSERT INTO tabelaOuvidoria (cpf, nome, tipo, reclamacao) VALUES (%s, %s, %s, %s)'
        dados = [cpf, nome, tipo, reclamacao]
        inserirBanco = insertChaveUnica(conn, consultaReclamacao, dados)

        if inserirBanco:
            print(f'Perfeito, {nome.capitalize()}! Sua reclamação foi registrada com sucesso.')
        else:
            print('Verifique se seu CPF já está cadastrado ou inválido.')

    except Exception as e:
        print(f'\033[31mErro {e}: Ocorreu um problema ao registrar sua reclamação. Tente novamente!\033[m')

#Atualizar ok
def atualizarInformacoes(conn):
    try:
        print("=" * 15, "\033[34mATUALIZAR\033[m", "=" * 15)
        qualCpf = input('Digite o cpf que a manifestação está relacionada: (Se preferir, pode digitar APENAS os dois últimos dígitos do cpf) ')
        manifestacao = input('Digite a nova manifestação: ')
        if not qualCpf or not manifestacao:
            print('\033[31mVerifique se os espaços foram devidamente preenchidos ou o valor válido!\033[m')
            return

        consultaAtualizar = 'update tabelaOuvidoria set reclamacao = %s where cpf like %s'
        dados = [ manifestacao, '%' + qualCpf]
        atualizarBanco = atualizarBancoDados(conn, consultaAtualizar, dados)

        if atualizarBanco:
            print('Atualização feita com sucesso!')
        else:
            print('CPF inválido!')

    except Exception as e:
        print(f'\033[31mErro,{e}: Ocorreu um problema ao registrar sua reclamação. Tente novamente!\033[m')

# QUANTIDADE
def quantidadeManifestacoes(conn):
    print("=" * 15, "\033[34mQUANTIDADE\033[m", "=" * 15)
    consultaQuantidade = 'select reclamacao from tabelaOuvidoria'
    listarQuantidadeDeReclamacoes = listarBancoDados(conn, consultaQuantidade)

    if len(listarQuantidadeDeReclamacoes) == 0:
        print(f'\033[31mLista de manifestações vazia!\033[m')
    else:
        print(f'Total de \033[34m{len(listarQuantidadeDeReclamacoes)}\033[m manifestações.')
        print()

# PESQUISAR
def pesquisarManifestacoes(conn):
    try:
        print("=" * 15, "\033[34mPESQUISA\033[m", "=" * 15)
        qualCpf = input('Digite o CPF para exibir a reclamação realizada: (Se preferir, pode digitar APENAS os dois últimos dígitos do cpf) ').strip()

        # Verifica se o CPF foi preenchido antes de buscar no banco
        if not qualCpf:
            print('\033[31mErro: O CPF não pode estar vazio. Por favor, insira um CPF válido!\033[m')
            return

        consultaPesquisar = 'SELECT reclamacao FROM tabelaOuvidoria WHERE cpf like %s'
        dados = ['%' + qualCpf]

        reclamacaoDesejada = listarBancoDados(conn, consultaPesquisar, dados)

        # Verifica se o CPF existe no banco antes de exibir a reclamação
        if not reclamacaoDesejada:
            print(f'\033[31mErro: Nenhuma manifestação encontrada para o CPF informado.\033[m')
        else:
            print(f'A reclamação referente a esse CPF é: "{reclamacaoDesejada[0][0]}"')

    except ValueError:
        print(f'\033[31mErro: O CPF informado é inválido.\033[m')

#Excluir
def excluirManifestacoes(conn):
    try:
        print("=" * 15, "\033[34mEXCLUIR\033[m", "=" * 15)
        cpf = input('Digite o cpf para remover a manifestação: (Se preferir, pode digitar APENAS os dois últimos dígitos do cpf) ')
        consultaExcluir = 'delete from tabelaOuvidoria where cpf like %s'
        dados = ['%' + cpf]
        if not cpf:
            print('\033[31mErro: Nenhum campo pode estar vazio. Por favor, preencha todos os campos corretamente!\033[m')
            return

        excluindoManifestacoes = excluirBancoDados(conn, consultaExcluir, dados)


        if excluindoManifestacoes == 0:
            print('Nenhuma manifestação removida.')

        else:
                print(f'Manifestação do cpf "\033[31m{cpf}\033[m" excluída com sucesso')
                print()
    except Exception as e:
        print(f'\033[31mErro {e}: Ocorreu um problema ao registrar sua reclamação. Tente novamente!\033[m')

def encerrar(conn):
    encerrarConexao(conn)
    print('Até mais!')