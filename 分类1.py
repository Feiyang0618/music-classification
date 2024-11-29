import os
import shutil
from pydub import AudioSegment
import numpy as np
import librosa

def calculate_bpm(file_path):
    audio = AudioSegment.from_file(file_path)
    audio_data = np.array(audio.get_array_of_samples())
    audio_data = audio_data.astype(np.float32) / 32768  
    sr = audio.frame_rate
    tempo, _ = librosa.beat.beat_track(y=audio_data, sr=sr)
    return tempo

def classify_speed(bpm):   
    if 116 <= bpm < 120:
        return '5.0'
    elif 120 <= bpm < 124:
        return '5.2'
    elif 124 <= bpm < 128:
        return '5.4'
    elif 128 <= bpm < 132:
        return '5.6'
    elif 132 <= bpm < 136:
        return '5.8'
    elif 136 <= bpm < 140:
        return '6.0'
    else:
        return '其他'

def process_audio_files(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        audio_extensions = ('.mp3', '.wav', '.m4a', '.flac')

    for file_name in os.listdir(input_directory):
        file_path = os.path.join(input_directory, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(audio_extensions):
            try:
        
                bpm = calculate_bpm(file_path)

                speed_category = classify_speed(bpm)

                category_folder = os.path.join(output_directory, speed_category)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                shutil.copy(file_path, category_folder)

                print(f"文件 {file_name} 已被分类为速度 {speed_category}。")

            except Exception as e:
                print(f"处理文件 {file_name} 时发生错误: {e}")
        else:
            print(f"文件 {file_name} 被跳过，非音频文件。")

input_dir = r'E:\音乐'  
output_dir = r'E:\音乐分类'  
process_audio_files(input_dir, output_dir)
