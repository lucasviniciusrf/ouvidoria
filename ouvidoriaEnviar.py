from ouvidoriaFinal import *

conn = criarConexao('localhost', 'root', '1234', 'ouvidoria')

print()
print("="*15,"\033[34mProjeto Ouvidoria\033[m","="*15)
print()
while True:
    print('=' * 50)
    print('''
        1) Listagem das Manifestações 
        2) Lista por Tipo 
        3) Criar Nova Manifestação 
        4) Exibir Quantidade de Manifestações 
        5) Pesquisar Manifestação por Código 
        6) Atualizar Manifestação
        7) Excluir Manifestação 
        8) Sair do Sistema''')
    print()
    print('=' * 50)
    opcao = input('Selecione a opção: ')
    print()

    if not opcao:
        print('\033[31mErro: Este campo pode estar vazio. Por favor, preencha corretamente!\033[m')
        continue
    
    elif opcao == '1':
        listagemManifestacoes(conn)

    elif opcao == '2':
        listagemTipo(conn)

    elif opcao == '3':
        adicionarManifestacao(conn)

    elif opcao == '4':
        quantidadeManifestacoes(conn)

    elif opcao == '5':
        pesquisarManifestacoes(conn)

    elif opcao == '6':
        atualizarInformacoes(conn)

    elif opcao == '7':
        excluirManifestacoes(conn)

    elif opcao == '8':
        encerrar(conn)
        break

    else:
            print('Opção inválida!')