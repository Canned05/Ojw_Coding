std = dict()    #딕셔너리 선언 
while True :
    print("=====================================================================")
    print("1.입력  2.검색  3.수정  4.삭제  5.출력  6.종료 ")
    print("=====================================================================")
    select = int(input())       #사용자에게 입력받음
    if select == 1:     #입력을 선택할 시
        try:
            id = int(input("학번 :")) 

        except:     #학번을 숫자가 아닌 다른 값으로 입력시
            print("학번을 숫자로 입력하세요")
            continue

        if id not in std:       #학생 정보 중복 안될 시   
            name = input("이름 :")
            kor = int(input("국어 :"))
            mth = int(input("수학 :"))
            eng = int(input("영어 :"))
            soc = int(input("사회 :"))
            his = int(input("역사 :"))

            total = kor+mth+eng+soc+his
            avg = round(total/5,2)
            std[id] = [name,kor,mth,eng,soc,his,total,avg]
            continue
        else:
            print("학생이 이미 존재합니다")

    if select == 2:     #검색을 선택할 시
        try:
            sch_id = int(input("검색 학번 :"))      #학번 검색
            
        except:     #학번이 숫자가 아닐 시 
            print("학번을 숫자로 입력하세요")
            continue               

        if sch_id not in std:       #일치하는 학생이 없을 시 
            print("일치하는 학번이 없습니다 다시 입력하세요")
            
        elif sch_id in std:         #일치 학생이 있을 시 
            print("이름\t국어\t수학\t영어\t사회\t역사\t총점\t평균")   
            for i in std[sch_id]:
                print(i, end='\t')
            print()
    if select == 3:     #수정을 선택할 시
        try:
            id = int(input("학번 :"))       #검색 학번을 입력받음

        except:     #학번이 숫자가 아닐 시
            print("학번을 숫자로 입력하세요")       
            continue        
        
        if id in std:       #검색한 학생이 있을시   
            name = input("이름 :")
            lang = int(input("국어 :"))
            mth = int(input("수학 :"))
            eng = int(input("영어 :"))
            soc = int(input("사회 :"))
            his = int(input("역사 :"))
            total = kor+mth+eng+soc+his
            avg = round(total/5,2)
            std[id] = [name,kor,mth,eng,soc,his,total,avg]      #수정 정보 기존 정보에 덮어씀
            continue
        
        elif id not in std:     #일치 학번이 없을 시
            print("일치하는 학번이 없습니다 다시 입력하세요")
        
    if select == 4:     #삭제 선택 시 
        try:
            del_id = int(input("삭제 시킬 학번을 입력하세요 :"))
            
        except:     #학번이 숫자가 아닐 시
            print("학번을 숫자로 입력하세요 :")
            continue        
        
        if del_id in std:       #삭제할 학생 정보가 있을 시
           del std[del_id]      #del 함수 사용하여 삭제 시킴
           
        
        elif del_id not in std:     #삭제할 학생 정보가 없을 시
            print("일치하는 학번이 없습니다 다시 입력하세요")
            
    if select == 5:     #출력을 선택할 시
        print("이름\t국어\t수학\t영어\t사회\t역사\t총점\t평균")   
        for s in std:
            for i in std[s]: 
                print(i, end='\t')
            print()
       


    if select == 6:     #종료 선택 시 
        break       #사용 종료
    
    
