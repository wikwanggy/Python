# from 패키지명 import 함수면
# from game.sound.echo import echo_test
from ..sound.echo import echo_test # relative 패키지


def render_test():
    print("render")
    echo_test()