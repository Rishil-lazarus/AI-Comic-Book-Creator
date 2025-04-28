#AI Comic Book Creator
Built an AI-powered comic book creation system that transforms stories into digital comic books. Using Stable Diffusion for comic-style image generation, the system divides the story into scenes and generates illustrations with speech bubbles. The final comic book is exported as a downloadable PDF.

📂 Dataset
Dataset Name: Custom Story Dataset (for testing purposes)
Source: User-provided stories
Features:

Story text is parsed and split into scenes

Each scene is matched with a comic-style illustration generated using Stable Diffusion

🛠️ Features
🧠 Stable Diffusion-based comic illustration generation
🔄 Dynamic speech bubble placement (based on dialogue in quotes)
🎯 Story-to-image translation for comic panels
📊 PDF export of the complete comic book
🌐 Flask-based web app with a modern dark theme UI for an engaging user experience
⚙️ Optimized for generating comics from user-inputted stories

🏗️ Project Structure

app/: Flask web app and backend code

static/: Static assets (CSS, images)

templates/: HTML templates for the web interface

comic_generator/: Python scripts for story parsing, image generation, and comic PDF creation

requirements.txt: Project dependencies

📊 Model & Performance

Stable Diffusion Model for comic-style image generation

Performance Goal: Create high-quality illustrations that match the story context

Evaluation: Visual quality, consistency of speech bubbles, and story-to-image coherence

💻 Tech Stack

Python 

Flask (for web app development)

Stable Diffusion (for image generation)

TensorFlow (for AI-related processing)

HTML/CSS (for frontend)

📦 Installation
Clone the Repository:
git clone https://github.com/Rishil-lazarus/AI-Comic-Book-Creator.git
cd AI-Comic-Book-Creator

Install Dependencies:
pip install -r requirements.txt

Run the Web App:
python app.py
