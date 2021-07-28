import moviepy.editor as mp
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import re
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

MOV_Directory = 'video.mp4' 

i2 = MOV_Directory
print(i2)
clip = mp.VideoFileClip(i2)
    
# [필수] 파일 주소 재설정 
sound_file_name = re.sub(pattern='mp4', repl='wav', string=i2)
print(sound_file_name)
clip.audio.write_audiofile(sound_file_name)

#adjust target amplitude
def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

#Convert wav to audio_segment
audio_segment = AudioSegment.from_wav(sound_file_name)

#normalize audio_segment to -20dBFS 
normalized_sound = match_target_amplitude(audio_segment, -20.0)
print("length of audio_segment={} seconds".format(len(normalized_sound)/1000))

#Print detected non-silent chunks, which in our case would be spoken words.
nonsilent_data = detect_nonsilent(normalized_sound, min_silence_len=500, silence_thresh=-20, seek_step=1)

a = 1
#convert ms to seconds
print("start,Stop")
for chunks in nonsilent_data:
    time_line = [[chunk/1000 for chunk in chunks]]
    for i in time_line:
        print(i[0], i[1])
        
        b = str(a)
        ffmpeg_extract_subclip("video.mp4", i[0], i[1], targetname="video"+b+".mp4")
        a += 1

#1, 단어별이나 문장별로 안 나온다. amplitude와 min_silence_len을 조절해볼 것
#2, 앵커가 말하는 부분만을 자르지 않았다. -> 이 문제는 상의해야 함
#   아직 앵커가 말하고 있음에도 불구하고, 화면 전환이 일어나며 얼굴이 나타나지 않음
#   이건 큰 화면 전환을 기준으로 잘라야 하는 문제일듯
#3, 이 코드들을 함수로 만들어 사용할 것 - 작은 문제



