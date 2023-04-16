from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import whisper
import multiprocessing

#Crete a new instance Flask class
app = Flask(__name__)
long_running_process = None
result = None

server_path = ""#"/var/www/html/apps/speech_text/"
audio_path = server_path + "audio.wav"
text_path = server_path + "output.txt"

lastDropdown = [""]

def dropdown():
    language = request.form.get("dropdown", False)
    lastDropdown[0] = str(language)
    return lastDropdown[0]

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        f = request.files['audio_data']
        with open(audio_path, 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')

        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")

#Audio uploader
@app.route('/upload', methods=['POST'])
def upload():
    #requiest the file name
    f = request.files['file']
    #save the audio file
    f.save(audio_path)
    print ('Audio file uploaded')
    return render_template('index.html', uploadedName=f.filename)
    #return redirect(url_for('transcribe'))  
    #return 'File uploaded successfully'

@app.route('/download')
def download_file():
    path = text_path   
    return send_file(path, as_attachment=True)

@app.route('/start-process')
def start_process():
    global long_running_process
    long_running_process = multiprocessing.Process(target=transcribe)
    long_running_process.start()
    return redirect(url_for('processing'))

@app.route('/processing')
def processing():
    return render_template('processing.html')

@app.route('/result')
def result():
    with open(text_path, 'r') as file:
        text = file.read()
        return render_template('result.html', text=text)

@app.route('/transcribe')#, methods=['POST'])
def check_process():
    global long_running_process
    # Check if the long-running task has completed
    if long_running_process and long_running_process.is_alive():
        return "processing"
    else:
        return "completed"

def transcribe():
    model = whisper.load_model("medium")
    #model = whisper.load_model("large-v2")

    # load the entire audio file
    audio = whisper.load_audio(audio_path)
    options = {
        #"language": "en", # input language, if omitted is auto detected
        "task": "transcribe" # or "transcribe" if you just want transcription
    }
    global result
    result = whisper.transcribe(model, audio, **options)
    #print(result["text"])
       # write the text to a file
    with open(text_path, "w", encoding='utf-8') as file:
        file.write(result["text"])
        os.remove(audio_path)
        return True            
    #return render_template('index.html', text=result["text"])
        
    
if __name__ == '__main__':
#    app.run(host="0.0.0.0", port=5000)
#    app.run()
    app.run(debug=True)