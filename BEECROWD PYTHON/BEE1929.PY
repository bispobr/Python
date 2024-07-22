vetor = [int (x) for x in input().strip().split(" ")]

if (abs(vetor[0] - vetor[1])  <  vetor[2] and vetor[2] < vetor[0] + vetor[1]) or (abs(vetor[0] - vetor[1]) < vetor[3] and vetor[3] < vetor[0] + vetor[1]) or (abs(vetor[0] - vetor[2]) < vetor[3] and vetor[3] < vetor[0] + vetor[2]) or (abs(vetor[1] - vetor[2]) < vetor[3] and vetor[3] < vetor[1] + vetor[2]):
    print("S")
else:
    print("N")