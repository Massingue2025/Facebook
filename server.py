from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Dados da transmissão
STREAM_URL = 'rtmps://live-api-s.facebook.com:443/rtmp/'
STREAM_KEY = 'FB-745433421335513-0-Ab2151bh5oex3yr_ADWG_rRV'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    video = request.files['video']
    if video:
        filepath = os.path.join(UPLOAD_FOLDER, video.filename)
        video.save(filepath)

        cmd = [
            'ffmpeg',
            '-re',
            '-i', filepath,
            '-c:v', 'libx264',
            '-preset', 'veryfast',
            '-maxrate', '3000k',
            '-bufsize', '6000k',
            '-pix_fmt', 'yuv420p',
            '-g', '50',
            '-c:a', 'aac',
            '-b:a', '128k',
            '-f', 'flv',
            STREAM_URL + STREAM_KEY
        ]

        try:
            subprocess.run(cmd, check=True)
            return "Live finalizada com sucesso!"
        except subprocess.CalledProcessError:
            return "Erro ao transmitir o vídeo."
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)
                print(f"Arquivo removido: {filepath}")

    return "Erro: Nenhum vídeo foi enviado."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
