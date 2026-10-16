# Contenido de las pautas. BORRADOR para revisar con residentes antes de usar con pacientes.
# Editá acá y volvé a correr:  python3 generar.py

PAUTAS = [
    {
        "slug": "catarro",
        "titulo": "Catarro",
        "subtitulo": "Resfrío y vías aéreas superiores",
        "color": "azul",
        "que_es": [
            "Es una infección causada por virus. Mejora sola en 7 a 10 días.",
            "La tos y los mocos pueden durar hasta 2 o 3 semanas. Es normal.",
            "Los antibióticos no sirven para los virus.",
        ],
        "cuidados": [
            "Lavados nasales con solución fisiológica antes de comer y de dormir.",
            "Ofrecé líquidos seguido y comidas en poca cantidad.",
            "Elevá un poco la cabecera de la cama o la cuna.",
            "No fumes dentro de la casa ni cerca del chico.",
            "Lavate las manos seguido para no contagiar a otros.",
            "Si tiene fiebre o está molesto, dale el antitérmico en la dosis que te indicó el pediatra.",
        ],
        "evitar": [
            "Jarabes para la tos o descongestivos en menores de 6 años.",
            "Antibióticos sin indicación médica.",
            "Aspirina.",
        ],
        "alarma": [
            "Respira rápido, se le hunden las costillas o hace ruido al respirar.",
            "Tiene los labios o la cara morados.",
            "No quiere tomar líquidos o hace muy poco pis.",
            "Tiene fiebre por más de 3 días.",
            "Está muy dormido, cuesta despertarlo o está muy irritable.",
            "Es menor de 3 meses y tiene 38 °C o más.",
            "Le duele el oído, le sale líquido del oído, o empeora después de haber mejorado.",
        ],
    },
    {
        "slug": "fiebre",
        "titulo": "Fiebre",
        "subtitulo": "Qué hacer en casa",
        "color": "ambar",
        "que_es": [
            "Es fiebre cuando el termómetro marca 38 °C o más en la axila.",
            "La fiebre es una defensa del cuerpo. No daña el cerebro.",
            "El número no dice qué tan grave es. Importa cómo está tu hijo cuando baja la fiebre.",
        ],
        "cuidados": [
            "Usá un termómetro digital.",
            "Vestilo con ropa liviana. No lo abrigues de más.",
            "Ofrecé líquidos seguido.",
            "Dale el antitérmico si está molesto, en la dosis que te indicó el pediatra. El objetivo es que esté cómodo, no llegar a un número.",
            "Si juega y come después de bajar la fiebre, es una buena señal.",
        ],
        "evitar": [
            "Baños con agua fría o paños con alcohol.",
            "Alternar medicamentos sin indicación médica.",
            "Despertarlo solo para darle el antitérmico.",
        ],
        "alarma": [
            "Es menor de 3 meses y tiene 38 °C o más.",
            "Le aparecen manchas en la piel que no se borran al apretarlas con un vaso.",
            "Está decaído o cuesta despertarlo, aun sin fiebre.",
            "Tiene una convulsión.",
            "Le duele mucho la cabeza, tiene la nuca dura o vomita mucho.",
            "Le cuesta respirar.",
            "Hace muy poco pis.",
            "La fiebre dura más de 3 días.",
        ],
    },
    {
        "slug": "gastroenteritis",
        "titulo": "Diarrea y vómitos",
        "subtitulo": "Gastroenteritis aguda",
        "color": "verde",
        # Contenido armado por el equipo médico (PDF del 14/10/2026). Falta revisión final con los residentes.
        "que_es": [
            "La gastroenteritis es un cuadro viral que se caracteriza por diarrea y/o vómitos, con o sin fiebre.",
            "Es muy frecuente en menores de 5 años, más todavía cuando recién empiezan las clases.",
            "Puede durar hasta 7 días y generalmente no es grave.",
        ],
        "cuidados": [],
        "bloques": [
            {
                "titulo": "¡Hidratación primero!",
                "parrafos": [
                    "Los chicos tienen que tomar de base entre 1 y 1,5 litros de agua por día.",
                    "Se rehidratan con agua mineral o con sales de rehidratación oral (SRO).",
                    "Por cada diarrea, tiene que tomar 10 ml por kilo de peso. Por cada vómito, 2 ml por kilo.",
                ],
                "tabla": {
                    "titulo": "Cuánto tomar según el peso",
                    "cols": ["Peso", "Por cada vómito", "Por cada diarrea"],
                    "filas": [
                        ["10 kg", "20 ml", "100 ml"],
                        ["15 kg", "30 ml", "150 ml"],
                        ["20 kg", "40 ml", "200 ml"],
                        ["25 kg", "50 ml", "250 ml"],
                        ["30 kg", "60 ml", "300 ml"],
                    ],
                },
            },
            {
                "titulo": "Cómo preparar las SRO",
                "items": [
                    "Mezclá un sobre de sales en 1 litro de agua.",
                    "El agua tiene que ser de la canilla, hervida antes por 10 minutos.",
                    "Esta preparación dura exactamente 24 horas.",
                    "Anotá en el recipiente el día y la hora en que la preparaste.",
                ],
            },
            {
                "titulo": "Dieta",
                "items": [
                    "Dale de 5 a 6 comidas por día, más chicas.",
                    "Evitá los azúcares (gaseosas, jugos, golosinas, mermeladas, chocolatadas) y las grasas (facturas, frituras, aceite en las comidas, carnes grasosas): pueden aumentar el volumen de la caca.",
                    "Evitá las frutas y verduras de color rojo.",
                    "Podés darle yogur y leche, pero descremados.",
                    "El apetito va a volver de a poco.",
                    "Qué darle: arroz, pastas o papa hervida + pollo a la plancha o hervido + fruta + yogur descremado.",
                ],
            },
            {
                "titulo": "Después de cada vómito",
                "pasos": [
                    "Esperá mínimo 30 minutos antes de darle agua.",
                    "Dale agua o SRO de a poco: una cucharada o 5 ml con jeringa.",
                    "Si vuelve a vomitar, esperá otros 30 minutos.",
                    "Probá con Reliveran gotas niños: 1 gota por kilo. Esperá otros 30 minutos.",
                    "Dale agua de a poco. Si vomita ese agua, andá a la guardia. Si la tolera, seguí dándole de a poco.",
                ],
            },
            {
                "titulo": "Lavado de manos",
                "parrafos": [
                    "El lavado de manos es fundamental para no contagiarse la diarrea.",
                ],
                "items": [
                    "Cada vez que cambiás un pañal.",
                    "Antes y después de cada comida.",
                    "Cada vez que el chico va al baño.",
                ],
            },
        ],
        "evitar": [
            "Rehidratar con gaseosas, jugos o jugos deportivos.",
            "Dar golosinas o frituras.",
            "Dar medicamentos para cortar la diarrea o calmar el dolor.",
            "Dar tés de yuyos.",
            "Mandarlo a la escuela antes de que pasen 24 horas desde que terminó la diarrea.",
            "Dar antibióticos, a menos que los recete el médico.",
        ],
        "alarma": [
            "Vomita todo lo que toma.",
            "Hace pis menos seguido: cada 8 horas o más en menores de 12 meses, cada 12 horas o más en menores de 5 años.",
            "Tiene sangre en la caca o en los vómitos.",
            "Está muy dormido y cuesta despertarlo.",
            "El dolor de panza es constante durante varias horas.",
        ],
    },
]
