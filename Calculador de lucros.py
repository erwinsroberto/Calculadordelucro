vr_compra=float(input("Digite o valor da compra:"))
if vr_compra <20:
  lucro_45=vr_compra*0.45
  venda=vr_compra+lucro_45
  print("O lucro é de:", lucro_45)
  print("E o valor da venda é de:", venda)
else:
  lucro_30=vr_compra*0.30
  venda=vr_compra+lucro_30
  print("O lucro é de:", lucro_30)
  print("E o valor da venda é de:", venda)