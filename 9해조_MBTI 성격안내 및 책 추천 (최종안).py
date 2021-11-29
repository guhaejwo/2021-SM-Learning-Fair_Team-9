#MBTI를 입력하고 책 추천 받기

ans = 'Y' 
while ans == 'Y' :
   
   print("이 프로그램은 당신의 MBTI를 입력받아 그에 따른 성향을 알려주는 프로그램입니다!")
   mbti=input("MBTI를 입력해주세요   : ")
   print(" ")

   while True:
     if mbti == 'ISTJ' or 'istj' in mbti :
        print("당신은 책임감이 강해서 본인이 맡은 일은 열심히 하는 성격의 유형이군요!")
        print("당신은 익숙한 것을 좋아하며 직설적인 것을 좋아합니다.")
        print("당신의 장점은 쉽게 화내려 하지 않는다는 점입니다.")
        print("당신의 단점은 변화를 좋아하지 않고, 그에 쉽게 적응하지 못한다는 점입니다.")
        break

     elif mbti == 'ISFJ' or 'isfj' in mbti :
        print("당신은 약속을 중요하게 여기고 시간개념이 확실한 성격의 유형이군요!")
        print("당신은 어떤 일을 하더라도 체계적으로 해냅니다.")
        print("당신의 장점은 타인들보다 눈치가 빠르다는 점입니다.")
        print("당신의 단점은 본인만의 시간이 꼭 필요하다는 점입니다.")
        break

     elif mbti == 'INFJ' or 'infj' in mbti :
        print("당신은 다툼을 싫어하며 트렌드에 관심이 없는 성격의 유형이군요!")
        print("당신은 무엇인가 만드는 것을 선호합니다.")
        print("당신의 장점은 권유를 통해 사람들의 마음을 움직이는 지도력이 탁월하다는 점입니다.")
        print("당신의 단점은 너무나 비현실적인 면이 있다는 점입니다.")
        break

     elif mbti == 'INTJ' or 'intj' in mbti :
        print("당신은 체계적인 일을 좋아하고 독창성이 뛰어난 성격의 유형이군요!")
        print("당신은 완벽주의 성향을 가지고 있습니다")
        print("당신의 장점은 복잡한 일들을 효율성있게 해결한다는 점입니다.")
        print("당신의 단점은 어떤 일이던지 진행방식부터 알아보려한다는 점입니다.")
        break

     elif mbti == 'ISTP' or 'istp' in mbti :
        print("당신은 자기주장이 매우 강하고 전체적인 업무를 매우 잘하는 성격의 유형이군요!")
        print("당신은 마음에 없는 소리를 잘 하지 않습니다.")
        print("당신의 장점은 정밀하고 세밀화된 업무를 잘한다는 점입니다.")
        print("당신의 단점은 생각은 적극적이나 행동은 소극적이라는 점입니다.")
        break

     elif mbti == 'ISFP' or 'isfp' in mbti :
        print("당신은 자유로운 영혼의 소유자로 규칙을 좋아하지 않는 성격의 유형이군요!")
        print("당신은 자신을 규제하는 상황을 좋아하지 않습니다.")
        print("당신의 장점은 최대한 어색함을 없애려고 노력한다는 점입니다.")
        print("당신의 단점은 스트레스에 취약하다는 점입니다.")
        break

     elif mbti == 'INFP' or 'infp' in mbti :
        print("당신은 개인주의적 성향이 있으며 언어에 많은 관심과 호기심을 보이는 성격의 유형이군요!")
        print("당신은 타인과 친해지기 전에는 조용하지만 친해지면 매우 잘 지냅니다.")
        print("당신의 장점은 분쟁을 싫어하고 분쟁을 만들려고 하지 않는다는 점입니다.")
        print("당신의 단점은 감수성이 예민하고 멘탈이 약하다는 점입니다.")
        break

     elif mbti == 'INTP' or 'intp' in mbti :
        print("당신은 규율을 지키는 것을 좋아하며 화를 잘 내지 않는 성격의 유형이군요!")
        print("당신은 기본적인 매너가 있는 사람입니다.")
        print("당신의 장점은 화를 잘 내지 않는다는 점입니다.")
        print("당신의 단점은 연락이 다소 늦는다는 점입니다.")
        break

     elif mbti == 'ESTP' or 'estp' in mbti :
        print("당신은 실용적, 현실적, 행동지향적이며 어디서든 적응을 잘 하는 성격의 유형이군요!")
        print("당신은 새로운 환경이나 상황에 잘 적응하며 사교적입니다.")
        print("당신의 장점은 날카로운 관찰력과 기억력을 가지고 있다는 점입니다.")
        print("당신의 단점은 길게 생각하려하지 않아서 장기적인 목표를 세우기 힘들다는 점입니다.")
        break

     elif mbti == 'ESFP' or 'esfp' in mbti :
        print("당신은 스타성이 뛰어나며 사교적이고 활동적이며 즐거움을 추구하는 성격의 유형이군요!")
        print("당신은 친절하고 낙천적이며 타인에게 일어나는 일에 관심이 많습니다.")
        print("당신의 장점은 에너지가 많고 활동적이며 변화에 잘 적응한다는 점입니다.")
        print("당신의 단점은 감정에 약하고 민감하며 결정을 내리는 것을 힘들어한다는 점입니다.")
        break

     elif mbti == 'ENFP' or 'enfp' in mbti :
        print("당신은  다른 사람들과 함께 시간을 보내면서 에너지를 얻는 성격의 유형이군요! ")
        print("당신은 사실이나 세부사항들보다 아이디어나 개념에 집중하고 그에 따라 결정을 내립니다.")
        print("당신의 장점은 호기심이 많고, 활발하며 열정적이라는 점입니다.")
        print("당신의 단점은 자유나 자기표현을 중시하다보니 민감하다는 점입니다.")
        break
   
     elif mbti == 'ENTP' or 'entp' in mbti :
        print("당신은 대담하고 창의적인 경향이 있으며, 어떠한 저항이 있어도 목표를 힘차게 추구하는 성격의 유형이군요!")
        print("당신은 당신의 생각이나 아이디어를 거리낌없이 말하고 토론이나 논쟁을 즐깁니다.")
        print("당신의 장점은 다재다능하고, 활발한 성격으로 늘 자신감이 있다는 점입니다.")
        print("당신의 단점은 추진력은 좋으나 뒷심이 부족하다는 점입니다.")
        break

     elif mbti == 'ESTJ' or 'estj' in mbti :
        print("당신은 현실적이고 구체적이며 생산적인 일을 추구하는 성격의 유형이군요!")
        print("당신은 판단을 할 때 주관에 초점을 맞추지 않고, 사실과 논리를 고려합니다.")
        print("당신의 장점은 한 번 시작한 일은 끝까지 해내려고 한다는 점입니다.")
        print("당신의 단점은 융통성이 적고 완고한 성격이며 미래가능성을 보지 못한다는 점입니다.")
        break

     elif mbti == 'ESFJ' or 'esfj' in mbti :
        print("당신은 사람을 소중하게 여기고 타인을 돕는 것을 좋아하는 성격의 유형입니다.")
        print("당신은 다정하며 다른 사람을 돌보거나 도움을 주면서 즐거움과 성취감을 느낍니다.")
        print("당신의 장점은 남을 잘 서포트해주고 남에게 관심이 많다는 점입니다.")
        print("당신의 단점은 타인들의 필요에 몰두하여 스스로를 돌보지 않는다는 점입니다.")
        break

     elif mbti == 'ENFJ' or 'enfj' in mbti :
        print("당신은 활발하고 적극적이고, 사교적인 성격으로 다른 사람과의 인간관계를 중요하게 생각하는 성격의 유형이군요!")
        print("당신은 온화하고 부드러운 성품을 지녔으며 사회에 좋은 영감을 줄 수 있는 리더가 될 수 있습니다.")
        print("당신의 장점은 다른 사람들의 감정이나 생각을 잘 감지해낸다는 점입니다.")
        print("당신의 단점은 논리적인 사고가 부족하고, 객관성이 부족하다는 점입니다.")
        break

     elif mbti == 'ENTJ' or 'entj' in mbti :
        print("당신은 솔직하고 단호하면서도 매사에 열정적이며 지도력과 통솔력이 있는 성격의 유형이군요!")
        print("당신은 지식에 대한 관심이 많으며 장기적인 계획을 세우고, 창조적인 문제해결을 선호합니다.")
        print("당신의 장점은 적극적이고 카리스마와 리더십을 가지고 모임이나 대화를 이끌어나갈 수 있다는 점입니다.")
        print("당신의 단점은 참을성이 부족하고, 자신감과 의지력이 지나치면 자신의 의견만을 밀어붙인다는 점입니다.")
        break

     else  :
        print("잘못된 대답입니다!")
        mbti=input("MBTI를 입력해주세요 : ")

   print(" ")
   print("그런 당신께 책을 추천드릴까요?")

   ans=input("네 / 아니오 : ")

   while True:
  
     if ans == "네" :
         if mbti == 'ISTJ' or 'istj' in mbti :
            print("ISTJ인 당신!  당신을 위한 추천도서는 리처드 도킨스의 '이기적 유전자'입니다!")
            print("이 도서를 추천하는 이유는 논리주의자이며 신속 정확한 당신에게 알맞는 책이기 때문입니다.")
            break
      
      
         elif mbti == 'ISFJ' or 'isfj' in mbti :
            print("ISFJ인 당신! 당신을 위한 추천도서는 제인 오스틴의 '오만과 편견'입니다!")
            print("이 도서를 추천하는 이유는 수호자이며 이타주의적인 당신에게 알맞는 책이기 때문입니다.")
            break
      
         elif mbti == 'INFJ' or 'infj' in mbti :
            print("INFJ인 당신! 당신을 위한 추천도서는 헤르만 헤세의 '데미안'입니다!")
            print("이 도서를 추천하는 이유는 옹호자이며 섬세한 당신에게 알맞는 책이기 때문입니다.")
            break
      
         elif mbti == 'INTJ' or 'intj' in mbti :
            print("INTJ인 당신! 당신을 위한 추천도서는 김유진의 '나의 하루는 4시 30분에 시작된다'입니다!")
            print("이 도서를 추천하는 이유는 전략가이며 상상력이 풍부하며 원칙주의적인 당신에게 알맞는 책이기 때문입니다.")
            break
      
         elif mbti == 'ISTP' or 'istp' in mbti :
            print("ISTP인 당신! 당신을 위한 추천도서는 랜들 먼로의 '더 위험한 과학책'입니다!")
            print("이 도서를 추천하는 이유는 만능재주꾼이며 호기심이 많고, 이성주의적인 당신에게 알맞기 때문입니다.")
            break
      
         elif mbti == 'ISFP' or 'isfp' in mbti :
            print("ISFP인 당신! 당신을 위한 추천도서는 구병모의 '위저드 베이커리'입니다!")
            print("이 도서를 추천하는 이유는 예술가이며 무엇이든 자신만의 시각으로 재해석하는 당신에게 알맞은 책이기 때문입니다.")
            break
      
         elif mbti == 'INFP' or 'infp' in mbti :
            print("INFP인 당신! 당신을 위한 추천도서는 한강의 '소년이 온다'입니다!")
            print("이 도서를 추천하는 이유는 중재자이며 긍정적인 이상주의자인 당신에게 알맞는 책이기 때문입니다.")
            break
      
         elif mbti == 'INTP' or 'intp' in mbti :
            print("INTP인 당신! 당신을 위한 추천도서는 유발 하라리의 '사피엔스'입니다!")
            print("이 도서를 추천하는 이유는 사색가이며 독창성과 창의력이 뛰어난 당신에게 알맞는 책이기 때문입니다.")
            break
      
         elif mbti == 'ESTP' or 'estp' in mbti :
            print("ESTP인 당신! 당신을 위한 추천도서는 김민철의 '모든 요일의 여행'입니다!")
            print("이 도서를 추천하는 이유는 삶을 즐기는 것을 좋아하고, 홀로 집에 있는 것을 싫어하는 당신에게 알맞은 책이기 때문입니다.")
            break
      
         elif mbti == 'ESFP' or 'esfp' in mbti :
            print("ESFP인 당신! 당신을 위한 추천도서는 하이케 팔러의 '100 인생 그림책'입니다!")
            print("이 도서를 추천하는 이유는 흥이 많고, 활동적이며 사교적인 당신에게 알맞은 책이기 때문입니다.")
            break
      
         elif mbti == 'ENFP' or 'enfp' in mbti :
            print("ENFP인 당신! 당신을 위한 추천도서는 정세랑의 '시선으로부터'입니다!")
            print("이 도서를 추천하는 이유는 인간비타민이며 긍정적이고 사교적인 당신에게 알맞은 책이기 때문입니다.")
            break
      
         elif mbti == 'ENTP' or 'entp' in mbti :
            print("ENTP인 당신! 당신을 위한 추천도서는 김난도, 전미영 외 7명의 '트렌드 코리아 2021'입니다!")
            print("이 도서를 추천하는 이유는 아이디어 뱅크이며 호기심이 많아 새로운 것을 좋아하고 토론을 좋아하는 당신에게 알맞기 때문입니다.")
            break
      
         elif mbti == 'ESTJ' or 'estj' in mbti :
            print("ESTJ인 당신! 당신을 위한 추천도서는 할 엘로드의 '미라클 모닝'입니다!")
            print("이 도서를 추천하는 이유는 자기계발을 열심히 하고자하는 당신에게 알맞은 책이기 때문입니다.") 
            break
      
         elif mbti == 'ESFJ' or 'esfj' in mbti :
            print("ESFJ인 당신! 당신을 위한 추천도서는 김수현의 '애쓰지 않고 편안하게'입니다!")
            print("이 도서를 추천하는 이유는 수다쟁이 인기인이며 인간관계를 중시하는 당신에게 알맞은 책이기 때문입니다.")
            break
      
         elif mbti == 'ENFJ' or 'enfj' in mbti :
            print("ENFJ인 당신! 당신을 위한 추천도서는 호프 자런의 '나는 풍요로웠고, 지구는 달라졌다'입니다!")
            print("이 도서를 추천하는 이유는 관심사가 다양하고, 영향력을 행사하는 것을 좋아하는 당신에게 알맞는 책이기 때문입니다.")
            break
      
         elif mbti == 'ENTJ' or 'entj' in mbti :
            print("ENTJ인 당신! 당신을 위한 추천도서는 권오현의 '초격차: 리더의 질문'입니다!")
            print("이 도서를 추천하는 이유는 타고난 리더이며 강하고 담대한 리더십을 가진 당신에게 알맞은 책이기 때문입니다.")
            break
      

     elif ans == "아니오" :
         
         break
  

     else :
       print("잘못된 대답입니다!")
       ans=input("네 / 아니오 : ")
       
   ans = input("다른 유형을 더 알아보시겠습니까? ( Y / N ): ")
ans = 'N'
ans = input("프로그램을 종료합니다!")
