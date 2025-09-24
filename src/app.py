import streamlit as st
# Interfaz de bienvenida para el generador de análisis de flujo de caja
st.set_page_config(page_title="Generador de Análisis de Flujo de Caja", page_icon="💸", layout="centered")

st.title("💸 Generador de Análisis de Flujo de Caja")

st.markdown(
	"""
	¡Bienvenido/a! Esta aplicación te ayuda a analizar el flujo de caja de tu empresa de manera sencilla y visual.
    
	**¿Cómo funciona?**
	1. Prepara tu archivo Excel con las siguientes columnas, en este orden:
		- `PERIODO`: El periodo de análisis (por ejemplo, meses o años).
		- `VENTAS`: Total de ventas en el periodo.
		- `CMV`: Costo de mercancía vendida.
		- `UTILIDAD_BRUTA`: Utilidad bruta obtenida.
		- `GASTOS`: Gastos operativos.
		- `AMORTIZACION`: Gastos de amortización.
		- `UAII`: Utilidad antes de impuestos e intereses.
		- `IMPUESTOS`: Impuestos pagados.
		- `UNETA`: Utilidad neta final.
	2. Sube tu archivo Excel usando el botón de carga.
	3. Visualiza y analiza tu flujo de caja con gráficos y tablas interactivas.
    
	---
    
	**¿Por qué usar esta herramienta?**
	- Te permite entender fácilmente la salud financiera de tu negocio.
	- Obtén insights rápidos y visuales para tomar mejores decisiones.
	- No necesitas conocimientos avanzados de finanzas o programación.
    
	"""
)

st.info("Por favor, sube tu archivo Excel con las columnas indicadas para comenzar el análisis. Ve ala ventana valorador")