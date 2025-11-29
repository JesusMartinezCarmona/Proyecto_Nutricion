# --- Proyecto: Nutri-Quiz Lógico (Versión de Consola con 10 Preguntas) ---

# --- 1. BASE DE CONOCIMIENTOS (REGLAS) ---
# Se han añadido más reglas para las nuevas preguntas
import tkinter as tk
from tkinter import messagebox
from tkinter import font 
import random

REGLAS = [
    # Reglas de Hábitos Positivos
    {'if': ['come_frutas_frecuente', 'come_verduras_frecuente'], 'then': 'buen_consumo_vegetales'},
    {'if': ['consume_agua_natural'], 'then': 'buena_hidratacion'},
    {'if': ['come_leguminosas_frecuente'], 'then': 'buen_consumo_proteinas'},
    {'if': ['come_origen_animal_frecuente'], 'then': 'buen_consumo_proteinas'},

    # Reglas de Hábitos a Mejorar
    {'if': ['consume_bebidas_azucaradas'], 'then': 'riesgo_alto_azucar'},
    {'if': ['prefiere_papas_o_dulces'], 'then': 'MENSAJE_ORIENTACION_SNACKS'},
    {'if': ['come_chatarra_semanal'], 'then': 'MENSAJE_ORIENTACION_FRITOS'},
    
    # Reglas de Conclusión (Diagnóstico)
    {'if': ['buen_consumo_vegetales', 'buena_hidratacion', 'buen_consumo_proteinas'], 'then': 'dieta_balanceada'},
    
    # Reglas que definen una dieta no balanceada
    {'if': ['riesgo_alto_azucar'], 'then': 'dieta_no_balanceada'},
    {'if': ['MENSAJE_ORIENTACION_SNACKS'], 'then': 'dieta_no_balanceada'},
    {'if': ['MENSAJE_ORIENTACION_FRITOS'], 'then': 'dieta_no_balanceada'},
    {'if': ['evita_verduras'], 'then': 'dieta_no_balanceada'},

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
    while hechos_nuevos_encontrados:
        hechos_nuevos_encontrados = False
        for regla in REGLAS:
            premisa_cumplida = all(condicion in hechos for condicion in regla['if'])
                conclusion = regla ['then']
                if premisa_cumplida and conclusion not in hechos:
                    hechos.add(conclusion)
                    hechos_nuevos_encontrados = True
    return hechos


# --- 3. PREGUNTAS DEL QUIZ (con Emojis, SIN PUNTOS) ---
# Formato: ('texto de opción', 'hecho')
PREGUNTAS_QUIZ = [
    {
        'pregunta': 'Cuando tienes mucha sed, ¿Qué se te antoja más? 💧',
        'opciones': [
            ('Agua natural 🧊', 'consume_agua_natural'),
            ('Jugo de cajita o refresco 🥤', 'consume_bebidas_azucaradas'),
            ('Agua de sabor (jamaica, limón) 🍋', 'consume_agua_natural'),
        ]
    },
    {
        'pregunta': 'En la comida, ¿Qué comes más seguido? 🍗🥗',
        'opciones': [
            ('Pollo, pescado o carne 🥩', 'come_origen_animal_frecuente'),
            ('Frijoles, lentejas o garbanzos 🌱', 'come_leguminosas_frecuente'),
            ('Casi no como de esos 🤷‍♂️', 'ninguno_proteina'),
        ]
    },
    {
        'pregunta': '¿Qué tan seguido comes verduras (brócoli, zanahoria, lechuga)? 🥕🥦🥬',
        'opciones': [
            ('¡En casi todas mis comidas! ✅', 'come_verduras_frecuente'),
            ('Algunas veces a la semana 🟡', 'come_verduras_ocasional'),
            ('Casi nunca, no me gustan ❌', 'evita_verduras'),
        ]
    },
    {
        'pregunta': 'Si pudieras elegir un snack, ¿uál sería? 🍎🍟',
        'opciones': [
            ('Una fruta (manzana, plátano) 🍌', 'come_frutas_frecuente'),
            ('Unas papitas o galletas dulces 🍪', 'prefiere_papas_o_dulces'),
            ('Un yogurt o un sándwich 🥪', 'snack_balanceado'),
        ]
    },
    {
        'pregunta': '¿Con qué frecuencia comes pizza, hamburguesas o alimentos fritos? 🍕🍔🍟',
        'opciones': [
            ('Casi nunca (una vez al mes) 💯', 'evita_chatarra'),
            ('Varias veces por semana 😱', 'come_chatarra_semanal'),
            ('Solo en fiestas (1 o 2 veces al mes) 🎉', 'evita_chatarra'),
        ]
    }
]


# --- 4. BASE DE CONSEJOS INTERMEDIOS ---
CONSEJOS_INTERMEDIOS = {
    'consume_bebidas_azucaradas': 
        "¡Ojo! Las bebidas azucaradas tienen mucha azúcar que te quita energía. 🛑 Cámbialas por agua de sabor sin azúcar. ¡Tu cuerpo te lo agradecerá!",
    'consume_agua_natural': 
        "¡Excelente elección! El agua es el combustible más importante para tu cerebro y tus músculos. ¡Sigue hidratándote! 🥳",
    'come_origen_animal_frecuente': 
        "Las proteínas te ayudan a construir músculos fuertes. ¡Recuerda combinar con vegetales y leguminosas! 🥗",
    'come_leguminosas_frecuente': 
        "¡Muy bien! Frijoles y lentejas son súper alimentos que te dan energía y fibra. Son proteína vegetal de campeones. 🌱",
    'evita_verduras': 
        "¡Las verduras son tus súper protectores! 🛡️ Te dan vitaminas para no enfermarte. Prueba a comerlas en ensaladas divertidas.",
    'come_verduras_frecuente': 
        "¡Súper! Los colores de las verduras significan vitaminas diferentes. ¡Mientras más colores comas, más fuerte eres! 🌈",
    'prefiere_papas_o_dulces': 
        "Los snacks fritos y dulces son grasas malas. 🚫 La próxima vez, elige un snack divertido como fruta picada o palomitas naturales. 🍿",
    'come_frutas_frecuente': 
        "¡Genial! Las frutas son el 'dulce natural' y te dan mucha energía. ¡Come una diferente cada día! 🍎🍊",
}


# --- 5. CLASE PARA LA VENTANA DE CONSEJOS PERSONALIZADA (Colores Vivos) ---
class ConsejoWindow:
    def __init__(self, parent, title, message):
        self.top = tk.Toplevel(parent)
        self.top.title("Consejo Nutricional")
        self.top.transient(parent) 
        self.top.grab_set()        
        
        # Centrar la ventana
        parent.update_idletasks()
        x = parent.winfo_x() + parent.winfo_width() // 2 - self.top.winfo_width() // 2
        y = parent.winfo_y() + parent.winfo_height() // 2 - self.top.winfo_height() // 2
        self.top.geometry(f"450x300+{x-150}+{y-100}") 
        
        # COLORES VIVOS para la ventana de consejo
        self.top.config(bg="#FFFDE7") # Fondo amarillo muy claro
        
        # Fuentes personalizadas
        consejo_font_titulo = font.Font(family="Arial Black", size=18, weight="bold")
        consejo_font_mensaje = font.Font(family="Verdana", size=14, weight="bold")
        consejo_font_boton = font.Font(family="Verdana", size=12)

        # Título del consejo
        lbl_title = tk.Label(self.top, text=f"💡 {title}", font=consejo_font_titulo, bg="#FFFDE7", fg="#FF5722") 
        lbl_title.pack(pady=(15, 5), padx=10)

        # Mensaje del consejo
        lbl_message = tk.Label(self.top, text=message, font=consejo_font_mensaje, bg="#FFFDE7", fg="#212121", wraplength=400)
        lbl_message.pack(pady=10, padx=20)
        
        # Botón para cerrar
        btn_ok = tk.Button(self.top, text="¡Entendido! 👍", command=self.top.destroy, 
                           font=consejo_font_boton, bg="#FFEB3B", fg="#212121", 
                           activebackground="#FFC107", relief="raised", borderwidth=2)
        btn_ok.pack(pady=15)
        
        self.top.wait_window()

# --- 6. LA APLICACIÓN DE QUIZ (INTERFAZ GRÁFICA) ---

class NutriQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nutri-Quiz Lógico 🍎🥕") 
        self.root.geometry("600x450")
        
        # --- Estilo y Fuentes ---
        self.root.configure(bg="#E8F5E9") # Fondo: Verde Menta Claro
        self.font_titulo = ("Arial Black", 22, "bold") 
        self.font_pregunta = ("Verdana", 14)          
        self.font_opcion = ("Verdana", 12, "bold") 
        self.font_progreso = ("Verdana", 10, "bold") 

        self.indice_pregunta_actual = 0
        self.hechos_recopilados = []
        self.total_preguntas = len(PREGUNTAS_QUIZ)
        
        self.opcion_seleccionada = tk.StringVar()
        
        # --- Crear widgets ---
        self.label_titulo = tk.Label(root, text="¡Bienvenido al Nutri-Quiz! 🎉🥗", font=self.font_titulo, bg="#E8F5E9", fg="#388E3C") # Verde Esmeralda
        self.label_titulo.pack(pady=20)
        
        # Progreso
        self.label_progreso = tk.Label(root, text="", font=self.font_progreso, bg="#E8F5E9", fg="#388E3C")
        self.label_progreso.pack(pady=(0, 10))
        
        self.label_pregunta = tk.Label(root, text="", font=self.font_pregunta, bg="#E8F5E9", fg="#388E3C", wraplength=550)
        self.label_pregunta.pack(pady=5)
        
        self.frame_opciones = tk.Frame(root, bg="#E8F5E9")
        self.frame_opciones.pack(pady=10)
        
        self.radio_buttons = []
        for i in range(3): 
            rb = tk.Radiobutton(self.frame_opciones, text="", variable=self.opcion_seleccionada,
                                value="", font=self.font_opcion, bg="#FFB300", fg="#212121", # Botón: Amarillo Sol
                                activebackground="#FF8F00", selectcolor="#FFB300", 
                                indicatoron=0, 
                                relief="raised", borderwidth=3, 
                                width=40, height=2,
                                tristatevalue="x")
            rb.pack(pady=5)
            self.radio_buttons.append(rb)
            
        self.boton_siguiente = tk.Button(root, text="Siguiente 👉", font=self.font_pregunta, 
                                         bg="#FF5722", fg="white", # Botón Siguiente: Naranja Coral
                                         activebackground="#E64A19",
                                         command=self.siguiente_pregunta)
        self.boton_siguiente.pack(pady=20)
        
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        self.opcion_seleccionada.set(None)
        
        pregunta_data = PREGUNTAS_QUIZ[self.indice_pregunta_actual]
        self.label_pregunta.config(text=pregunta_data['pregunta'])
        
        # Actualizar el contador de progreso (SIN PUNTOS)
        progreso_texto = f"Pregunta {self.indice_pregunta_actual + 1} de {self.total_preguntas}"
        self.label_progreso.config(text=progreso_texto)

        for i, rb in enumerate(self.radio_buttons):
            if i < len(pregunta_data['opciones']):
                # Desempaquetamos la tupla (texto, hecho)
                texto, valor_hecho = pregunta_data['opciones'][i]
                rb.config(text=texto, value=valor_hecho, state="normal") 
            else:
                rb.config(text="", value="", state="disabled")

    def siguiente_pregunta(self):
        hecho_seleccionado = self.opcion_seleccionada.get()
        
        if not hecho_seleccionado or hecho_seleccionado == "None":
            messagebox.showwarning("¡Ojo!", "Por favor, selecciona una opción para continuar.")
            return
            
        self.hechos_recopilados.append(hecho_seleccionado)
        print(f"Hecho añadido: {hecho_seleccionado}") 

        # --- MOSTRAR CONSEJO INTERMEDIO (Ventana llamativa) ---
        if hecho_seleccionado in CONSEJOS_INTERMEDIOS:
            titulo_pregunta = PREGUNTAS_QUIZ[self.indice_pregunta_actual]['pregunta'].split('?')[0].split('(')[0]
            ConsejoWindow(self.root, f"", CONSEJOS_INTERMEDIOS[hecho_seleccionado])

        # Avanzar a la siguiente pregunta
        self.indice_pregunta_actual += 1
        
        if self.indice_pregunta_actual < self.total_preguntas:
            self.mostrar_pregunta()
            if self.indice_pregunta_actual == self.total_preguntas - 1:
                self.boton_siguiente.config(text="¡Ver mi resultado! ✨", bg="#FFC107") # Amarillo para el final
        else:
            self.mostrar_resultado()

    # --- FUNCIÓN MOSTRAR_RESULTADO (SIN PUNTOS) ---
    def mostrar_resultado(self):
        hechos_finales = motor_inferencia_adelante(self.hechos_recopilados)
        
        # Limpiar la pantalla
        self.label_progreso.pack_forget()
        self.label_pregunta.pack_forget()
        self.frame_opciones.pack_forget()
        self.boton_siguiente.pack_forget()
        
        # Lógica de Diagnóstico basada solo en Hechos (Gamificación de Personaje)
        titulo_resultado = "¡Estos son tus resultados! 📊"
        mensaje_resultado = ""
        
        # Definir el personaje/diagnóstico
        if 'MENSAJE_FELICITACION' in hechos_finales:
            titulo_resultado = "¡¡ERES EL CAPITÁN ENERGÍA!! 🦸‍♂️"
            mensaje_resultado += "¡Tu alimentación es excelente! Eres un **Súper Nutri-Chef** con el poder de la salud. Sigue eligiendo alimentos que te hacen fuerte."
            
        elif 'dieta_muy_desbalanceada' in hechos_finales:
            titulo_resultado = "¡GUERRERO DEL AZÚCAR! 🍬"
            mensaje_resultado += "Tienes un gran potencial, pero la comida chatarra y el azúcar están ganando la batalla. ¡Es hora de un entrenamiento nutricional!\n\n"
            mensaje_resultado += "¡No te rindas! Mañana puedes empezar a tomar más agua y probar una verdura nueva."
            
        elif 'MENSAJE_ORIENTACION_GENERAL' in hechos_finales:
            titulo_resultado = "¡DETECTIVE NUTRICIONAL! 🕵️‍♀️"
            mensaje_resultado += "Vas por buen camino, ¡pero tu misión es mejorar algunos hábitos!\n\n"
            
            # Agregar consejos específicos de orientación general
            if 'MENSAJE_ORIENTACION_AZUCAR' in hechos_finales:
                mensaje_resultado += "💧 Tienes que beber más agua y menos refresco. ¡Es tu próximo reto!\n"
            if 'MENSAJE_ORIENTACION_SNACKS' in hechos_finales:
                mensaje_resultado += "🍎 Cambia las papitas por snacks saludables como la fruta.\n"
            if 'evita_verduras' in hechos_finales:
                mensaje_resultado += "🥦 ¡Las verduras son súper poderosas! Intenta comer aunque sea un poquito cada día.\n"
            
        else: 
            titulo_resultado = "¡Buen trabajo! 💪"
            mensaje_resultado += "Tus hábitos son bastante buenos, ¡pero recuerda que siempre hay algo nuevo y saludable que probar! ¡Sigue explorando el mundo de los alimentos!"


        self.label_titulo.config(text=titulo_resultado, fg="#FF5722") 
        
        # Mostrar el mensaje final
        self.label_resultado = tk.Label(self.root, text=mensaje_resultado, font=self.font_pregunta, 
                                         bg="#E8F5E9", fg="#212121", wraplength=550) 
        self.label_resultado.pack(pady=30, padx=20)
        
        self.boton_salir = tk.Button(self.root, text="Salir 🚪", font=self.font_pregunta, 
                                     bg="#FFEB3B", fg="#212121", 
                                     command=self.root.quit)
        self.boton_salir.pack(pady=10)


# --- CÓDIGO PARA EJECUTAR LA APLICACIÓN ---
if __name__ == "__main__":
    main_window = tk.Tk()
    app = NutriQuizApp(main_window)
    main_window.mainloop()
