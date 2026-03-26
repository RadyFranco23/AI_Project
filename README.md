#  AI Projects Portfolio

Este repositorio consolida una colección de proyectos avanzados de Inteligencia Artificial aplicados a problemas reales dentro del desarrollo de software moderno. Cada módulo está diseñado bajo principios de *AI Engineering*, combinando modelos de machine learning, arquitecturas cloud-native y patrones de diseño orientados a producción.

El objetivo principal es demostrar la capacidad de diseñar, implementar y desplegar sistemas inteligentes end-to-end, integrando múltiples servicios y frameworks en pipelines robustos, escalables y mantenibles.

---

##  Áreas cubiertas

*  Speech Processing (ASR / TTS)
*  Computer Vision
*  Natural Language Processing (NLP)
*  Automatización de QA con IA
*  Sistemas multi-agente

---

#  Proyectos

##  1. Neural Text-to-Speech (Azure AI)

Este proyecto implementa un sistema de síntesis de voz basado en modelos neuronales proporcionados por Azure Cognitive Services. El sistema permite transformar texto en audio con alta naturalidad, controlando aspectos como entonación, velocidad y estilo mediante SSML.

###  Arquitectura

* Cliente → API backend → Azure TTS → Stream de audio

###  Características técnicas

* Uso de *Neural Voices (WaveNet / Transformer-based)*
* Configuración mediante variables de entorno seguras
* Streaming de audio en tiempo real (low latency)
* Soporte para SSML (Speech Synthesis Markup Language)

###  Documentación

| Elemento | Descripción                |
| -------- | -------------------------- |
| Input    | Texto plano o SSML         |
| Output   | Audio en formato WAV/MP3   |
| Paso 1   | Recepción de texto         |
| Paso 2   | Envío a Azure TTS API      |
| Paso 3   | Procesamiento neuronal     |
| Paso 4   | Retorno de stream de audio |

---

##  2. Speech-to-Text + Translation Pipeline

Pipeline completo de procesamiento de audio que integra reconocimiento de voz automático (ASR) con traducción automática basada en modelos de lenguaje.

###  Arquitectura

* Ingesta de audio → Whisper (ASR) → Post-procesamiento → Azure OpenAI → Traducción

###  Características técnicas

* Modelos *encoder-decoder* para ASR
* Normalización de audio (sample rate, noise handling)
* Procesamiento batch o streaming
* Integración con LLMs para traducción contextual

###  Documentación

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

##  3. OCR con Azure Vision

Sistema de reconocimiento óptico de caracteres que permite extraer texto estructurado desde imágenes o documentos.

###  Arquitectura

* Input (imagen/URL) → Azure Vision API → Parsing estructural → Output JSON

###  Características técnicas

* Detección de texto por líneas y palabras
* Bounding boxes con coordenadas
* Layout analysis (estructura del documento)
* Procesamiento remoto vía URL

###  Documentación

| Elemento | Descripción                  |
| -------- | ---------------------------- |
| Input    | Imagen local o URL           |
| Output   | JSON con texto y coordenadas |
| Paso 1   | Envío de imagen              |
| Paso 2   | Detección de texto           |
| Paso 3   | Análisis estructural         |
| Paso 4   | Generación de respuesta JSON |

---

##  4. Object Detection (Azure + ONNX)

Sistema híbrido de detección de objetos que combina inferencia en la nube y ejecución local optimizada.

###  Arquitectura

* Video stream → Frame extraction → Modelo (Azure / ONNX) → Post-procesamiento → Visualización

###  Características técnicas

* Modelos YOLO/SSD/Faster R-CNN
* Inferencia local con ONNX Runtime
* Procesamiento en tiempo real con OpenCV
* Auto-etiquetado de datasets (pseudo-labeling)

###  Documentación

| Elemento | Descripción               |
| -------- | ------------------------- |
| Input    | Video o stream            |
| Output   | Frames con bounding boxes |
| Paso 1   | Captura de frames         |
| Paso 2   | Inferencia del modelo     |
| Paso 3   | Detección de objetos      |
| Paso 4   | Renderizado de resultados |

---

##  5. Spam Detector (Machine Learning)

Clasificador de texto basado en técnicas clásicas de machine learning para detección de spam.

###  Arquitectura

* Input texto → Vectorización → Modelo Naive Bayes → Predicción

###  Características técnicas

* Bag of Words / TF-IDF
* Modelo probabilístico (Multinomial Naive Bayes)
* Pipeline reproducible con sklearn
* Evaluación con métricas estándar

###  Documentación

| Elemento | Descripción                    |
| -------- | ------------------------------ |
| Input    | Texto                          |
| Output   | Clasificación (Spam / No Spam) |
| Paso 1   | Limpieza de texto              |
| Paso 2   | Vectorización                  |
| Paso 3   | Inferencia del modelo          |
| Paso 4   | Resultado                      |

---

##  6. AI Test Case Generator

API que automatiza la generación de casos de prueba, validacion de los casos de pruebas y la creacion de los script de prueba automatizada utilizando agentes AI.

###  Arquitectura

* Input (requerimiento) → LLM → Generación → Validación → Creacion de scripts

###  Características técnicas

* Prompt engineering avanzado
* Generación estructurada de test cases
* Validación automática
* Ciclos de mejora iterativa

###  Documentación

| Elemento | Descripción                   |
| -------- | ----------------------------- |
| Input    | Requerimiento funcional       |
| Output   | Casos de prueba estructurados |
| Paso 1   | Recepción del requerimiento   |
| Paso 2   | Generación con LLM            |
| Paso 3   | Validación                    |
| Paso 4   | Creacion de scripts automatizados         |

---

##  7. AI Software Factory (Multi-Agent System)

Sistema basado en agentes inteligentes que automatiza la transformación de requerimientos en artefactos de desarrollo.

###  Arquitectura

* Input → Agente planner → DAG de tareas → Agentes ejecutores → Persistencia

###  Características técnicas

* Sistemas multi-agente
* Orquestación basada en grafos (DAG)
* Generación de artefactos de software
* Persistencia en Azure

###  Documentación

| Elemento | Descripción                                 |
| -------- | ------------------------------------------- |
| Input    | Requerimientos                              |
| Output   | Historias de usuario, código, documentación |
| Paso 1   | Parsing del requerimiento                   |
| Paso 2   | Generación de plan                          |
| Paso 3   | Ejecución por agentes                       |
| Paso 4   | Persistencia de resultados                  |

---

Modelos y Experimentos de Deep Learning

Esta sección describe implementaciones fundamentales de modelos de deep learning desarrollados como base para los sistemas del portafolio. Estos componentes demuestran dominio de arquitecturas neuronales, entrenamiento de modelos y técnicas avanzadas de optimización.

8. Clasificador de Texto con LSTM (NLP)

Implementación de un modelo de procesamiento de lenguaje natural basado en redes neuronales recurrentes (LSTM) para clasificación de sentimiento en texto.

Descripción técnica

En este módulo se construye un pipeline completo de NLP que incluye tokenización, construcción de vocabulario y entrenamiento de un modelo secuencial. Se utiliza torchtext para la gestión de datos y spaCy para la tokenización, permitiendo un flujo estructurado desde texto crudo hasta embeddings.

El modelo utiliza una capa de Embedding + LSTM, seguida de regularización con dropout y una capa fully connected para clasificación binaria.

Lo que hago en este archivo
Implemento tokenización y normalización de texto usando spaCy
Construyo el vocabulario dinámico a partir del dataset
Diseño una arquitectura LSTM para clasificación de sentimientos
Entreno el modelo con BCEWithLogitsLoss y optimización Adam
Evalúo el modelo en dataset de test
Implemento inferencia sobre texto libre (predicción en producción)

📄 Archivo:

9. Clasificación de Imágenes con Red Neuronal Feedforward (MNIST)

Modelo base de deep learning para clasificación de dígitos utilizando el dataset MNIST.

Descripción técnica

Se implementa una red neuronal fully connected (MLP) que procesa imágenes transformadas a vectores. Este módulo demuestra el flujo completo de entrenamiento: carga de datos, batching, forward/backward pass y persistencia del modelo.

Lo que hago en este archivo
Preprocesamiento de imágenes con ToTensor()
División del dataset en entrenamiento, validación y prueba
Diseño de una red neuronal densa (MLP)
Implementación manual del loop de entrenamiento
Cálculo de métricas de exactitud
Serialización del modelo (.pth)
Generación de input estructurado para integración con APIs

📄 Archivo:

10. Clasificación de Imágenes con CNN (CIFAR-10)

Implementación de una red neuronal convolucional para clasificación de imágenes en múltiples clases.

Descripción técnica

Este modelo aplica una arquitectura CNN con múltiples bloques convolucionales, max pooling y dropout, optimizada para clasificación en el dataset CIFAR-10. Se ejecuta entrenamiento en GPU cuando está disponible.

Lo que hago en este archivo
Normalización de imágenes RGB
Construcción de arquitectura CNN (Conv + ReLU + Pooling)
Regularización mediante dropout
Implementación de entrenamiento y validación
Uso de GPU para acelerar entrenamiento
Visualización de predicciones sobre imágenes reales

📄 Archivo:

11. Modelos Secuenciales: RNN, LSTM y GRU

Implementación comparativa de arquitecturas recurrentes para predicción de secuencias de texto.

Descripción técnica

Este módulo demuestra el funcionamiento interno de modelos secuenciales mediante la predicción de la siguiente palabra en una frase. Se implementan tres variantes: RNN básica, LSTM y GRU, permitiendo comparar su comportamiento y capacidad de memoria.

Lo que hago en este archivo
Construyo un vocabulario manual y codificación de tokens
Transformo secuencias de texto en tensores
Implemento desde cero tres arquitecturas recurrentes:
RNN básica
LSTM
GRU
Diseño el forward pass para predicción de secuencia
Comparo enfoques de modelado secuencial

📄 Archivo:

12. Técnicas de Regularización en Deep Learning

Implementación práctica de estrategias para mejorar la generalización de modelos.

Descripción técnica

Se exploran múltiples técnicas de regularización aplicadas a redes neuronales, abordando overfitting y estabilidad del entrenamiento.

Lo que hago en este archivo
Implemento Dropout para evitar co-adaptación de neuronas
Integro Batch Normalization para estabilizar activaciones
Aplico L2 Regularization (weight decay) desde el optimizador
Simulo Early Stopping basado en validación
Aplico Data Augmentation para enriquecer datasets de imágenes

📄 Archivo:

13. Transfer Learning con ResNet (Deep Learning avanzado)

Implementación de transferencia de aprendizaje utilizando modelos preentrenados.

Descripción técnica

Se utiliza ResNet18 preentrenado en ImageNet como extractor de características, adaptándolo a un nuevo problema (CIFAR-10) mediante fine-tuning parcial.

Lo que hago en este archivo
Cargo un modelo preentrenado (ResNet18)
Congelo capas para usar feature extraction
Reemplazo la capa final para clasificación personalizada
Entreno únicamente la capa fully connected
Ajusto imágenes al formato requerido por el modelo
Evalúo predicciones sobre datos reales

#  Stack Tecnológico

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

#  Enfoque

* Diseño de sistemas de IA modulares
* Pipelines end-to-end
* Arquitecturas híbridas (cloud + edge)
* Sistemas escalables y orientados a producción

---

#  Valor

Este portafolio demuestra experiencia en:

* AI Engineering
* Machine Learning aplicado
* NLP y LLMs
* Computer Vision
* Cloud (Azure)
* Automatización del ciclo de desarrollo (SDLC)

---


#  Autor

Radi Franco

