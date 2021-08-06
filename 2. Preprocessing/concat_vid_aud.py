from moviepy.editor import *
import re

def concat_vid (MOV_Directory, Audio_Directory):

    MOV_List = os.listdir(MOV_Directory)

    AUD_List = glob.glob(Audio_Directory + '*.wav')
    AUD_List = os.listdir(AUD_List)

    for MOV in MOV_List:
        for AUD in AUD_List:
            mov = re.sub(pattern='.mp4', repl='', string=MOV)
            aud = re.sub(pattern='.wav', repl='', string=AUD)

            if mov == aud:
                MOV_name = MOV_Directory + '/' + MOV
                AUD_name = Audio_Directory + '/' + AUD
                videoclip = VideoFileClip(MOV_name)
                audioclip = AudioFileClip(AUD_name)
                new_audioclip = CompositeAudioClip([audioclip])
                videoclip.audio = new_audioclip
                videoclip.write_videofile(MOV_name)

