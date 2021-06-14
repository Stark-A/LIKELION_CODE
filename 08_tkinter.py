from tkinter import *   # tkinter안 모든 함수 다 불러옴 그리고 불러온 함수이름만 적어서 사용할수 있음
import pandas as pd
import os   # 디렉토리를 만들고, 삭제.... 현재 폴더 위치.

print(os.getcwd())

# 파일 불러오기
dat = pd.read_csv("./한국산업은행_금융 관련 용어_20151231.csv", encoding="euc-kr")
print(dat.columns)
# 기능 추가
# 제출 버튼을 클릭했을 때, 동작 기능.
def click(event=None):
    print("버튼이 클릭 되었습니다.")
    # pass
    word = entry.get()      # 아래 entry 상자의 내용을 text로 넣는다.
    # END로 지정하면 문자열이 입력된 최종 입력 지점을 의미.
    # 특정 지점부터 텍스트 엔트리 위젯의 끝까지 모두 지우기 위해 END를 쓴다.
    dv_output.delete(0.0, END) # 텍스트 박스 내용을 지운다.
    cf_output.delete(0.0, END)
    mean_output.delete(0.0, END)

    try:
        def_word = dat.loc[dat['용어'] == word, '구분'].values[0]
        def_word1 = dat.loc[dat['용어'] == word, '분류'].values[0]
        def_word2 = dat.loc[dat['용어'] == word, '설명'].values[0]
    except:
        def_word = "단어의 뜻을 찾을 수 없습니다."
        # dat = window_add(dat)

    dv_output.insert(END, def_word)
    cf_output.insert(END, def_word1)
    mean_output.insert(END, def_word2)

window = Tk()
window.title("My Dictionary")

# 01 입력 상자 설명 레이블
label = Label(window, text="원하는 단어 입력 후, 엔터 키 누르기")
label.grid(row=0, column=0, sticky=W)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=15, bg="light green")
entry.grid(row=1, column=0, sticky=W)

# 03 제출 버튼 추가
subm_b = Button(window, text="제출", width=8, command=click)
subm_b.grid(row=2, column=0, sticky=W)

# 04 설명 레이블 - 의미
dv_label = Label(window, text="\n구분:")
dv_label.grid(row=3, column=0,sticky=W)

cf_label = Label(window, text="\n분류:")
cf_label.grid(row=5, column=0,sticky=W)

mean_label = Label(window, text="\n설명:")
mean_label.grid(row=7, column=0,sticky=W)

# 05 텍스트 박스 입력 상자
# columnspan=2 는  (4,0~(4,1) 위치까지 분포
dv_output = Text(window, width=20, height=1, wrap=WORD, background="light green")
dv_output.grid(row=4, column=0, columnspan=2, sticky=W)

cf_output = Text(window, width=20, height=1, wrap=WORD, background="light green")
cf_output.grid(row=6, column=0, columnspan=2, sticky=W)

mean_output = Text(window, width=50, height=6, wrap=WORD, background="light green")
mean_output.grid(row=8, column=0, columnspan=2, sticky=W)
# 메인 반복문 실행
window.bind("<Return>",click)
window.mainloop()