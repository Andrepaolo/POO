def calculardescuentosegunprecio():
    n1=float(input("Ingrese el precio del articulo: ")) 
    if n1<100.00:
        print(("usted tiene un descuento de 10% y debe pagar: "), n1-(n1)*10/100)
    if 99.99<n1<200.00:
        print(("usted tiene un descuento de 12% y debe pagar: "), n1-(n1)*12/100)
    if n1>=200:
        print(("usted tiene un descuento de 15% y debe pagar: "), n1-(n1)*15/100)
calculardescuentosegunprecio()