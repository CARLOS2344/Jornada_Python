def mensagem_com_linhas(msg):
    mais_quatro = len(msg) + 4
    print("=" * mais_quatro)
    print(f"  {msg.title()}")
    print("=" * mais_quatro)