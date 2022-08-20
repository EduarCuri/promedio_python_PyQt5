def calcularpromedio(vn1, vn2, vn3):
    import statistics as operacion
    vpromedio = operacion.mean([vn1, vn2, vn3])
    return vpromedio

def calcularobservacion(vpromedio):
    observacion = ""
    if vpromedio >= 12:
        observacion = "APROBADO"
    else:
        observacion = "DESAPROBADO"
    return observacion