
# # 패키지 안의 함수 실행하기
# # 1.echo 모듈을 import하여 실행하기
# import game.sound.echo
# game.sound.echo.echo_test()
# # 2.echo 모듈이 있는 디렉토리까지 from...import하여 실행하기
# from game.sound import echo
# echo.echo_test()
# # 3.echo 모듈의 echo_test 함수를 직접 import
# from game.sound.echo import echo_test
# echo_test()


#import game
#echo_test()

#import game.sound.echo.echo_test

# from game.sound import *
# echo.echo_test()

from game.graphic.render import render_test
render_test()