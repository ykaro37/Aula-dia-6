# QUESTÃO 1 

notas = []
print("--- Cadastro de Notas (6 Alunos) ---")

for i in range(6):
    while True:
        try:
            nota = float(input(f"Digite a nota do aluno {i+1} (entre 0.0 e 10.0): "))
            if 0.0 <= nota <= 10.0:
                notas.append(nota)
                break
            else:
                print("Valor inválido! A nota deve estar entre 0.0 e 10.0.")
        except ValueError:
            print("Entrada inválida. Digite um número real.")

print("\n[Q1] Notas armazenadas com sucesso:", notas)


# QUESTÃO 2 

media_geral = sum(notas) / len(notas)
acima_ou_igual = 0
abaixo_media = []

for nota in notas:
    if nota >= media_geral:
        acima_ou_igual += 1
    else:
        abaixo_media.append(nota)

print("\n--- Relatório de Desempenho ---")
print(f"1. Média geral da turma: {media_geral:.2f}")
print(f"2. Quantidade de alunos acima ou igual à média: {acima_ou_igual}")
print(f"3. Notas específicas abaixo da média: {abaixo_media}")


# QUESTÃO 3 

print("\n--- Sistema de Recuperação ---")
notas_atualizadas = notas.copy()

for i in range(len(notas_atualizadas)):
    if notas_atualizadas[i] < media_geral:
        print(
            f"\nO aluno {i+1} obteve nota {notas_atualizadas[i]} (abaixo da média)."
        )

        while True:
            try:
                nota_rec = float(
                    input(
                        f"Digite a nota de recuperação para o aluno {i+1} (0.0 a 10.0): "
                    )
                )

                if 0.0 <= nota_rec <= 10.0:
                    if nota_rec > notas_atualizadas[i]:
                        print(
                            f"-> Nota melhorada! Substituindo {notas_atualizadas[i]} por {nota_rec}."
                        )
                        notas_atualizadas[i] = nota_rec
                    else:
                        print(
                            "-> A nota de recuperação não supera a original. Mantendo a original."
                        )
                    break
                else:
                    print("Valor inválido! Digite entre 0.0 e 10.0.")

            except ValueError:
                print("Entrada inválida. Digite um número.")

nova_media_geral = sum(notas_atualizadas) / len(notas_atualizadas)

print("\n--- Resultado Final ---")