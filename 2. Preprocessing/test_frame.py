from moviepy.editor import VideoFileClip

def get_duration(filename):
    clip = VideoFileClip(filename)
    return clip.duration

mov = Whole_MOV_List() #전체 영상 리스트

mov_list = Two_min_under_MOV(mov) #2분 이하 영상들


one_anchor_s = one_anchor_starts_MOV(mov_list) #앵커 1명으로 시작하는 영상 리스트

one_anchor_cut = one_anchor_only(one_anchor_s) #앵커 한 명만 말하는 부분 자른 영상 디렉토리 반환
    
b = os.listdir(one_anchor_cut)
            
MOV_LIST = os.listdir(mov_list)

for i in MOV_LIST:
    for j in b:
        if i == j:
            new_i = './MOV/' + i
            new_j = './One_Anch'+'/'+j
            ffmpeg_extract_subclip(new_i, 0, get_duration(new_j), targetname="./CUT_VID/"+i+".mp4")

#CUT_VID라는 폴더에 사람이 한명만 있는 부분만 잘린 영상들이 저장되어 있음


seg_vid = video_segment('./CUT_VID')
#seg_vid에 문장 단위 영상이 존재
