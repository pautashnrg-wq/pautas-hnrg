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
        "que_es": [
            "Casi siempre la causa un virus. La diarrea puede durar hasta 5 a 7 días.",
            "Lo más importante es que no se deshidrate.",
        ],
        "cuidados": [
            "Dale sales de rehidratación oral después de cada diarrea o vómito.",
            "Si vomita, dale una cucharadita cada 1 o 2 minutos y andá aumentando.",
            "Si toma el pecho, seguí dándole.",
            "Volvé a su comida de siempre apenas tenga hambre.",
            "Lavate bien las manos, sobre todo después de cambiar pañales.",
        ],
        "evitar": [
            "Jugos, gaseosas, bebidas deportivas y caldos de sobre.",
            "Remedios para cortar la diarrea o los vómitos sin indicación médica.",
        ],
        "alarma": [
            "Tiene la boca seca, llora sin lágrimas o tiene los ojos hundidos.",
            "No hace pis en 6 a 8 horas.",
            "Está muy decaído, dormido o irritable.",
            "Vomita todo y no puede tomar las sales.",
            "Tiene sangre en la caca.",
            "Vomita verde.",
            "Tiene dolor de panza fuerte o que no se va.",
        ],
    },
]
