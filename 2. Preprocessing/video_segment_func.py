import moviepy.editor as mp
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import re
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

#adjust target amplitude
def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)


def video_segment(MOV_Directory):
    
    MOV_List = os.listdir(MOV_Directory)

    for MOV in MOV_List:
        MOV_name = MOV_Directory + '/' + MOV

        clip = mp.VideoFileClip(MOV_name)
        
        sound_file_name = re.sub(pattern='mp4', repl='wav', string=MOV_name)
        clip.audio.write_audiofile(sound_file_name)

        audio_segment = AudioSegment.from_wav(sound_file_name)

#normalize audio_segment to -20dBFS 
        normalized_sound = match_target_amplitude(audio_segment, -20.0)
        print("length of audio_segment={} seconds".format(len(normalized_sound)/1000))

#Print detected non-silent chunks, which in our case would be spoken words.
        nonsilent_data = detect_nonsilent(normalized_sound, min_silence_len=300, silence_thresh=-20, seek_step=1)

        a = 1
#convert ms to seconds
        print("start,Stop")
        for chunks in nonsilent_data:
            time_line = [[chunk/1000 for chunk in chunks]]
            for i in time_line:
                print(i[0], i[1])
        
                b = str(a)
                ffmpeg_extract_subclip(MOV_name, i[0], i[1], targetname="./SEG_VID/"+MOV+b+".mp4")
                a += 1
    
    return './SEG_VID' #잘린 비디오 디렉토리







