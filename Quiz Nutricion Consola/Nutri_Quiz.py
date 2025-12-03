# --- Proyecto: Nutri-Quiz Lógico ---


import tkinter as tk
from tkinter import messagebox
import time
import random

# ==========================================
# 1. LÓGICA Y REGLAS (CEREBRO)
# ==========================================

# [LEY APLICABLE]: Norma Oficial Mexicana NOM-043-SSA2-2012
# "Servicios básicos de salud. Promoción y educación para la salud en materia alimentaria."
# Esta estructura de datos codifica los criterios del 'Plato del Bien Comer', clasificando
# hábitos en positivos o negativos según la frecuencia de consumo de los 3 grupos de alimentos.
REGLAS = [
    # Reglas de Hábitos Positivos (Criterio: Inclusión diaria de grupos alimenticios)
    {'if': ['come_frutas_frecuente', 'come_verduras_frecuente'], 'then': 'buen_consumo_vegetales'},
    {'if': ['consume_agua_natural'], 'then': 'buena_hidratacion'},
    {'if': ['come_leguminosas_frecuente'], 'then': 'buen_consumo_proteinas'},
    {'if': ['come_origen_animal_frecuente'], 'then': 'buen_consumo_proteinas'},
    {'if': ['come_cereales_integrales'], 'then': 'buen_consumo_cereales'},

    # Reglas de Hábitos a Mejorar (Criterio: Reducción de azúcares y grasas saturadas)
    {'if': ['consume_bebidas_azucaradas'], 'then': 'riesgo_alto_azucar'},
    
    # Mensajes directos de orientación
    {'if': ['prefiere_papas_o_dulces'], 'then': 'MENSAJE_ORIENTACION_SNACKS'},
    {'if': ['come_chatarra_semanal'], 'then': 'MENSAJE_ORIENTACION_FRITOS'},
    
    # Diagnósticos Integrales
    {'if': ['buen_consumo_vegetales', 'buena_hidratacion', 'buen_consumo_proteinas'], 'then': 'dieta_balanceada'},
    {'if': ['riesgo_alto_azucar'], 'then': 'dieta_no_balanceada'},
    {'if': ['MENSAJE_ORIENTACION_SNACKS'], 'then': 'dieta_no_balanceada'},
    {'if': ['MENSAJE_ORIENTACION_FRITOS'], 'then': 'dieta_no_balanceada'},
    {'if': ['evita_verduras'], 'then': 'dieta_no_balanceada'},

    # Detección de Riesgo (Criterio: Exceso calórico y deficiencia de micronutrientes)
    {'if': ['prefiere_papas_o_dulces', 'consume_bebidas_azucaradas'], 'then': 'dieta_muy_desbalanceada'},
    {'if': ['come_chatarra_semanal', 'consume_bebidas_azucaradas'], 'then': 'dieta_muy_desbalanceada'},

    # Resultados Finales para Feedback
    {'if': ['dieta_balanceada'], 'then': 'MENSAJE_FELICITACION'},
    {'if': ['dieta_no_balanceada'], 'then': 'MENSAJE_ORIENTACION_GENERAL'},
    {'if': ['riesgo_alto_azucar'], 'then': 'MENSAJE_ORIENTACION_AZUCAR'},
    {'if': ['dieta_muy_desbalanceada'], 'then': 'MENSAJE_ORIENTACION_COMPLETA'},
]

# [LEY APLICABLE]: Ley General de Salud & Recomendaciones de la OMS
# Se integran cápsulas informativas que refuerzan la educación higiénica (lavado de manos),
# la importancia de la hidratación (agua simple) y la variedad en la dieta.
TIPS_NUTRICIONALES = [
    "💡 ¡DATO CURIOSO!\nSegún el 'Plato del Buen Comer', ninguna comida es más importante que otra.\n¡El secreto es combinar los 3 grupos!",
    "🚿 ZONA DE HIGIENE\n¿Sabías que lavarte las manos antes de comer es la regla #1 de un Nutri-Ninja?\n¡Los microbios no están invitados!",
    "💧 HIDRATACIÓN\nTu cuerpo es 60% agua.\n¡Necesitas agua simple potable para pensar rápido y no secarte como una pasita!",
    "🏃‍♂️ ENERGÍA PURA\nLos cereales (como el maíz, avena y arroz) son la 'gasolina' del cuerpo.\n¡Son perfectos para correr en el recreo!",
    "🛡️ ESCUDO PROTECTOR\nLas frutas y verduras tienen vitaminas invisibles.\nFuncionan como un escudo mágico contra las gripas.",
    "🦷 DIENTES DE ACERO\nMasticar despacio ayuda a tu pancita y mantiene tus dientes fuertes.\n¡Disfruta cada bocado, no hay prisa!",
    "🌈 ARCOÍRIS EN TU PLATO\nIntenta que tu plato tenga muchos colores.\nEntre más colores (verde, rojo, naranja), ¡más saludable es!",
]

# [LEY LÓGICA]: Modus Ponendo Ponens (Ley de la Separación)
# En lógica de primer orden: Si P implica Q, y P es verdadero, entonces Q es verdadero.
# Esta función aplica el algoritmo de "Encadenamiento hacia Adelante" para derivar conclusiones
# a partir de los hechos base proporcionados por el usuario.
def motor_inferencia_adelante(hechos_iniciales):
    hechos = set(hechos_iniciales)
    hechos_nuevos_encontrados = True
    while hechos_nuevos_encontrados:
        hechos_nuevos_encontrados = False
        for regla in REGLAS:
            premisa_cumplida = True
            for condicion in regla['if']:
                if condicion not in hechos:
                    premisa_cumplida = False
                    break
            conclusion = regla['then']
            # Aplicación de la regla si la conclusión es nueva
            if premisa_cumplida and conclusion not in hechos:
                hechos.add(conclusion)
                hechos_nuevos_encontrados = True
    return hechos

# [CONFIGURACIÓN]: Base de Datos de Preguntas
# Mapeo directo entre preguntas amigables y los hechos lógicos que activan el sistema.
PREGUNTAS_QUIZ = [
    {
        'pregunta': '🥵 Tienes MUCHA sed después de jugar fútbol, ¿qué se te antoja?',
        'icono': '💧',
        'opciones': [
            ('¡Agua natural helada!', 'consume_agua_natural', '#4FC3F7'),
            ('Jugo de cajita o refresco', 'consume_bebidas_azucaradas', '#FF8A65'),
            ('Agüita de limón o jamaica', 'consume_agua_natural', '#AED581'),
        ]
    },
    {
        'pregunta': '🍽️ Es hora de la comida, ¿qué plato se ve más rico?',
        'icono': '🍗',
        'opciones': [
            ('Pollo, pescado o carnita', 'come_origen_animal_frecuente', '#FFD54F'), 
            ('Un plato de frijoles o lentejas', 'come_leguminosas_frecuente', '#A1887F'),
            ('Mmm... nada de eso me gusta', 'ninguno_proteina', '#E0E0E0'),
        ]
    },
    {
        'pregunta': '🥦 ¿Se te antojan unas verduras (brócoli, zanahoria)?',
        'icono': '🥗',
        'opciones': [
            ('¡Me encantan! Como siempre', 'come_verduras_frecuente', '#81C784'),
            ('A veces, si me obligan...', 'come_verduras_ocasional', '#FFB74D'),
            ('¡Guácala! No me gustan', 'evita_verduras', '#E57373'),
        ]
    },
    {
        'pregunta': '🎒 Recreo: Tienes hambre, ¿qué sacas de tu lonchera?',
        'icono': '🍎',
        'opciones': [
            ('Una fruta picada', 'come_frutas_frecuente', '#FFF176'),
            ('Unas papitas o galletas', 'prefiere_papas_o_dulces', '#FF8A65'),
            ('Un sándwich o yogurt', 'snack_balanceado', '#4DB6AC'),
        ]
    },
    {
        'pregunta': '🍕 Fin de semana de películas, ¿cenamos una pizza o hamburguesas?',
        'icono': '🍔',
        'opciones': [
            ('Casi nunca comemos eso', 'evita_chatarra', '#64B5F6'),
            ('¡Pizza o Hamburguesa! (Muy seguido)', 'come_chatarra_semanal', '#F06292'),
            ('Solo en fiestas especiales', 'evita_chatarra', '#BA68C8'),
        ]
    },
    {
        'pregunta': '🥣 ¡Buenos días! ¿Qué desayunas antes de ir a la escuela?',
        'icono': '☀️',
        'opciones': [
            ('Avena, amaranto o cereal sin azúcar', 'come_cereales_integrales', '#FFECB3'),
            ('Cereal de cajita de colores (¡muy dulce!)', 'riesgo_alto_azucar', '#EF9A9A'),
            ('Un huevito con tortilla', 'come_origen_animal_frecuente', '#FFF59D'),
        ]
    },
    {
        'pregunta': '🧁 Te ofrecen un postre después de comer, ¿cuál eliges?',
        'icono': '🍰',
        'opciones': [
            ('Una rebanada de pastel o chocolate', 'prefiere_papas_o_dulces', '#F48FB1'),
            ('Una gelatina o arroz con leche', 'snack_balanceado', '#CE93D8'),
            ('Unas fresas o mango picado', 'come_frutas_frecuente', '#C5E1A5'),
        ]
    },
    {
        'pregunta': '🍜 Hace frío y hay sopa caliente, ¿cuál prefieres?',
        'icono': '🍲',
        'opciones': [
            ('Sopa de verduras o consomé de pollo', 'come_verduras_frecuente', '#A5D6A7'),
            ('Sopa instantánea (de vasito)', 'come_chatarra_semanal', '#FFAB91'),
            ('Crema de elote o zanahoria', 'come_verduras_ocasional', '#FFE082'),
        ]
    },
    {
        'pregunta': '🥛 ¿Qué tomas usualmente durante la cena?',
        'icono': '🌙',
        'opciones': [
            ('Un vaso de leche o agua', 'buena_hidratacion', '#90CAF9'),
            ('Refresco o té helado dulce', 'consume_bebidas_azucaradas', '#B0BEC5'),
            ('Chocolate caliente con malvaviscos', 'riesgo_alto_azucar', '#D7CCC8'),
        ]
    },
    {
        'pregunta': '🌮 Vas a una fiesta mexicana, ¿qué pides de comer?',
        'icono': '🎉',
        'opciones': [
            ('3 Tacos de guisado o carne', 'come_origen_animal_frecuente', '#FFCC80'),
            ('Solo quesadillas fritas', 'come_chatarra_semanal', '#FFAB91'),
            ('Esquites o elote cocido', 'come_cereales_integrales', '#FFF59D'),
        ]
    }
]

# ==========================================
# 2. INTERFAZ GRÁFICA DIVERTIDA (GUI)
# ==========================================

# [PRINCIPIO DE DISEÑO]: Herencia y Polimorfismo (OOP)
# Se extiende la clase Button de Tkinter para crear un componente visual personalizado
# que mejora la experiencia de usuario (UX) mediante retroalimentación visual (hover).
class BotonOpcion(tk.Button):
    """Un botón personalizado que cambia de color y crece al pasar el mouse"""
    def __init__(self, master, color_base, **kwargs):
        super().__init__(master, **kwargs)
        self.color_base = color_base
        self.color_hover = self.aclarar_color(color_base)
        self.configure(bg=self.color_base, fg="#333", font=("Verdana", 11, "bold"), 
                       relief="flat", activebackground=self.color_hover, cursor="hand2")
        
        # Binding de eventos para interacción dinámica
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.configure(bg=self.color_hover)
        self.pack_configure(ipadx=10, ipady=5) 

    def on_leave(self, e):
        self.configure(bg=self.color_base)
        self.pack_configure(ipadx=0, ipady=0)

    def aclarar_color(self, hex_color):
        return "#FFFFFF" 

# [PRINCIPIO DE DISEÑO]: Separación de Intereses (Separation of Concerns)
# Esta clase maneja exclusivamente la Capa de Vista (interfaz gráfica y animaciones),
# delegando la lógica de negocio al motor de inferencia externo.
class NutriQuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🍏 Nutri-Quiz 🚀")
        self.root.geometry("700x650") # Un poco más alto para los tips
        self.root.configure(bg="#E0F7FA")
        
        self.hechos_recopilados = []
        self.indice_pregunta = 0
        
        # --- ELEMENTOS DE LA UI ---
        
        # 1. Barra de Progreso
        self.frame_progreso = tk.Frame(root, bg="#B2EBF2", height=20)
        self.frame_progreso.pack(fill="x", side="top")
        self.barra_relleno = tk.Frame(self.frame_progreso, bg="#00BCD4", width=10, height=20)
        self.barra_relleno.pack(side="left")
        
        # 2. Canvas para mascota (Feedback Visual Continuo)
        self.canvas_mascota = tk.Canvas(root, width=700, height=120, bg="#E0F7FA", highlightthickness=0)
        self.canvas_mascota.pack(pady=5)
        self.mascota_id = self.canvas_mascota.create_text(350, 60, text="🍎", font=("Arial", 60))
        self.direccion_salto = -1
        self.animar_mascota()

        # 3. Área de Contenido (Tarjeta cambiante)
        self.frame_pregunta = tk.Frame(root, bg="white", bd=5, relief="ridge")
        self.frame_pregunta.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Elementos dentro de la tarjeta (se ocultan/muestran)
        self.lbl_icono = tk.Label(self.frame_pregunta, text="", font=("Arial", 40), bg="white")
        self.lbl_icono.pack(pady=5)

        self.lbl_pregunta = tk.Label(self.frame_pregunta, text="", font=("Comic Sans MS", 16, "bold"), 
                                     bg="white", fg="#006064", wraplength=550)
        self.lbl_pregunta.pack(pady=10)

        self.frame_botones = tk.Frame(self.frame_pregunta, bg="white")
        self.frame_botones.pack(pady=10, fill="x", padx=50)

        self.cargar_pregunta()

    # [LÓGICA DE ANIMACIÓN]: Bucle de actualización (Game Loop pattern simplificado)
    def animar_mascota(self):
        coords = self.canvas_mascota.coords(self.mascota_id)
        if coords:
            y = coords[1]
            if y < 40: self.direccion_salto = 1
            if y > 80: self.direccion_salto = -1
            self.canvas_mascota.move(self.mascota_id, 0, self.direccion_salto)
        # Recursión temporal para mantener la animación fluida
        self.root.after(40, self.animar_mascota)

    def escribir_texto_maquina(self, widget, texto, index=0):
        if index == 0:
            widget.config(text="")
        if index < len(texto):
            widget.config(text=widget.cget("text") + texto[index])
            self.root.after(15, self.escribir_texto_maquina, widget, texto, index + 1) # Un poco más rápido

    def actualizar_progreso(self):
        total = len(PREGUNTAS_QUIZ)
        progreso = (self.indice_pregunta / total)
        ancho_ventana = 700
        nuevo_ancho = int(ancho_ventana * progreso)
        self.barra_relleno.config(width=nuevo_ancho)

    def cargar_pregunta(self):
        # Asegurarnos de que los elementos principales son visibles (por si venimos de un tip)
        self.lbl_icono.pack(pady=5)
        self.lbl_pregunta.pack(pady=10)
        self.frame_botones.pack(pady=10, fill="x", padx=50)

        # Limpiar botones anteriores
        for widget in self.frame_botones.winfo_children():
            widget.destroy()

        if self.indice_pregunta < len(PREGUNTAS_QUIZ):
            datos = PREGUNTAS_QUIZ[self.indice_pregunta]
            self.actualizar_progreso()
            
            self.lbl_icono.config(text=datos['icono'])
            self.escribir_texto_maquina(self.lbl_pregunta, datos['pregunta'])

            for texto, valor, color in datos['opciones']:
                btn = BotonOpcion(self.frame_botones, color_base=color, text=texto, 
                                  command=lambda v=valor: self.seleccionar_respuesta(v))
                btn.pack(fill="x", pady=5, ipady=5)
        else:
            self.mostrar_resultados()

    def seleccionar_respuesta(self, valor):
        self.hechos_recopilados.append(valor)
        self.indice_pregunta += 1
        
        # --- LÓGICA DE TIPS ---
        # Si aún quedan preguntas, mostramos un tip
        if self.indice_pregunta < len(PREGUNTAS_QUIZ):
            self.mostrar_tip()
        else:
            # Si es la última, vamos directo al resultado
            self.cargar_pregunta()

    # [PRINCIPIO PEDAGÓGICO]: Reforzamiento Intermitente y Aprendizaje a Ritmo Propio
    # Se introduce contenido educativo (Tips) entre las fases de evaluación.
    # Cambio: Ahora requiere acción del usuario para avanzar, permitiendo lectura completa.
    def mostrar_tip(self):
        """Muestra una pantalla intermedia con un consejo nutricional"""
        # 1. Ocultar la interfaz de pregunta
        self.frame_botones.pack_forget()
        self.lbl_pregunta.pack_forget()
        self.lbl_icono.pack_forget()
        
        # 2. Seleccionar un tip aleatorio
        tip_actual = random.choice(TIPS_NUTRICIONALES)
        
        # 3. Crear el contenido del tip (Frame Temporal)
        self.frame_tip = tk.Frame(self.frame_pregunta, bg="#FFF59D", bd=0) # Amarillo claro
        self.frame_tip.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título del Tip
        lbl_titulo = tk.Label(self.frame_tip, text="✨ ¿SABÍAS QUÉ? ✨", 
                              font=("Comic Sans MS", 20, "bold"), bg="#FFF59D", fg="#F57F17")
        lbl_titulo.pack(pady=(30, 10))
        
        # Emoji Nerd
        lbl_emoji = tk.Label(self.frame_tip, text="🤓", font=("Arial", 60), bg="#FFF59D")
        lbl_emoji.pack(pady=5)
        
        # Texto del tip
        lbl_texto = tk.Label(self.frame_tip, text=tip_actual, 
                             font=("Verdana", 14), bg="#FFF59D", fg="#3E2723",
                             wraplength=450, justify="center")
        lbl_texto.pack(pady=20)
        
        # 4. Botón para continuar (CONTROL DE USUARIO)
        # Se elimina el timer automático y se agrega un botón explícito
        btn_continuar = tk.Button(self.frame_tip, text="¡Entendido, Siguiente! ▶", 
                                  command=self.cerrar_tip,
                                  bg="#FF9800", fg="white", font=("Arial", 13, "bold"),
                                  cursor="hand2", relief="raised", borderwidth=3)
        btn_continuar.pack(pady=20)

    def cerrar_tip(self):
        """Destruye el tip y carga la siguiente pregunta"""
        if hasattr(self, 'frame_tip'):
            self.frame_tip.destroy()
        
        # Llamamos a cargar_pregunta, que se encarga de restaurar la visibilidad
        self.cargar_pregunta()

    # [EVALUACIÓN Y DIAGNÓSTICO]:
    # Función final que integra los hechos inferidos para ofrecer una retroalimentación formativa,
    # alineada con los objetivos de la educación para la salud.
    def mostrar_resultados(self):
        self.barra_relleno.config(width=700)
        self.frame_botones.destroy()
        self.lbl_icono.destroy()
        
        hechos_finales = motor_inferencia_adelante(self.hechos_recopilados)
        
        titulo = "¡Terminaste!"
        mensaje = ""
        es_bueno = False

        if 'MENSAJE_FELICITACION' in hechos_finales and 'MENSAJE_ORIENTACION_GENERAL' not in hechos_finales:
            titulo = "🏆 ¡ERES UN MAESTRO NUTRI-EXPERTO! 🏆"
            mensaje = "¡Increíble! Comes súper saludable.\nTu cuerpo tiene toda la energía para correr, saltar y sacar dieces."
            self.canvas_mascota.itemconfigure(self.mascota_id, text="😎")
            es_bueno = True
        elif 'MENSAJE_ORIENTACION_COMPLETA' in hechos_finales:
            titulo = "⚠️ ¡ALERTA DE EMERGENCIA! ⚠️"
            mensaje = "Houston, tenemos un problema. Estás comiendo mucha azúcar y grasas.\n¡Tu cuerpo necesita gasolina de calidad! Intenta comer una fruta mañana."
            self.canvas_mascota.itemconfigure(self.mascota_id, text="🤒")
        else:
            titulo = "✨ ¡VAS BIEN, PERO PUEDES MEJORAR! ✨"
            self.canvas_mascota.itemconfigure(self.mascota_id, text="🤔")
            
            if 'MENSAJE_ORIENTACION_AZUCAR' in hechos_finales:
                mensaje += "• Mucho ojo con los refrescos, ¡son bombas de azúcar!\n"
            if 'MENSAJE_ORIENTACION_SNACKS' in hechos_finales:
                mensaje += "• Cambia las papitas por palomitas caseras o fruta.\n"
            if 'MENSAJE_ORIENTACION_FRITOS' in hechos_finales:
                mensaje += "• La comida rápida es rica, pero solo de vez en cuando.\n"
            if 'evita_verduras' in hechos_finales:
                mensaje += "• ¡Dale una oportunidad al brócoli! Te da súper fuerza.\n"
            
            if mensaje == "": mensaje = "Trata de comer más variado y colorido."

        self.lbl_pregunta.config(text=titulo, fg="#E91E63", font=("Arial", 22, "bold"))
        
        lbl_msg = tk.Label(self.frame_pregunta, text=mensaje, font=("Verdana", 14), 
                           bg="white", justify="center", wraplength=500)
        lbl_msg.pack(pady=20)

        # Botón estándar (se verá si NO hay confeti)
        btn_salir = tk.Button(self.frame_pregunta, text="Salir del Juego", command=self.root.quit,
                              bg="#FF5722", fg="white", font=("Arial", 12, "bold"))
        btn_salir.pack(pady=20)

        if es_bueno:
            self.lanzar_confeti()

    def lanzar_confeti(self):
        self.canvas_mascota.pack_forget()
        
        # Ajustamos height a 650 para cubrir toda la ventana
        c = tk.Canvas(self.root, width=700, height=650, bg="#E0F7FA", highlightthickness=0)
        c.place(x=0, y=0) 
        c.create_text(350, 250, text="🎉 ¡FELICIDADES! 🎉", font=("Comic Sans MS", 40, "bold"), fill="#E91E63")
        
        # --- CORRECCIÓN: Botón de Salir DENTRO de la pantalla de celebración ---
        # Como este canvas tapa al botón anterior, creamos uno nuevo aquí dentro
        btn_salir_fiesta = tk.Button(self.root, text="Salir del Juego", command=self.root.quit,
                                     bg="#FF5722", fg="white", font=("Arial", 14, "bold"), 
                                     cursor="hand2", relief="raised", borderwidth=3)
        
        # Lo colocamos en el canvas (coordenada x=350, y=450)
        c.create_window(350, 450, window=btn_salir_fiesta)
        
        colores = ['#F44336', '#2196F3', '#FFEB3B', '#4CAF50', '#9C27B0']
        
        particulas = []
        for _ in range(100):
            x = random.randint(0, 700)
            y = random.randint(-500, 0)
            color = random.choice(colores)
            size = random.randint(5, 15)
            obj = c.create_oval(x, y, x+size, y+size, fill=color, outline="")
            particulas.append({'id': obj, 'speed': random.randint(2, 8)})

        def mover_confeti():
            for p in particulas:
                c.move(p['id'], 0, p['speed'])
                if c.coords(p['id'])[1] > 650: # Ajustado al nuevo alto
                    c.move(p['id'], 0, -700)
            self.root.after(30, mover_confeti)

        mover_confeti()

if __name__ == "__main__":
    main_window = tk.Tk()
    app = NutriQuizGame(main_window)
    main_window.mainloop()
