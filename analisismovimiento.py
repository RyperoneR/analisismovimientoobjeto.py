parametros_iniciales = {
    "x0": float(input("Posicion inicial (m): ")),
    "v0": float(input("Velocidad inicial (m/s): ")),
    "a": float(input("Aceleracion (m/s^2): ")),
    "t": float(input("Tiempo (s): "))
}

posicion_final = (parametros_iniciales["x0"]+(parametros_iniciales["v0"]*parametros_iniciales["t"])+(0.5*parametros_iniciales["a"]*(parametros_iniciales["t"]*parametros_iniciales["t"])))
velocidad_final = (parametros_iniciales["v0"]+parametros_iniciales["a"]*parametros_iniciales["t"])

print("Posicion final: ", posicion_final, "m")
print("Velocidad final: ", velocidad_final, "m/s")
print("Aceleracion: ", parametros_iniciales["a"], "m/s^2")