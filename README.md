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

## 8. Clasificador de Texto con LSTM (NLP)

Implementación de un modelo de procesamiento de lenguaje natural basado en redes neuronales recurrentes (LSTM) para clasificación de sentimientos en texto.

###  Arquitectura

Texto → Tokenización (spaCy) → Embedding → LSTM → Fully Connected → Predicción

###  Características técnicas

* Tokenización y normalización de texto con spaCy
* Construcción de vocabulario dinámico con torchtext
* Uso de embeddings entrenables
* Arquitectura LSTM para modelado secuencial
* Regularización con Dropout
* Entrenamiento con BCEWithLogitsLoss

###  Documentación

| Elemento | Descripción                         |
| -------- | ----------------------------------- |
| Input    | Texto                               |
| Output   | Clasificación (Positivo / Negativo) |
| Paso 1   | Tokenización del texto              |
| Paso 2   | Conversión a índices (vocabulario)  |
| Paso 3   | Embedding + LSTM                    |
| Paso 4   | Clasificación final                 |

---

## 9. Clasificación de Imágenes (MNIST - MLP)

Modelo base de deep learning para clasificación de dígitos escritos a mano utilizando una red neuronal completamente conectada.

###  Arquitectura

Imagen (28x28) → Flatten → Red neuronal (MLP) → Predicción

###  Características técnicas

* Preprocesamiento con ToTensor
* División de dataset (train/val/test)
* Red neuronal fully connected (MLP)
* Entrenamiento con CrossEntropyLoss
* Optimización con SGD
* Persistencia del modelo (.pth)

###  Documentación

| Elemento | Descripción             |
| -------- | ----------------------- |
| Input    | Imagen (28x28)          |
| Output   | Dígito (0–9)            |
| Paso 1   | Vectorización de imagen |
| Paso 2   | Forward pass (MLP)      |
| Paso 3   | Cálculo de pérdida      |
| Paso 4   | Actualización de pesos  |

---

## 10. Clasificación de Imágenes con CNN (CIFAR-10)

Sistema de clasificación de imágenes utilizando redes neuronales convolucionales profundas.

###  Arquitectura

Imagen RGB → Convoluciones → Pooling → Flatten → Fully Connected → Predicción

###  Características técnicas

* Normalización de imágenes RGB
* Arquitectura CNN con múltiples capas convolucionales
* MaxPooling para reducción de dimensionalidad
* Dropout para regularización
* Entrenamiento en GPU (CUDA)
* Evaluación con métricas de exactitud

###  Documentación

| Elemento | Descripción                  |
| -------- | ---------------------------- |
| Input    | Imagen RGB                   |
| Output   | Clase (10 categorías)        |
| Paso 1   | Preprocesamiento             |
| Paso 2   | Extracción de features (CNN) |
| Paso 3   | Clasificación                |
| Paso 4   | Evaluación                   |

---

## 11. Modelos Secuenciales (RNN, LSTM, GRU)

Implementación comparativa de arquitecturas recurrentes para predicción de secuencias de texto.

###  Arquitectura

Secuencia de palabras → Embedding → RNN/LSTM/GRU → Fully Connected → Predicción

###  Características técnicas

* Construcción manual de vocabulario
* Codificación de texto a tensores
* Implementación de tres arquitecturas:

  * RNN básica
  * LSTM
  * GRU
* Modelado de dependencias temporales
* Predicción de la siguiente palabra

###  Documentación

| Elemento | Descripción              |
| -------- | ------------------------ |
| Input    | Secuencia de palabras    |
| Output   | Siguiente palabra        |
| Paso 1   | Tokenización manual      |
| Paso 2   | Conversión a índices     |
| Paso 3   | Procesamiento secuencial |
| Paso 4   | Predicción final         |

---

## 12. Técnicas de Regularización

Implementación de diferentes estrategias para mejorar la generalización de modelos y evitar overfitting.

###  Arquitectura

Dataset → Modelo → Regularización → Entrenamiento → Evaluación

###  Características técnicas

* Dropout (apagado aleatorio de neuronas)
* Batch Normalization
* L2 Regularization (weight decay)
* Early Stopping basado en validación
* Data Augmentation para imágenes

###  Documentación

| Elemento | Descripción                |
| -------- | -------------------------- |
| Input    | Dataset                    |
| Output   | Modelo regularizado        |
| Paso 1   | Aplicación de técnicas     |
| Paso 2   | Entrenamiento              |
| Paso 3   | Monitoreo de validación    |
| Paso 4   | Selección del mejor modelo |

---

## 13. Transfer Learning (ResNet)

Implementación de transferencia de aprendizaje utilizando un modelo preentrenado para clasificación de imágenes.

###  Arquitectura

Imagen → ResNet preentrenada → Fine-tuning → Predicción

###  Características técnicas

* Uso de ResNet18 preentrenado (ImageNet)
* Congelación de capas (feature extraction)
* Reemplazo de la capa fully connected
* Entrenamiento parcial del modelo
* Adaptación de input (resize a 224x224)

###  Documentación

| Elemento | Descripción            |
| -------- | ---------------------- |
| Input    | Imagen                 |
| Output   | Clase (10 categorías)  |
| Paso 1   | Preprocesamiento       |
| Paso 2   | Extracción de features |
| Paso 3   | Fine-tuning            |
| Paso 4   | Predicción             |

---

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
Ai Engineer
