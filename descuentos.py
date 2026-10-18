importe= float(input("Introduce el importe de la compra en euros: "))
descuento=float(0)
descuento_aplicado=float(0)
if importe <0:
    print("El importe no puede ser negativo.")
else:
    if importe < 100:
        descuento = 0
        descuento_aplicado = importe * descuento
        total_a_pagar = importe - descuento_aplicado
        print(f"Descuento aplicado: {descuento * 100:.0f}%")
        print(f"Importe del descuento: {descuento_aplicado:.2f} €")
        print(f"Total a pagar: {total_a_pagar:.2f} €")
    if importe >= 100 and importe < 300:
        descuento = 0.10
        descuento_aplicado = importe * descuento
        total_a_pagar = importe - descuento_aplicado
        print(f"Descuento aplicado: {descuento * 100:.0f}%")
        print(f"Importe del descuento: {descuento_aplicado:.2f} €")
        print(f"Total a pagar: {total_a_pagar:.2f} €")
    if importe >= 300:
        descuento = 0.15
        descuento_aplicado = importe * descuento
        total_a_pagar = importe - descuento_aplicado
        print(f"Descuento aplicado: {descuento * 100:.0f}%")
        print(f"Importe del descuento: {descuento_aplicado:.2f} €")
        print(f"Total a pagar: {total_a_pagar:.2f} €")