# --- Proyecto: Nutri-Quiz Lógico (Versión de Consola con 10 Preguntas) ---

# --- 1. BASE DE CONOCIMIENTOS (REGLAS) ---
# Se han añadido más reglas para las nuevas preguntas
REGLAS = [
    # Reglas de Hábitos Positivos
    {'if': ['come_frutas_frecuente', 'come_verduras_frecuente'], 'then': 'buen_consumo_vegetales'},
    {'if': ['consume_agua_natural'], 'then': 'buena_hidratacion'},
    {'if': ['come_leguminosas_frecuente'], 'then': 'buen_consumo_proteinas'},
    {'if': ['come_origen_animal_frecuente'], 'then': 'buen_consumo_proteinas'},
    {'if': ['come_cereales_integrales'], 'then': 'buen_consumo_cereales'},
    {'if': ['desayuno_completo'], 'then': 'buen_habito_desayuno'},
    {'if': ['come_variado'], 'then': 'buena_variedad'},
    {'if': ['come_pescado_frecuente'], 'then': 'buen_consumo_omega3'},

    # Reglas de Hábitos a Mejorar (Específicas)
    {'if': ['consume_bebidas_azucaradas'], 'then': 'riesgo_alto_azucar'},
    {'if': ['prefiere_papas_o_dulces'], 'then': 'MENSAJE_ORIENTACION_SNACKS'},
    {'if': ['come_chatarra_semanal'], 'then': 'MENSAJE_ORIENTACION_FRITOS'},
    {'if': ['come_cereales_refinados'], 'then': 'MENSAJE_ORIENTACION_CEREALES'}, # Nueva
    {'if': ['evita_desayuno'], 'then': 'MENSAJE_ORIENTACION_DESAYUNO'}, # Nueva
    {'if': ['desayuno_incompleto'], 'then': 'MENSAJE_ORIENTACION_DESAYUNO'}, # Nueva
    {'if': ['evita_frutas'], 'then': 'MENSAJE_ORIENTACION_FRUTAS'}, # Nueva
    {'if': ['come_poca_variedad'], 'then': 'MENSAJE_ORIENTACION_VARIEDAD'}, # Nueva

    # Reglas de Conclusión (Diagnóstico)
    # Hacemos que "dieta_balanceada" sea más difícil de obtener (más realista)
    {'if': ['buen_consumo_vegetales', 'buena_hidratacion', 'buen_consumo_proteinas', 'buen_habito_desayuno', 'buena_variedad'], 'then': 'dieta_balanceada'},
    
    # Reglas que definen una dieta no balanceada
    {'if': ['riesgo_alto_azucar'], 'then': 'dieta_no_balanceada'},
    {'if': ['MENSAJE_ORIENTACION_SNACKS'], 'then': 'dieta_no_balanceada'},
    {'if': ['MENSAJE_ORIENTACION_FRITOS'], 'then': 'dieta_no_balanceada'},
    {'if': ['evita_verduras'], 'then': 'dieta_no_balanceada'},
    {'if': ['MENSAJE_ORIENTACION_CEREALES'], 'then': 'dieta_no_balanceada'}, # Nueva
    {'if': ['MENSAJE_ORIENTACION_DESAYUNO'], 'then': 'dieta_no_balanceada'}, # Nueva
    {'if': ['MENSAJE_ORIENTACION_FRUTAS'], 'then': 'dieta_no_balanceada'}, # Nueva
    {'if': ['MENSAJE_ORIENTACION_VARIEDAD'], 'then': 'dieta_no_balanceada'}, # Nueva

    # Regla para el peor escenario
    {'if': ['prefiere_papas_o_dulces', 'consume_bebidas_azucaradas'], 'then': 'dieta_muy_desbalanceada'},
    {'if': ['come_chatarra_semanal', 'consume_bebidas_azucaradas'], 'then': 'dieta_muy_desbalanceada'},

    # Reglas para Mensajes (el resultado final)
    {'if': ['dieta_balanceada'], 'then': 'MENSAJE_FELICITACION'},
    {'if': ['dieta_no_balanceada'], 'then': 'MENSAJE_ORIENTACION_GENERAL'},
    {'if': ['riesgo_alto_azucar'], 'then': 'MENSAJE_ORIENTACION_AZUCAR'},
    {'if': ['dieta_muy_desbalanceada'], 'then': 'MENSAJE_ORIENTACION_COMPLETA'},
]


# --- 2. MOTOR DE INFERENCIA (ENCADENAMIENTO HACIA ADELANTE) ---
def motor_inferencia_adelante(hechos_iniciales):
    """
    Aplica el encadenamiento hacia adelante usando la base de REGLAS.
    """
    hechos = set(hechos_iniciales)
    hechos_nuevos_encontrados = True

    print("\n--- [Motor de Inferencia Iniciado] ---")
    while hechos_nuevos_encontrados:
        hechos_nuevos_encontrados = False
        
        for regla in REGLAS:
            premisa_cumplida = True
            for condicion in regla['if']:
                if condicion not in hechos:
                    premisa_cumplida = False
                    break
            
            conclusion = regla['then']
            
            if premisa_cumplida and conclusion not in hechos:
                # ¡Dispara la regla!
                print(f"[Inferencia]: {regla['if']} -> {conclusion}") 
                hechos.add(conclusion)
                hechos_nuevos_encontrados = True
                
    print("--- [Motor de Inferencia Terminado] ---\n")
    return hechos


# --- 3. PREGUNTAS DEL QUIZ (10 PREGUNTAS) ---
PREGUNTAS_QUIZ = [
    # --- Pregunta 1 ---
    {
        'pregunta': 'Cuando tienes mucha sed, ¿qué se te antoja más?',
        'opciones': [
            ('Agua natural', 'consume_agua_natural'),
            ('Jugo de cajita o refresco', 'consume_bebidas_azucaradas'),
            ('Agua de sabor (jamaica, limón)', 'consume_agua_natural'),
        ]
    },
    # --- Pregunta 2 ---
    {
        'pregunta': 'En la comida, ¿qué comes más seguido?',
        'opciones': [
            ('Pollo, pescado o carne', 'come_origen_animal_frecuente'),
            ('Frijoles, lentejas o garbanzos', 'come_leguminosas_frecuente'),
            ('Casi no como de esos', 'ninguno_proteina'),
        ]
    },
    # --- Pregunta 3 ---
    {
        'pregunta': '¿Qué tan seguido comes verduras (brócoli, zanahoria, lechuga)?',
        'opciones': [
            ('¡En casi todas mis comidas!', 'come_verduras_frecuente'),
            ('Algunas veces a la semana', 'come_verduras_ocasional'),
            ('Casi nunca, no me gustan', 'evita_verduras'),
        ]
    },
    # --- Pregunta 4 ---
    {
        'pregunta': 'Si pudieras elegir un snack, ¿cuál sería?',
        'opciones': [
            ('Una fruta (manzana, plátano)', 'snack_fruta'), # Hecho cambiado para no colisionar
            ('Unas papitas o galletas dulces', 'prefiere_papas_o_dulces'),
            ('Un yogurt o un sándwich', 'snack_balanceado'),
        ]
    },
    # --- Pregunta 5 ---
    {
        'pregunta': '¿Con qué frecuencia comes pizza, hamburguesas o alimentos fritos?',
        'opciones': [
            ('Casi nunca (quizás una vez al mes)', 'evita_chatarra'),
            ('Varias veces por semana', 'come_chatarra_semanal'),
            ('Solo en fiestas (1 o 2 veces al mes)', 'evita_chatarra_ocasional'),
        ]
    },
    # --- Pregunta 6 (NUEVA) ---
    {
        'pregunta': 'Cuando comes pan o cereal, ¿cuál eliges más seguido?',
        'opciones': [
            ('Pan blanco o cereal de caja con azúcar', 'come_cereales_refinados'),
            ('Pan integral, avena o cereal de fibra', 'come_cereales_integrales'),
            ('Casi no como pan ni cereal', 'evita_cereales'),
        ]
    },
    # --- Pregunta 7 (NUEVA) ---
    {
        'pregunta': '¿Qué haces normalmente en las mañanas?',
        'opciones': [
            ('Tomo un desayuno completo (ej. huevo, fruta, leche)', 'desayuno_completo'),
            ('Solo como una galleta o un pan rápido', 'desayuno_incompleto'),
            ('Casi nunca desayuno, se me hace tarde', 'evita_desayuno'),
        ]
    },
    # --- Pregunta 8 (NUEVA) ---
    {
        'pregunta': 'Hablando de frutas (manzana, plátano, etc.), ¿cuántas comes al día?',
        'opciones': [
            ('¡Como dos o más! Me encantan.', 'come_frutas_frecuente'),
            ('A veces como una', 'come_frutas_ocasional'),
            ('Casi nunca, se me olvida', 'evita_frutas'),
        ]
    },
    # --- Pregunta 9 (NUEVA) ---
    {
        'pregunta': 'En la semana, ¿tus comidas son...?',
        'opciones': [
            ('¡Muy variadas! Como de todo un poco.', 'come_variado'),
            ('Casi siempre como lo mismo (ej. siempre pollo o siempre pasta)', 'come_poca_variedad'),
            ('No estoy seguro', 'no_sabe_variedad'),
        ]
    },
    # --- Pregunta 10 (NUEVA) ---
    {
        'pregunta': '¿Qué tan seguido comes pescado o atún?',
        'opciones': [
            ('¡Varias veces por semana!', 'come_pescado_frecuente'),
            ('De vez en cuando (1 o 2 veces al mes)', 'come_pescado_ocasional'),
            ('No me gusta / Casi nunca', 'evita_pescado'),
        ]
    }
]


# --- 4. FUNCIONES DE LA APLICACIÓN DE CONSOLA ---

def hacer_quiz():
    """
    Función principal que ejecuta el quiz en la consola.
    """
    hechos_recopilados = []
    print("=================================")
    print("  🍎 ¡Bienvenido al Nutri-Quiz! 🍎")
    print("=================================")
    print("Responde las siguientes 10 preguntas escribiendo el NÚMERO de la opción (ej. 1, 2 o 3).\n")

    # Iterar por cada pregunta en la base de conocimientos
    for i, pregunta_data in enumerate(PREGUNTAS_QUIZ):
        print(f"\n--- Pregunta {i+1} de {len(PREGUNTAS_QUIZ)} ---")
        print(f"{pregunta_data['pregunta']}")
        
        # Imprimir las opciones
        for j, (texto, valor_hecho) in enumerate(pregunta_data['opciones']):
            print(f"  {j+1}. {texto}")
        
        # Obtener y validar la respuesta del usuario
        while True:
            try:
                respuesta_num_str = input("Tu respuesta (número): ")
                respuesta_num = int(respuesta_num_str)
                
                # Validar que el número esté en el rango de opciones
                if 1 <= respuesta_num <= len(pregunta_data['opciones']):
                    # Obtener el "hecho" correspondiente
                    indice = respuesta_num - 1
                    hecho_seleccionado = pregunta_data['opciones'][indice][1]
                    hechos_recopilados.append(hecho_seleccionado)
                    print(f"¡Entendido! (Hecho: {hecho_seleccionado})")
                    break # Salir del bucle while y pasar a la siguiente pregunta
                else:
                    print(f"¡Error! Por favor, escribe un número entre 1 y {len(pregunta_data['opciones'])}.")
            except ValueError:
                print("¡Error! Por favor, escribe solo el número de la opción.")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")

    return hechos_recopilados

def mostrar_resultado_consola(hechos_finales):
    """
    Imprime los resultados finales en la consola basado en los hechos inferidos.
    """
    print("=================================")
    print("     TUS RESULTADOS 🥦")
    print("=================================\n")

    titulo_resultado = "¡Estos son tus resultados!"
    mensaje_resultado = ""
    
    # Lógica para determinar el mensaje (ACTUALIZADA con nuevas reglas)
    if 'MENSAJE_FELICITACION' in hechos_finales and 'MENSAJE_ORIENTACION_GENERAL' not in hechos_finales:
        titulo_resultado = "¡¡Felicidades, Súper Nutri-Chef!! 🥦"
        mensaje_resultado = "¡Tu alimentación es excelente! Sigue así, estás comiendo de forma muy balanceada y saludable.\n\n"
        mensaje_resultado += "Recuerda que comer bien te da energía para jugar, aprender y crecer muy fuerte."
        
    elif 'MENSAJE_ORIENTACION_COMPLETA' in hechos_finales:
        titulo_resultado = "¡Hora de un cambio, campeón! 🚀"
        mensaje_resultado = "Parece que te gustan mucho las bebidas con azúcar y la comida chatarra.\n\n"
        mensaje_resultado += "¡No te preocupes! Podemos mejorar. Intenta cambiar el refresco por agua de frutas y las papitas por un snack saludable (como una manzana o pepino).\n\n"
        mensaje_resultado += "¡Tu cuerpo te lo agradecerá con más energía!"

    elif 'MENSAJE_ORIENTACION_GENERAL' in hechos_finales:
        titulo_resultado = "¡Puedes mejorar! 💪"
        mensaje_resultado = "Vamos por buen camino, pero podemos mejorar algunas cosas.\n\n"
        
        # Lógica corregida para mensajes específicos
        if 'MENSAJE_ORIENTACION_AZUCAR' in hechos_finales:
            mensaje_resultado += "Recuerda que los refrescos y jugos tienen mucha azúcar. ¡Intenta tomar más agua natural!\n\n"
        
        if 'MENSAJE_ORIENTACION_SNACKS' in hechos_finales:
            mensaje_resultado += "Las papitas y galletas son ricas, pero trata de no comerlas tan seguido. ¡Una fruta es un mejor snack!\n\n"
        
        if 'MENSAJE_ORIENTACION_FRITOS' in hechos_finales:
            mensaje_resultado += "La pizza y las hamburguesas son deliciosas, pero es mejor dejarlas para ocasiones especiales. ¡Intenta comer más pollo o pescado hecho en casa!\n\n"

        if 'evita_verduras' in hechos_finales:
             mensaje_resultado += "¡Las verduras son súper poderosas! Intenta comer aunque sea un poquito cada día, ¡te sorprenderá lo ricas que pueden ser!\n\n"
        
        # --- NUEVOS MENSAJES ---
        if 'MENSAJE_ORIENTACION_CEREALES' in hechos_finales:
             mensaje_resultado += "El pan blanco y los cereales de azúcar son ricos, pero no alimentan mucho. Prueba cambiarlos por pan integral o avena, ¡te darán más energía!\n\n"

        if 'MENSAJE_ORIENTACION_DESAYUNO' in hechos_finales:
             mensaje_resultado += "¡El desayuno es la comida más importante! No te lo saltes. Empezar el día con un buen desayuno te ayuda a tener energía y concentrarte en la escuela.\n\n"

        if 'MENSAJE_ORIENTACION_FRUTAS' in hechos_finales:
             mensaje_resultado += "¡Las frutas son como dulces saludables! Intenta comer al menos una o dos al día. Son deliciosas y te dan muchas vitaminas.\n\n"
        
        if 'MENSAJE_ORIENTACION_VARIEDAD' in hechos_finales:
             mensaje_resultado += "Comer siempre lo mismo puede ser aburrido. ¡Intenta probar cosas nuevas! Comer alimentos de diferentes colores ayuda a que tu cuerpo tenga todas las defensas que necesita.\n\n"

    else:
        mensaje_resultado = "¡Gracias por jugar! Recuerda siempre intentar comer un poco de todo: frutas, verduras, carnes y cereales."

    # Imprimir los mensajes formateados
    print(f"*** {titulo_resultado} ***\n")
    print(mensaje_resultado)
    print("\n=================================")


# --- 5. PUNTO DE ENTRADA PRINCIPAL ---
def main():
    """
    Función principal que orquesta la ejecución del programa.
    """
    # 1. Ejecutar el quiz para obtener los hechos iniciales
    hechos_iniciales = hacer_quiz()
    
    print(f"\nHechos iniciales recopilados: {hechos_iniciales}")
    
    # 2. Correr el motor de inferencia
    hechos_finales = motor_inferencia_adelante(hechos_iniciales)
    
    print(f"Hechos finales inferidos: {hechos_finales}")
    
    # 3. Mostrar los resultados al usuario
    mostrar_resultado_consola(hechos_finales)
    
    print("\n¡Gracias por jugar! Presiona Enter para salir.")
    input() # Espera a que el usuario presione Enter para cerrar


# Ejecutar la función principal si el script se corre directamente
if __name__ == "__main__":
    main()