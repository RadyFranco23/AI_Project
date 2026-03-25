# 🚀 AI Projects Portfolio

Este repositorio consolida una colección de proyectos avanzados de Inteligencia Artificial aplicados a problemas reales dentro del desarrollo de software moderno. Cada módulo está diseñado bajo principios de *AI Engineering*, combinando modelos de machine learning, arquitecturas cloud-native y patrones de diseño orientados a producción.

El objetivo principal es demostrar la capacidad de diseñar, implementar y desplegar sistemas inteligentes end-to-end, integrando múltiples servicios y frameworks en pipelines robustos, escalables y mantenibles.

---

## 🧠 Áreas cubiertas

* 🎙️ Speech Processing (ASR / TTS)
* 🖼️ Computer Vision
* 🧠 Natural Language Processing (NLP)
* 🧪 Automatización de QA con IA
* 🏗️ Sistemas multi-agente

---

# 📂 Proyectos

## 🎙️ 1. Neural Text-to-Speech (Azure AI)

Este proyecto implementa un sistema de síntesis de voz basado en modelos neuronales proporcionados por Azure Cognitive Services. El sistema permite transformar texto en audio con alta naturalidad, controlando aspectos como entonación, velocidad y estilo mediante SSML.

### 🔧 Arquitectura

* Cliente → API backend → Azure TTS → Stream de audio

### ⚙️ Características técnicas

* Uso de *Neural Voices (WaveNet / Transformer-based)*
* Configuración mediante variables de entorno seguras
* Streaming de audio en tiempo real (low latency)
* Soporte para SSML (Speech Synthesis Markup Language)

### 📌 Mini documentación

| Elemento | Descripción                |
| -------- | -------------------------- |
| Input    | Texto plano o SSML         |
| Output   | Audio en formato WAV/MP3   |
| Paso 1   | Recepción de texto         |
| Paso 2   | Envío a Azure TTS API      |
| Paso 3   | Procesamiento neuronal     |
| Paso 4   | Retorno de stream de audio |

---

## 🎧 2. Speech-to-Text + Translation Pipeline

Pipeline completo de procesamiento de audio que integra reconocimiento de voz automático (ASR) con traducción automática basada en modelos de lenguaje.

### 🔧 Arquitectura

* Ingesta de audio → Whisper (ASR) → Post-procesamiento → Azure OpenAI → Traducción

### ⚙️ Características técnicas

* Modelos *encoder-decoder* para ASR
* Normalización de audio (sample rate, noise handling)
* Procesamiento batch o streaming
* Integración con LLMs para traducción contextual

### 📌 Mini documentación

| Elemento | Descripción                  |
| -------- | ---------------------------- |
| Input    | Archivo de audio o stream    |
| Output   | Texto transcrito + traducido |
| Paso 1   | Captura de audio             |
| Paso 2   | Preprocesamiento             |
| Paso 3   | Transcripción con Whisper    |
| Paso 4   | Traducción con LLM           |
| Paso 5   | Entrega del resultado        |

---

## 🖼️ 3. OCR con Azure Vision

Sistema de reconocimiento óptico de caracteres que permite extraer texto estructurado desde imágenes o documentos.

### 🔧 Arquitectura

* Input (imagen/URL) → Azure Vision API → Parsing estructural → Output JSON

### ⚙️ Características técnicas

* Detección de texto por líneas y palabras
* Bounding boxes con coordenadas
* Layout analysis (estructura del documento)
* Procesamiento remoto vía URL

### 📌 Mini documentación

| Elemento | Descripción                  |
| -------- | ---------------------------- |
| Input    | Imagen local o URL           |
| Output   | JSON con texto y coordenadas |
| Paso 1   | Envío de imagen              |
| Paso 2   | Detección de texto           |
| Paso 3   | Análisis estructural         |
| Paso 4   | Generación de respuesta JSON |

---

## 🎯 4. Object Detection (Azure + ONNX)

Sistema híbrido de detección de objetos que combina inferencia en la nube y ejecución local optimizada.

### 🔧 Arquitectura

* Video stream → Frame extraction → Modelo (Azure / ONNX) → Post-procesamiento → Visualización

### ⚙️ Características técnicas

* Modelos YOLO/SSD/Faster R-CNN
* Inferencia local con ONNX Runtime
* Procesamiento en tiempo real con OpenCV
* Auto-etiquetado de datasets (pseudo-labeling)

### 📌 Mini documentación

| Elemento | Descripción               |
| -------- | ------------------------- |
| Input    | Video o stream            |
| Output   | Frames con bounding boxes |
| Paso 1   | Captura de frames         |
| Paso 2   | Inferencia del modelo     |
| Paso 3   | Detección de objetos      |
| Paso 4   | Renderizado de resultados |

---

## 📧 5. Spam Detector (Machine Learning)

Clasificador de texto basado en técnicas clásicas de machine learning para detección de spam.

### 🔧 Arquitectura

* Input texto → Vectorización → Modelo Naive Bayes → Predicción

### ⚙️ Características técnicas

* Bag of Words / TF-IDF
* Modelo probabilístico (Multinomial Naive Bayes)
* Pipeline reproducible con sklearn
* Evaluación con métricas estándar

### 📌 Mini documentación

| Elemento | Descripción                    |
| -------- | ------------------------------ |
| Input    | Texto                          |
| Output   | Clasificación (Spam / No Spam) |
| Paso 1   | Limpieza de texto              |
| Paso 2   | Vectorización                  |
| Paso 3   | Inferencia del modelo          |
| Paso 4   | Resultado                      |

---

## 🧪 6. AI Test Case Generator

API que automatiza la generación de casos de prueba utilizando modelos de lenguaje.

### 🔧 Arquitectura

* Input (requerimiento) → LLM → Generación → Validación → Iteración

### ⚙️ Características técnicas

* Prompt engineering avanzado
* Generación estructurada de test cases
* Validación automática
* Ciclos de mejora iterativa

### 📌 Mini documentación

| Elemento | Descripción                   |
| -------- | ----------------------------- |
| Input    | Requerimiento funcional       |
| Output   | Casos de prueba estructurados |
| Paso 1   | Recepción del requerimiento   |
| Paso 2   | Generación con LLM            |
| Paso 3   | Validación                    |
| Paso 4   | Corrección iterativa          |

---

## 🧠 7. AI Software Factory (Multi-Agent System)

Sistema basado en agentes inteligentes que automatiza la transformación de requerimientos en artefactos de desarrollo.

### 🔧 Arquitectura

* Input → Agente planner → DAG de tareas → Agentes ejecutores → Persistencia

### ⚙️ Características técnicas

* Sistemas multi-agente
* Orquestación basada en grafos (DAG)
* Generación de artefactos de software
* Persistencia en Azure

### 📌 Mini documentación

| Elemento | Descripción                                 |
| -------- | ------------------------------------------- |
| Input    | Requerimientos                              |
| Output   | Historias de usuario, código, documentación |
| Paso 1   | Parsing del requerimiento                   |
| Paso 2   | Generación de plan                          |
| Paso 3   | Ejecución por agentes                       |
| Paso 4   | Persistencia de resultados                  |

---

# 🛠️ Stack Tecnológico

* Python
* TypeScript / NestJS
* Flask
* PyTorch
* Scikit-learn
* OpenCV
* ONNX Runtime
* Azure OpenAI
* Azure Cognitive Services
* Azure Blob Storage
* Azure Document Intelligence

---

# 💡 Enfoque

* Diseño de sistemas de IA modulares
* Pipelines end-to-end
* Arquitecturas híbridas (cloud + edge)
* Sistemas escalables y orientados a producción

---

# 🔥 Valor

Este portafolio demuestra experiencia en:

* AI Engineering
* Machine Learning aplicado
* NLP y LLMs
* Computer Vision
* Cloud (Azure)
* Automatización del ciclo de desarrollo (SDLC)

---

## 📊 Siguientes mejoras sugeridas

* Diagramas de arquitectura (C4 / UML)
* Diagramas de flujo por proyecto
* Ejemplos de uso (code snippets)
* Benchmarks de rendimiento

---

Si necesitas, puedo ayudarte a:

* Generar diagramas (Mermaid, PlantUML)
* Escribir ejemplos de código para cada módulo
* Preparar endpoints/API specs (OpenAPI/Swagger)


# 👨‍💻 Autor

Radi Franco

