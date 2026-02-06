import streamlit as st
import json
import random

# Cargar preguntas
with open("preguntas.json", "r", encoding="utf-8") as file:
    preguntas = json.load(file)

st.title("Quiz Seguridad Industrial y Prevención de Riesgos")

# Inicializar sesión
if "quiz" not in st.session_state:
    st.session_state.quiz = random.sample(preguntas, 4)
    st.session_state.respuestas = {}
    st.session_state.mostrar_resultado = False

# Mostrar preguntas
for i, p in enumerate(st.session_state.quiz):

    st.subheader(f"Pregunta {i+1}")
    st.write(p["pregunta"])

    respuesta = st.radio(
        "Selecciona una opción:",
        ["A", "B", "C"],
        format_func=lambda x: f"{x}) {p[x]}",
        key=f"pregunta_{i}"
    )

    st.session_state.respuestas[i] = respuesta

# Botón evaluar
if st.button("Evaluar"):

    puntos = 0

    for i, p in enumerate(st.session_state.quiz):
        if st.session_state.respuestas.get(i) == p["correcta"]:
            puntos += 1

    calificacion = (puntos / 4) * 10

    st.success(f"Puntos obtenidos: {puntos} / 4")
    st.success(f"Calificación final: {calificacion:.2f} / 10")

# Botón reiniciar
if st.button("Reiniciar Quiz"):

    st.session_state.quiz = random.sample(preguntas, 4)
    st.session_state.respuestas = {}
    st.rerun()
