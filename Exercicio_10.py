while True:

    nome_usuario = input ("\nDigite seu nome de usuário: ")
    senha_usuario = input ("Digite sua senha: ")

    if len (nome_usuario) < 5:

        print ("Atenção. O nome de usuário deve ter pelo menos 5 caracteres.")
        continue
            
        
    if len (senha_usuario) < 8:

        print ("A senha deve ter pelo menos 8 caracteres.")
        continue

    print ("Cadastro realizado com sucesso!!")
    break