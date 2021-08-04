from moviepy.editor import VideoFileClip

def get_duration(filename):
    clip = VideoFileClip(filename)
    return clip.duration

mov = Whole_MOV_List() #전체 영상 리스트

mov_list = Two_min_under_MOV(mov) #2분 이하 영상들


one_anchor_s = one_anchor_starts_MOV(mov_list) #앵커 1명으로 시작하는 영상 리스트

one_anchor_cut = one_anchor_only(one_anchor_s) #앵커 한 명만 말하는 부분 자른 영상 디렉토리 반환
switch_result = Switching_moment() #목소리 달라지는 부분에서WAV 파일 cut한 result table return


a = os.listdir(switch_result[WAV_name]) #이 부분 result_table이 어떤 방식으로 나오는 것인지 헷갈림...
a = re.sub(pattern='.wav', repl='.mp4', string=a)
    
b = os.listdir(one_anchor_cut)
            
MOV_LIST = os.listdir(mov_list)

for i in MOV_LIST:
    if i == a && i == b:
        new_a = re.sub(pattern='.mp4', repl='.wav', string=a)
        new_b = './One_Anch'+'/'+b
        if switch_result[]  > get_duration(new_b): #switch_result에서 원하는 TimeStamp 어떻게 뽑이내지...?
            ffmpeg_extract_subclip(i, 0, switch_result[], targetname="./CUT_VID/"+i+".mp4")
        else:
            ffmpeg_extract_subclip(i, 0, get_duration(new_b), targetname="./CUT_VID/"+i+".mp4")

seg_vid = video_segment('./CUT_VID')

cut_face = video_frame_face(seg_vid)
